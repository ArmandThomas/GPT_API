import undetected_chromedriver as uc
import time
from classes.ConnectToGoogle import ConnectToGoogle
from classes.SendMessageToGPT4 import SendMessageToGPT4
from classes.ConnectWithMicrosoft import ConnectWithMicrosoft
from fastapi import FastAPI
from pydantic import BaseModel
from pyvirtualdisplay import Display
import platform

if platform.system() == 'Linux':
    display = Display(visible=0, size=(1920, 1440))
    display.start()

class BodySendMessage(BaseModel):
    message: str

app = FastAPI()

class Options(uc.ChromeOptions):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.headless = False
        self.add_argument("--no-sandbox")

driver = uc.Chrome(options=Options())

driver.get("https://chat.openai.com/auth/login")

connect_with_microsoft = ConnectWithMicrosoft(driver)
connect_with_microsoft.login()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/send-message")
async def send_message(body: BodySendMessage):
    send_message_to_gpt4 = SendMessageToGPT4(driver, body.message)
    while not send_message_to_gpt4.response:
        time.sleep(1)
    return send_message_to_gpt4.response

