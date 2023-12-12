from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

env_vars = dotenv_values('.env')
password = env_vars['PASSWORD']
email = env_vars['EMAIL']

x_path = {
    'btn' : '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]',
    'btn-login_with_microsoft': '/html/body/div/main/section/div/div/div/div[4]/form[1]/button',
    'email' : '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]',
    'btn-next': '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input',
    'password': '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input',
    'btn-login' : '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input',
    'btn-stay_signed_in': '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input',
}

class ConnectWithMicrosoft():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.email = email
        self.password = password
        self.gpt_to_microsoft()

    def gpt_to_microsoft(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['btn'])))
        self.driver.find_element(By.XPATH, x_path['btn']).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['btn-login_with_microsoft'])))
        self.driver.find_element(By.XPATH, x_path['btn-login_with_microsoft']).click()

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
        time.sleep(1)
        self.send_password()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['btn-login'])))
        self.driver.find_element(By.XPATH, x_path['btn-login']).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['btn-stay_signed_in'])))
        self.driver.find_element(By.XPATH, x_path['btn-stay_signed_in']).click()

