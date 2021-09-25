from selenium import webdriver

gecko_driver = "C:/Users/divxd/Development/geckodriver.exe"
driver = webdriver.Firefox(executable_path=gecko_driver)

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name(name="fName")
first_name.send_keys("MyFirstName")

last_name = driver.find_element_by_name(name="lName")
last_name.send_keys("MyLastName")

email = driver.find_element_by_name(name="email")
email.send_keys("myEmail@email.dmn")

submit_button = driver.find_element_by_css_selector(css_selector=".btn-primary")
submit_button.click()