from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Obtain User Data needed for Login Process
uname = input("Enter your Instagram Username: ")
pw = input("Enter your Instagram Password: ")
url=input("Enter the URL of the Post you want to extract Comments from: ")

# Initialize the WebDriver
driver = webdriver.Firefox()

login ="https://www.instagram.com"

driver.get(login) 

time.sleep (2)

# Login process
username=driver.find_element(By.NAME,"username")
username.send_keys (uname)

password =driver.find_element (By.NAME,"password")
password.send_keys(pw)
password.submit()

time.sleep(7)

driver.get(url)
time.sleep(2)

# Wait for the comments section to load
comments_container_xpath = "//div[contains(@class, 'x5yr21d') and contains(@class, 'xw2csxc') and contains(@class, 'x1odjw0f') and contains(@class, 'x1n2onr6')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, comments_container_xpath)))

# Function to scroll and load all comments
def load_all_comments(driver):
    comments_container = driver.find_element(By.XPATH, comments_container_xpath)
    last_height = driver.execute_script("return arguments[0].scrollHeight", comments_container)

    while True:
        try:
    # Scroll down the comments container
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", comments_container)
            time.sleep(4)
                
    # Check if the comments container height has changed
            new_height = driver.execute_script("return arguments[0].scrollHeight", comments_container)
            if new_height == last_height:
                break
            last_height = new_height

        except Exception as e:
            print(f"An error occurred: {e}")
            break    

# Load all comments
load_all_comments(driver)

soup = BeautifulSoup(driver.page_source, features="lxml")

# find all comments divs
comments = soup.find_all("div", {"class": "x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"})

# initialize data storage
data = {}
index = 0

# extract information from each comment div
for comment in comments:
    content_div = comment.find_all("span", class_=lambda c: c.startswith("x1lliihq "))  # Look for class starting with "x9f619"
        
    if content_div:
        content = [c.get_text() for c in content_div]  
        try:
            data[index] = {"URL":url,"User":content[0],"Content":content[2], "Likes":content[3]} # add all gathered information to data storage
            index += 1
        except Exception as e:
            print("One Comment could not be extracted") # In case not all information could be extracted
    else:
        content = ""  # in case the content_div wasn't found in the comment div

# create a dataframe with all comments
df = pd.DataFrame.from_dict(data, orient="index")
df = df.drop_duplicates()
df["Likes"] = df["Likes"].apply(lambda x: "0 likes" if x == "Reply" else x)

now = datetime.now() # created datetimestamp to name csv file
df.to_csv(f"extracted_comments_{now.timestamp()}.csv") # export csv file with comments