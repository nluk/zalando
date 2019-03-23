from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePageObject

class ZalandoPage(BasePageObject):

    url = "https://www.zalando.pl/zalando-newsletter?c_ref=footer_subscription"

    #Locators

    newsletter_email_loc = (By.XPATH,"//input[@type='email']")
    newsletter_female_radio_loc = (By.XPATH,"//div[input[@value='FEMALE']]/label")
    newsletter_save_button_loc = (By.XPATH,"//button[contains(span,'Zapisz')]")
    newsletter_check_mailbox_loc = (By.XPATH,"//h1[contains(text(),'Sprawdź skrzynkę!')]")
    
    def __init__(self,driver):
        BasePageObject.__init__(self,driver)
        self.load(ZalandoPage.url,'ZalandoWindow')
        self.window_handle = self.driver.current_window_handle
        self.inp_email = self.find_element_by(ZalandoPage.newsletter_email_loc)
        self.rad_female = self.find_element_by(ZalandoPage.newsletter_female_radio_loc)
        self.btn_save = self.find_element_by(ZalandoPage.newsletter_save_button_loc)
    
    def subscribe_to_newsletter(self,email):
        print('Signing up for newsletter')
        self.inp_email.send_keys(email)
        self.rad_female.click()
        self.btn_save.click()
        self.wait_for_element(ZalandoPage.newsletter_check_mailbox_loc,self.default_timeout)
       # self.driver.close()

    

