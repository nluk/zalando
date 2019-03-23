from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from expected_conditions_attribute import element_attribute_changed 

class BasePageObject:
    
    def __init__(self,webdriver):
        self.driver = webdriver
        self.window_handle = None

    def find_element_by(self,locator):
        wait = WebDriverWait(self.driver,100)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements_by(self,multiple_locator):
        wait = WebDriverWait(self.driver,100)
        try:
            elements = wait.until(EC.visibility_of_all_elements_located(multiple_locator))
        except TimeoutError:
            print("Elements not found - attempting once more")
        return elements


    def refresh_element_for_attribute(self,locator,attribute_details):
        wait = WebDriverWait(self.driver,10)
        return wait.until(element_attribute_changed(locator,*attribute_details))

    def get_focus(self):
        self.driver.switch_to_window(self.window_handle)
    
    def load(self,url,name):
        new_window_script = "window.open('about:blank', '{0}');".format(name)
        self.driver.execute_script(new_window_script)
        self.driver.switch_to.window(name)
        self.driver.get(url)
    
    def scroll_to(self,element_to_display):
        action = ActionChains(self.driver)
        action.move_to_element(element_to_display).perform()

  

