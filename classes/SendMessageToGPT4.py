from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

id = {
    'send_message-area': 'prompt-textarea',
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

        message_area = self.wait.until(EC.element_to_be_clickable((By.ID, id['send_message-area'])))
        message_area.send_keys(message)

        parent = message_area.find_element(By.XPATH, '..')

        btn = parent.find_element(By.TAG_NAME, 'button')
        btn.click()

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





