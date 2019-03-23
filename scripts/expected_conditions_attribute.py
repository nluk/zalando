class element_attribute_changed(object):
  """An expectation for checking that an element's specified attribute has changed

  locator - used to find the element
  returns the WebElement once it's specified attribute has changed
  """
  def __init__(self, locator, attribute_name, old_attribute_value):
    self.locator = locator
    self.attribute_name = attribute_name
    self.old_attribute_value = old_attribute_value

  def __call__(self, driver):
    element = driver.find_element(*self.locator)  
    if self.old_attribute_value == element.get_attribute(self.attribute_name):
        return False
    else:
        return element