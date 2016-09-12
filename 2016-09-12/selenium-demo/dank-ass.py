from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# import my naughty strings text file
with open("naughty-strings.txt") as f:
    naughties = f.readlines()

# for every naughty string
for n in naughties:

    # start firefox yo
    driver = webdriver.Firefox()

    # load up the pleb site
    driver.get("http://gogobooks.link/")
    
    # just wait a damn second for demo purposes
    time.sleep(1)

    # identify the input field
    inputbox = driver.find_element_by_name("p")

    # clear input field
    inputbox.clear()

    # send my naughty string tehehehe
    inputbox.send_keys(n)
    try:
        inputbox.send_keys(Keys.RETURN)
    except:
        pass
    
    # close dat browser
    driver.close()
