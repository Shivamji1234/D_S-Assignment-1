from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Q1. Write a python program to extract the video URL of the first five videos.
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.youtube.com/@PW-Foundation/videos")
titles=driver.find_elements(By.ID,"video-title")
data1=[]
for i in range(2):
    time.sleep(1)
    ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
video_link=driver.find_elements(By.ID,"video-title-link")
for i in range (5):
    data1.append(video_link[i].get_attribute('href'))
print(data1)
driver.quit()


#Q2. Write a python program to extract the URL of the video thumbnails of the first five videos.
driver=webdriver.Firefox()    
driver.get("https://www.youtube.com/@PW-Foundation/videos")
driver.implicitly_wait(10)
for i in range(2):
    time.sleep(1)
    ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
thumbnails=driver.find_elements(By.XPATH,'//div[@id="thumbnail"]//a[@id="thumbnail"]/yt-image/img')
data2=[]
for i in range (5):
    try:
        data2.append(thumbnails[i].get_attribute('src'))
    except:
        print("failed")
driver.quit()      
print(data2)
#Q3. Write a python program to extract the title of the first five videos.
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.youtube.com/@PW-Foundation/videos")
for i in range(2):
    time.sleep(1)
    ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
data3=[]
titles=driver.find_elements(By.ID,"video-title")
for i in range(5):
    try:
        data3.append(titles[i].text)
    except:
        print("failed")
driver.quit()
print(data3)
#Q4. Write a python program to extract the number of views of the first five videos.
driver=webdriver.Firefox()
driver.implicitly_wait(10)
data4=[]
for i in data1:
    time.sleep(2)
    driver.get(i)
    more=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/div[1]/yt-formatted-string/span[1]')
    body = driver.find_element(By.TAG_NAME,"body")
    body.send_keys(Keys.PAGE_DOWN)
    more.click()
    view=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/div[1]/yt-formatted-string/span[1]')
    data4.append(view.text) 
driver.quit()   
print(data4) 
#Q5. Write a python program to extract the time of posting of video for the first five videos.
driver=webdriver.Firefox()
driver.implicitly_wait(10)
data5=[]
for i in data1:
    driver.get(i)
    more=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/div[1]/yt-formatted-string/span[1]')
    body = driver.find_element(By.TAG_NAME,"body")
    body.send_keys(Keys.PAGE_DOWN)
    more.click()
    date=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/div[1]/yt-formatted-string/span[3]')
    data5.append(date.text) 
driver.quit()     
print(data5)    
 

