from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import yaml


def login(dr, url, usernameId, username, passwordId, password, submit_buttonId):
    dr.get(url)
    sleep(5)
    dr.find_element(by=By.ID, value=usernameId).send_keys(username)
    dr.find_element(by=By.ID, value=passwordId).send_keys(password)
    dr.find_element(by=By.CLASS_NAME, value=submit_buttonId).click()


def open_test_group(dr, url, informatica, group):
    dr.get(url + "/teacher/journal")
    sleep(10)
    dr.find_element(by=By.CLASS_NAME, value=informatica).click()
    dr.find_element(by=By.CLASS_NAME, value=group).click()


with open('loginDetails.yml', 'rb') as f:
    conf = yaml.load(f, Loader=yaml.SafeLoader)

myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']
main_url = "https://ege.sdamgia.ru"
service = Service(r"./chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

login(driver, main_url, "email", myFbEmail, "current-password", myFbPassword,
      "Button.Button_view_default.ProfileAuth-Button")
sleep(5)
open_test_group(driver, main_url, "PortalList-SubjectName", "PortalList-Group")

