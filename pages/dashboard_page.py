from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure 

class DashboardPage(BasePage):
    
    PAGE_URL = Links.DASHBOARD_PAGE
 
    MY_INFO_BUTTON = ('xpath' , "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[6]")
    
    LOADER = ('xpath', "//div[@class='oxd-form-loader']")
    
    @allure.step('Click My Info link')
    def click_my_info_link(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()