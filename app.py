from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep



class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
     



    def teste(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        ##driver = webdriver.Remote(options=chrome_options)

        hashtag = "gatos"

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.instagram.com')
        sleep(3)
        user_element = driver.find_element(By.XPATH, "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element(By.XPATH, "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        sleep(5)
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        sleep(5)
        for i in range(1, 1):
            print(i)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hrefs = driver.find_elements(By.TAG_NAME, "a")
        pic_harefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_harefs if hashtag in href]

        for pic_href in pic_harefs:
            print(pic_href)
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try: 
                hrefs1 = driver.find_element(By.CLASS_NAME, "fr66n").click()
                print("Realizou a curtida" + str(hrefs1))
                sleep(19)
            except Exception as e:
                print("Erro" + str(e))
              

           
            

 
        

teste = InstagramBot('','')
teste.teste()