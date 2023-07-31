import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def uploadBot(simp_path):
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--log-level=3")
    # options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\Google\\Chrome Beta\\User Data\\")
    # options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
    options.add_argument('--disable-blink-features=AutomationControlled')
    userdatadir = 'C:/Users/rajha/AppData/Local/Google/Chrome/User Data'
    options.add_argument(f"--user-data-dir={userdatadir}")

    bot = webdriver.Chrome(options=options)
    try:
        bot.get("https://studio.youtube.com")
        time.sleep(5)
        upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()
        time.sleep(1)

        file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
        #simp_path = 'tempVid/ftp.zip.mp4'
        abs_path = os.path.abspath(simp_path)
        file_input.send_keys(abs_path)
        time.sleep(4)
        time.sleep(7)
        link = bot.find_element(By.XPATH, '//*[@id="details"]/ytcp-video-metadata-editor-sidepanel/ytcp-video-info/div/div[2]/div[1]/div[2]/span/a')
        print(link.get_attribute("href"))
        next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
            time.sleep(1)

        done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
        done_button.click()
        time.sleep(5)
        bot.quit()
        flink=link.get_attribute('href')
        return flink
    except:
        pass