import os
from MailDeets import MailDeets
from parser import teamsparser
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

details = MailDeets()
teamsname = details.teamsid
teamspwd = details.teamspwd

# regnums = teamsparser('../data/data-vtop')

def get_emails(regnums):
    NET_DELAY = 20
    PATH = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(PATH)

    driver.get('https://teams.microsoft.com/')
    WebDriverWait(driver, 30)

    email_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.NAME, "loginfmt")
    ))
    email_box.send_keys(teamsname)
    email_box.send_keys(Keys.RETURN)

    pswd_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.NAME, "passwd")
    ))
    pswd_box.send_keys(teamspwd)
    time.sleep(NET_DELAY)

    chat_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.ID, "app-bar-86fcd49b-61a2-4701-b771-54728cd291fb")
    ))
    chat_button.click()

############################################
    try:
        who_chat = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-tid='chat-list-entry-with-Who']")
        ))
        who_chat.click()

        emails = []
        for regnum in regnums:
            searchbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@data-tid='ckeditor-newP2PMessage']")
            ))
            searchbox.send_keys(f'Who is {regnum}')
            searchbox.send_keys(Keys.RETURN)
            time.sleep(2)

            manager_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@title='Manager']")
            ))
            manager_button.click()

            sent_msgs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(text(),'Who is the manager')]")
            ))
            time.sleep(2)

            messages = []
            for msgdiv in sent_msgs:
                messages.append(msgdiv.text)
            msg = messages[-1]

            rex = '([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
            email = re.findall(rex, msg)
            emails.append(email[0])
            time.sleep(1)

        return emails

    except TimeoutError:
        print("Increase your NET_DELAY")

    finally:
        driver.quit()


if __name__ == '__main__':
    regnums = ['19BEE0208', '19BEE0221', '19BEE0228']
    mails = get_emails(regnums)
    print(mails)