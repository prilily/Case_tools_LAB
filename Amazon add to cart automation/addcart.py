from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome()
#driver.get("www.amazon.in")

web= webdriver.Chrome("/home/milano/apps/chromedriver")
'''
- to add product, a variable for product URL
- now call parameter as a variable (which has url) in web.get
- then get xpath of product for add to cart button, 
'''

producturl="https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_2_sspa?keywords=macbook+pro&qid=1637066129&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQSUhQWE1QTjNBSFUmZW5jcnlwdGVkSWQ9QTAzMTUxNzQzVUMyUTNQV0U4UUQxJmVuY3J5cHRlZEFkSWQ9QTA1MTkzNDlWQ0xJUEo0Nk9DTDcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
web.get(producturl)

addtocart=web.find_element_by_xpath("/html/body/div[4]/div[2]/div[3]/div[7]/div[7]/div/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[35]/div[1]/span/span/span/input")
addtocart.click()