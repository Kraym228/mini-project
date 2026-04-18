from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
#Явное ожидание


#Сам драйвер
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10 , poll_frequency=1)
        
   
    def open(self):
        with allure.step(f'Opening page {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)
        
    def is_opened(self):
        with allure.step(f'Opening {self.PAGE_URL} is opened'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
        
        
    def make_screenshot(self,screen_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screen_name,
            attachment_type=AttachmentType.PNG
        )
        
    