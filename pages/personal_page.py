from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import Keys

class PersonalPage(BasePage):
    
    PAGE_URL = Links.PERSONAL_PAGE
    
    FIRST_NAME_FIELD = ('xpath' , "//input[@name='firstName']")
    SAVE_BUTTON = ('xpath', "(//button[@type='submit'])[1]")
    LOADER = ('class name', "oxd-form-loader")
    
    SUCCESS_TOAST = ('xpath', "//div[contains(@class, 'oxd-toast--success')]")
    

    def change_name(self,new_name):
        with allure.step(f'Change name on "{new_name}"'):
            first_name_field =  self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + 'a')
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name
        
    @allure.step('Save changes')    
    def save_changes(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        
        
    @allure.step('Changes has been saves successfully')
    def is_changes_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))