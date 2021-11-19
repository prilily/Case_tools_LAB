from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

#make an object and path of chrome driver downloaded
web=webdriver.Chrome("/home/milano/apps/chromedriver")
web.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(1)

#create login variable and add path
# to find path via web scraping
'''
findelelment by xpath many approach to do it
- in fields, inspect, copy, dropdown list, copy full x path
- then in send keys, add the value thatyou will send, your phone number/emaiid
- now let us automate sign in
- next take button continue, copy x path, and add it to the continue variable
- then we send mouse click input event 
- submit.click() and no
- then run by python3 login.py
- then automatically input will be n and button click
- next code file search.py for adding product
'''

login= web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
login.send_keys("") #add your email./ phone number
Submit=web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
Submit.click()
