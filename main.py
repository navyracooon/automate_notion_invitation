from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = ""  # ここにNotionのURL
SETTING_BUTTON_SELECTOR = "#notion-app > div > div:nth-child(1) > div > nav > div > div > div > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(3) > div > div:nth-child(2)"
ADD_MEMBERS_BUTTON_SELECTOR = "#notion-app > div > div.notion-overlay-container.notion-default-overlay-container > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div.hide-scrollbar > div:nth-child(4) > div > div:nth-child(2) > div > div > div:nth-child(1)"
INPUT_EMAIL_FORM_SELECTOR = "#notion-app > div > div.notion-overlay-container.notion-default-overlay-container > div:nth-child(3) > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div:nth-child(1) > div > input[type=email]"
INVITE_BUTTON_SELECTOR = "#notion-app > div > div.notion-overlay-container.notion-default-overlay-container > div:nth-child(3) > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div:nth-child(2)"


member_list = []  # ここにメアドのリスト.


class AutomateNotionInvitation:
    @staticmethod
    def wait_and_click(driver, selector):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        button = driver.find_element(By.CSS_SELECTOR, selector)
        button.click()

    @staticmethod
    def wait_and_send(driver, selector, message):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        form = driver.find_element(By.CSS_SELECTOR, selector)
        form.send_keys(message)

    @staticmethod
    def run():
        driver = webdriver.Chrome()
        driver.get(url)
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, SETTING_BUTTON_SELECTOR)))

        AutomateNotionInvitation.wait_and_click(driver, SETTING_BUTTON_SELECTOR)

        for member in member_list:
            AutomateNotionInvitation.wait_and_click(driver, ADD_MEMBERS_BUTTON_SELECTOR)
            AutomateNotionInvitation.wait_and_send(driver, INPUT_EMAIL_FORM_SELECTOR, member)
            AutomateNotionInvitation.wait_and_click(driver, INVITE_BUTTON_SELECTOR)
            sleep(3)


if __name__ == "__main__":
    AutomateNotionInvitation.run()
    print("Finished")
