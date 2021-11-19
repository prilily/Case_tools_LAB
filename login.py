email=""
passwords=""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_argument("--incognito")
web= webdriver.Chrome(options=options)


web.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
login=web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
login.send_keys(email)

next=web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
next.click()

time.sleep(5)

password=web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
password.send_keys(passwords)
submit=web.find_element_by_id("passwordNext")
time.sleep(3)
submit.click()

time.sleep(2)

compose=web.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
compose.click()

# decide to,subject and letter then send

to= web.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[6]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/input")
time.sleep(2)
to.send_keys("priyankamessage@gmail.com")
time.sleep(1)
subject=web.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[6]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div[3]/input")
time.sleep(2)
subject.send_keys("automation with selenuim testing")
time.sleep(2)
message=web.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[6]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div")
time.sleep(2)
message.send_keys("hello there, this is sent via automation. Let's hope it is successful. Good Day Sunshine!")

time.sleep(1)
send=web.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[6]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]")
time.sleep(2)
send.click()
time.sleep(5)

logout_menu=web.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]")
logout_menu.click()
time.sleep(2)

signout=web.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[4]/div[5]/a")
time.sleep(2)
signout.click()

time.sleep(2)

web.close()


