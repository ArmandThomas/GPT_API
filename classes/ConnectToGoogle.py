from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

env_vars = dotenv_values('.env')
password = env_vars['PASSWORD']
email = env_vars['EMAIL']

x_path = {
    'btn' : '/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[1]/div/div/button',
    'email': '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input',
    'password': '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input',
    'btn-next': '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button',
    'gpt-login-btn': '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]',
    'gtp-google-btn': '/html/body/div/main/section/div/div/div/div[4]/form[2]/button',
}

class ConnectToGoogle():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.email = email
        self.password = password
        self.gpt_to_google()

    def gpt_to_google(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['gpt-login-btn'])))
        self.driver.find_element(By.XPATH, x_path['gpt-login-btn']).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['gtp-google-btn'])))
        self.driver.find_element(By.XPATH, x_path['gtp-google-btn']).click()

    def send_email(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['email'])))
        self.driver.find_element(By.XPATH, x_path['email']).send_keys(self.email)

    def send_password(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['password'])))
        self.driver.find_element(By.XPATH, x_path['password']).send_keys(self.password)


    def login(self):
        self.send_email()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['btn-next'])))
        self.driver.find_element(By.XPATH, x_path['btn-next']).click()
        self.send_password()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['btn-next'])))
        self.driver.find_element(By.XPATH, x_path['btn-next']).click()