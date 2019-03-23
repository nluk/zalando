from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePageObject

class ZalandoPage(BasePageObject):

    url = "https://www.zalando.pl/zalando-newsletter?c_ref=footer_subscription"

    #Locators

    newsletter_email_loc = (By.ID,"lp_email")
    newsletter_sign_up_female_loc = (By.XPATH,"//input[@name='subscribeFemale']")

    def __init__(self,driver):
        BasePageObject.__init__(self,driver)
        self.load(ZalandoPage.url,'ZalandoWindow')
        self.window_handle = self.driver.current_window_handle
        self.inp_email = self.find_element_by(ZalandoPage.newsletter_email_loc)
        self.btn_sign_up_female = self.find_element_by(ZalandoPage.newsletter_sign_up_female_loc)
    
    def subscribe_to_newsletter(self,email):
        print('Signing up for newsletter')
        self.inp_email.send_keys(email)
        self.btn_sign_up_female.click()
        self.driver.close()

    

