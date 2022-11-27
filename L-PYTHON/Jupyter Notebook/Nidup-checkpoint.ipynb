# Login to your insta id, search for a keyword, download all images in a particular folder.
#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from pathlib import Path

# To connect webdriver
current_path = str(Path().absolute())
driver = webdriver.Chrome(current_path + "/chromedriver.exe")
driver.get("https://www.instagram.com/now._you._know._me/saved/hot/17880820292407971/")

# Target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Will enter our username and password
username.clear()
username.send_keys("now._you._know._me")
password.clear()
password.send_keys("manish2352")

# This code will target the login button and press it.
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)
print("You have signed in" )
# disable the alert
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

# search for the hashtag cat
keyword = "#milliebobbybrown"
searchbox.send_keys(keyword)
print("You have searched for", keyword)

# FIXING THE DOUBLE ENTER
time.sleep(5)  # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()


# scroll down n times, here it's
n_scrolls = 1
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

#target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]
print('Found ' + str(len(anchors)) + ' links to images')
anchors[:5]
# follow each image link and extract only image at index=1
images = []
for a in anchors:
    driver.get(a)
    time.sleep(1)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])
images[:5]

# We'll save all the images there
import os
import wget
#download images
counter = 0
path = current_path + "\pic"
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
