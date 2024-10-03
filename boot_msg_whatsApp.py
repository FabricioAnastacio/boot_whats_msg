import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import time


print('Qual o caminho do curriculo? Esteja no fornato: D:\exemple\exmple\currículo.pdf')
curriculun_path = input()

navegation = webdriver.Chrome()
navegation.get('https://web.whatsapp.com/')
Keyboard = Controller()

button_send = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div/p'
button_more = '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]/div/div/div/span'
button_document = '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li'
button_send_curriculum = '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div'


def send():
    try:
        navegation.find_element("xpath", button_send).send_keys(Keys.ENTER)
        return False
    except:
        return True


def click_document():
    try:
        navegation.find_element("xpath", button_document).click()
        return False
    except:
        return True


def upload_curriculum():
    Keyboard.type(curriculun_path)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)


def send_curriculum():
    try:
        navegation.find_element("xpath", button_send_curriculum).click()
        return False
    except:
        return True


def play_in_boot(contacts_df, text):
    while len(navegation.find_elements("id", "side")) < 1:
        time.sleep(1)

    for i, number in enumerate(contacts_df['Número']):
        link = f"https://web.whatsapp.com/send?phone={number}&text={text}"
        navegation.get(link)

        while send():
            time.sleep(1)

        navegation.find_element("xpath", button_more).click()

        while click_document():
            time.sleep(1)

        time.sleep(1)
        upload_curriculum()

        while send_curriculum():
            time.sleep(1)
        time.sleep(5)


if __name__ == '__main__':
    red_excel = pd.read_excel('Enviar.xlsx')
    text_msg = open('Msg.txt', 'r').read()
    play_in_boot(red_excel, text_msg)
