from selenium import webdriver
from temp_mail_page import TempMailPage
from zalando_page import ZalandoPage


execution_options = webdriver.ChromeOptions()
execution_options.add_argument("--disable-bundled-ppapi-flash");
execution_options.add_argument('--headless')
execution_options.add_argument('--blink-settings=imagesEnabled=false')
print('Initializing scraper')
driver = webdriver.Chrome(options=execution_options)
print('Opening TempMail')
email_page = TempMailPage(driver)
temporary_email = email_page.new_address()
print('Opening Zalando')
zalando_page = ZalandoPage(driver)
zalando_page.subscribe_to_newsletter(temporary_email)
email_page.confirm_newsletter()
email_page.get_discount_code()
driver.close()