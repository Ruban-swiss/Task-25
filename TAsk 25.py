from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # added keys module
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Task25:
    
    def __init__(self, url= "https://www.imdb.com/search/name/" ):
       self.url = url
       self.driver = webdriver.Chrome()
       self.action = ActionChains(self.driver) # added action chain - it performs keyboard actions
       self.wait = WebDriverWait(self.driver, 10) # added explicit wait
    

    def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10) # added implicit wait
       for _ in range(9): # used "for loop" to click "page down key" in keyboard, multiple times (To make name and birthdate textbox visible)
            self.action.send_keys(Keys.DOWN).perform()
       
        
    def search_name(self):
        # Name
        xpath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[1]/label/span[1]/div"
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        xpath1 = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input"
        self.wait.until( EC.presence_of_element_located( (By.XPATH, xpath1) ) ).send_keys("Ruban")

        for _ in range(9): # used "for loop" to click "page down key" in keyboard, multiple times (To make name and birthdate textbox visible)
            self.action.send_keys(Keys.DOWN).perform()
        
        # Birthdate
        xpath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[3]/div[1]/label/span[1]/div"
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        xpath1 = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[3]/div[2]/div/div/div/div/div/div/input"
        self.wait.until( EC.presence_of_element_located( (By.XPATH, xpath1) ) ).send_keys("13-03-1979")

        # Search
        xpath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button/span"
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        
        expected_url = "https://www.imdb.com/search/name/?name=Ruban"
        assert expected_url == self.driver.current_url # confirming whether url changed or not

    def quit(self):
        self.driver.quit()
         
obj = Task25()
obj.boot()
obj.search_name()
obj.quit()

        