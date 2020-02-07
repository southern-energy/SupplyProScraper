import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import Options
import requests
import bs4
import re
import json

# Original Method when I started using Selenium
# print("Real Browser Launching")
browser = webdriver.Chrome("./chromedriver.exe")
# print("Real Browser has Launched")


# print("Headless Browser Running")
# options = Options()
# options.add_argument("--headless") # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('--disable-gpu')  # applicable to windows os only
# options.add_argument('start-maximized') # 
# options.add_argument('disable-infobars')
# options.add_argument("--disable-extensions")
# browser = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver.exe')
# print("Headless Browser has Launched")

# Creating Session

session = requests.Session()

def site_session_login():
    browser.get("https://www.hyphensolutions.com/MH2SUPPLY/LogIn.asp")
    with open('./SupplyProLoginInfo.json') as login_data:
        data = json.load(login_data)
    username = data['username']
    password = data['password']
    session.post("https://www.hyphensolutions.com/MH2SUPPLY/LogIn.asp", data = dict(user_name=username, password=password))
site_session_login()

def site_login():
    browser.get("https://www.hyphensolutions.com/MH2SUPPLY/LogIn.asp")
    with open('./SupplyProLoginInfo.json') as login_data:
        data = json.load(login_data)
    username = data['username']
    password = data['password']
    browser.find_element_by_name("user_name").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_name("cmdSubmit").click()
site_login()


def force_login():
    # print(browser.current_url)
    if browser.current_url == ("https://www.hyphensolutions.com/MH2Supply/Login.asp?user%5Fname=Builder+Services&force%5Fsignon=Y&DM1Redir=") :
        # print(f"We have to force the login.")
        with open('./SupplyProLoginInfo.json') as login_data:
            data = json.load(login_data)
        username = data['username']
        password = data['password']
        browser.find_element_by_name("user_name").send_keys(username)
        browser.find_element_by_name("password").send_keys(password)
        browser.find_element_by_name("force_signon").click()
        browser.find_element_by_name("cmdSubmit").click()
    else:
        return 'We did not have to force the log in.'

force_login()

def navigate_to_future_orders():
    # print("We are inside future orders.")
    session.get("https://www.hyphensolutions.com/MH2Supply/Reports/PotentialOrders.asp?days=60&sessid=")
    browser.get("https://www.hyphensolutions.com/MH2Supply/Reports/PotentialOrders.asp?days=60&sessid=")
navigate_to_future_orders()

def interact_with_future_orders_page():
    browser.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[1]/tbody/tr[2]/td[2]/select")

# ========================================

def select_dan_ryan_SC():
    browser.find_element_by_name("account_id").send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.RETURN)
    browser.find_element_by_name("rows_per_page").send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.RETURN)
    browser.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/th[7]/a/span/b").click()
    Text_For_Counter = browser.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[1]/tbody/tr[1]/td[3]/b").text
    # print(Text_For_Counter)
    try:
        number_of_items = (re.findall(r'^\d\d\d',Text_For_Counter))
        number_of_items = int(number_of_items[0])
    except:
        number_of_items = (re.findall(r'^\d\d',Text_For_Counter))
        number_of_items = int(number_of_items[0])
    print(number_of_items)
    Text_For_Counter = browser.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[1]/tbody/tr[1]/td[3]/b").text
    # Variable for how many pages we need to scrape.
    try:
        number_of_pages = (re.findall(r'\d\d$',Text_For_Counter))
        number_of_pages = int(number_of_pages[0])
    except:
        number_of_pages = (re.findall(r'\d$',Text_For_Counter))
        number_of_pages = int(number_of_pages[0])

    print(number_of_pages)

    if number_of_pages == None:
        tr_elements = browser.find_elements_by_xpath('/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[2]/tbody/tr')
        i = 0
        for i in range(1, len(tr_elements)):
            # print(i)
            print(tr_elements[i].text, end='\n')
    else:
        i = 0
        while i < number_of_pages:
            # print(i)
            # print(number_of_pages)
            tr_elements = browser.find_elements_by_xpath('/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[2]/tbody/tr')
            for i in range(1, len(tr_elements)):
                # print(i)
                print(tr_elements[i].text, end='\n')
            browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/form/table[1]/tbody/tr[2]/td[3]/input[3]').send_keys(Keys.RETURN)
            i += 1

select_dan_ryan_SC()

# TODO: See if there is a way that we can combine the output of the while loop that scrapes through multiple pages. If not, we can just use Standard Output during execution in Bash script.
# TODO: When having to replicate steps, use JSON file to direct the scraper for each builder and subdivision.