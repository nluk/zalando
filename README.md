# zalando

##### *Unfortunately Zalando discount code delivery time has recently significantly increased. <br> Together with a changed layout, it looks suspiciously like a countermeasure for this little script.*
##### *Update 03/06/2019 - TempMail page has received a significant layout refresh, rendering all mappings obsolete.<br> Project won't be updated anytime soon *

Short project leveraging Selenium browser to generate a discount code for Zalando:
* Creates a temporary email address
* Registers an account on Zalando using that email
* Verifies email
* Extracts discount code from message

### Features
* Page Object Pattern mapping
* Concurrent tabs usage
* Custom page condition - element attribute changed
* Headless configuration without image rendering by default


### Requirements
* Selenium package (via requirements.txt)
* Chrome/Chromium webdriver
* Decent connection
* Python 3.4+

### Run main script to get discount code:
```
python3 get_discount_code.py
```
