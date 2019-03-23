from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from base_page import BasePageObject


class TempMailPage(BasePageObject):

    url = "https://temp-mail.org/en/"

    #Locators

    delete_address_loc = (By.ID,"click-to-delete")
    refresh_emails_loc = (By.ID,"click-to-refresh")
    email_subjects_loc = (By.XPATH,"//table[@id='mails']/tbody/tr/td")
    page_description_loc = (By.XPATH,"//div[@class='inboxSeoBl']")
    email_body_loc = (By.XPATH,"//div[@class='pm-text']/div[1]/div[1]")
    email_body_links_loc = (By.XPATH,"//div[@class='pm-text']/div[1]/div[1]/a")
    email_address_loc = (By.ID,"mail")
    newsletter_confirm_link = (By.XPATH,"//a[contains(@href,'confirm')]")
    discount_code_loc = (By.XPATH,"//td[contains(text(),'kod rabatowy')]/span")



    def __init__(self,driver):
        BasePageObject.__init__(self,driver)
        self.load(TempMailPage.url,'TempMailPage')
        self.window_handle = self.driver.current_window_handle
        self.btn_delete_address = self.find_element_by(TempMailPage.delete_address_loc)
        self.btn_refresh_emails = self.find_element_by(TempMailPage.refresh_emails_loc)
        self.inp_current_email = self.find_element_by(TempMailPage.email_address_loc)
        

    def refresh_emails(self):
        try:
            self.btn_refresh_emails.click()
        except StaleElementReferenceException:
            self.btn_refresh_emails = self.find_element_by(TempMailPage.refresh_emails_loc)
            self.btn_refresh_emails.click()

    def new_address(self):
        print('Preparing new email address:')
        current_email_value = self.inp_current_email.get_attribute('value')
        self.btn_delete_address.click()
        new_email = self.refresh_element_for_attribute(TempMailPage.email_address_loc,('value',current_email_value)).get_attribute('value')
        print(new_email)
        return new_email
    
    def get_email_subjects(self):
        self.refresh_emails()
        self.scroll_to(self.find_element_by(TempMailPage.page_description_loc))
        return self.find_elements_by(TempMailPage.email_subjects_loc)
    
    def confirm_newsletter(self):
        self.get_focus()
        print('Searching for newsletter confirmation email')
        self.find_email('Potwierd')
        confirmation_url = self.find_element_by(TempMailPage.newsletter_confirm_link).get_attribute("href")
        self.load(confirmation_url,'ConfirmationWindow')
        self.driver.close()
        print('Newsletter confirmed')
    
    def get_discount_code(self):
        self.get_focus()
        print('Searching for email with discount code')
        self.find_email('10%')
        print('Discount code found:')
        discount_code = self.find_element_by(TempMailPage.discount_code_loc).text
        print(discount_code)
        return discount_code

  
    def find_email(self,keyword):
        email_found = False
        while not email_found:
            for subject_element in self.get_email_subjects():
                if keyword in subject_element.text:
                    self.scroll_to(self.find_element_by(TempMailPage.page_description_loc))
                    subject_element.click()
                    email_found = True
                    break


