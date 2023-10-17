# Access the given Insta page get the data as per requirements 

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Insta:

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Access into the given webpage 
    
    def access_insta(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
        except Exception as e:
            print("url error on: ",e)
            
# Acquire the required data using XPATH only either it may be Relative or Absolute 

    def follower_following(self):
        try:
            self.access_insta()
            followers = self.driver.find_element(by=By.XPATH, value ='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button').text
            print("Total Followers of Guvi Insta Page: ",followers)
            following = self.driver.find_element(by=By.XPATH, value ='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button').text
            print("Total Following by Guvi Insta Page: ",following)
        except Exception as error:
            print("extract error on: ",error)
        finally:
            self.driver.quit()

url ="https://www.instagram.com/guviofficial/"
ex_ins = Insta(url)
ex_ins.follower_following()





        
