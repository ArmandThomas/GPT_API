from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

x_path = {
    'send_message-area': '/html/body/div[1]/div/div[2]/div[1]/div[2]/main/div[2]/div[2]/form/div/div[2]/div/textarea',
    'send_message-btn': '/html/body/div[1]/div/div[2]/div[1]/div[2]/main/div[2]/div[2]/form/div/div[2]/div/button',
    'status_assistant' : '/html/body/div[1]/div[1]/div[2]/div/main/div[3]/form/div/div[1]/div/button',
}
class SendMessageToGPT4:
    def __init__(self, driver, message):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.nbr_message = self.get_nbr_message()
        self.send_message(message)
        self.response = self.get_last_message()

    def get_last_message(self):
        content = self.driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        last_message = soup.find_all('div', attrs={'data-message-author-role': 'assistant'})[-1]
        is_streaming = True if 'result-streaming' in last_message.find('div').get('class') else False
        if is_streaming:
            return ''
        return last_message.text if last_message else ''


    def get_nbr_message(self):
        content = self.driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        nbr_message = soup.find_all('div', attrs={'data-message-author-role': 'assistant'})
        return len(nbr_message) if nbr_message else 0

    def send_message(self, message):

        self.driver.save_screenshot('screenshot.png')

        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['send_message-area'])))
        self.driver.find_element(By.XPATH, x_path['send_message-area']).send_keys(message)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, x_path['send_message-btn'])))
        self.driver.find_element(By.XPATH, x_path['send_message-btn']).click()

        has_replied = False

        while not has_replied:
            nbr_message = self.get_nbr_message()
            if nbr_message > self.nbr_message:
                curr_message = self.get_last_message()
                if curr_message != "":
                    self.response = curr_message.encode('utf-8')
                    has_replied = True
            else:
                time.sleep(1)





