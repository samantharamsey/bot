# -*- coding: utf-8 -*-
'''
A bot to auto swipe on tinder and send a message if you match
'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


def login():
    # click login button
    login_element = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'
    login = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, login_element)))
    login.click()
    
    # choose facebook as login method
    fb_element = '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button'
    fb = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, fb_element)))
    fb.click()
    
    # direct bot to navigate to popup facebook login window
    workspace = driver.window_handles[0]
    popup = driver.window_handles[1]
    driver.switch_to.window(popup)
    
    # facebook login credentials
    email_fb = driver.find_element_by_xpath('//*[@id="email"]')
    email_fb.send_keys('FACEBOOK EMAIL')
    pw_fb = driver.find_element_by_xpath('//*[@id="pass"]')
    pw_fb.send_keys('FACEBOOK PASSWORD')
    
    # click login
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    # navigate back to primary tinder window
    driver.switch_to.window(workspace)

def popups():
    # allow tinder to use location
    loc_element = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
    loc = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, loc_element)))
    loc.click()
    
    # not interested in notifications
    notif_element = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]'
    notif = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, notif_element)))
    notif.click()
    
    # accept cookies
    cook_element = '//*[@id="content"]/div/div[2]/div/div/div[1]/button'
    cook = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, cook_element)))
    cook.click()
    
def send_likes():
    # click like button
    like_element = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'
    like = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, like_element)))
    like.click()
    
def send_nope():
    # click nope button
    nope_element = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button'
    nope = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, nope_element)))
    nope.click()
    
    
def send_msg(text):
    # type message in text box
    textbox = driver.find_element_by_xpath('//*[@id="chat-text-area"]')
    textbox.send_keys(text)
    
    # send message
    mess_element = '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button'
    mess = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, mess_element)))
    mess.click()
    
def more_popups():
    try:
        # decline to send a super like to a popular user
        pop_element = '//*[@id="modal-manager"]/div/div/button[2]'
        pop = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, pop_element)))
        pop.click()
    except:
        # decline other random tinder stuff
        element = '//*[@id="modal-manager"]/div/div/div[2]/button[2]'
        ele = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, element)))
        ele.click()
    
    
if __name__ == "__main__":
    
    # number of likes to send
    num = 15
    # message to send to matches
    text = r'hi'
    # create a randomized list of time intervals
    time = [random.uniform(1, 3) for i in range(num)]
    
    # open the webbrowser and navigate to tinder
    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path= r"C:\Users\saman\chromedriver\chromedriver.exe")
    driver.get('http://tinder.com/')
    
    # do the things :)
    login()
    popups()
    for i in range(num):
        try:
            # wait a random amount of time before sending next like
            sleep(time[i])
            # also send some nopes to look slightly less suspish
            if time[i] < 2.75:
                send_likes()
            else:
                send_nope()
        except:
            # if can't send like, send message
            try:
                send_msg(text)
            # if can't send message, close random pop up
            except:
                more_popups()
    

    

    