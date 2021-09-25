from selenium import webdriver

# Create the web driver to work with chrome
chrome_driver_path = "C:/Users/divxd/Development/chromedriver.exe"
gecko_driver_path = "C:/Users/divxd/Development/geckodriver.exe"
driver = webdriver.Firefox(executable_path=gecko_driver_path)

# Open the browser and the site specified
# driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS")
driver.get("https://www.python.org")

# Finding elements by ID
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# Finding Elements by name
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# Finding elements by css selector
# docs_link = driver.find_element_by_css_selector(css_selector=".documentation-widget a")
# print(docs_link.text)

# Finding elements by XPath
# tutorial_link = driver.find_element_by_xpath(xpath="/html/body/div/div[3]/div/section/div[1]/div[1]/p[2]/a")
# print(tutorial_link.get_attribute("href"))

# Find elements in python.org for upcoming events and make a dictionary from it
event_times = driver.find_elements_by_css_selector(css_selector=".event-widget li time")
event_links = driver.find_elements_by_css_selector(css_selector=".event-widget li a")
events = {x: {"time": event_times[x].text, "name": event_links[x].text} for x in range(len(event_links))}
print(events)

# Closes the current tab
# driver.close()

# Quits the browser
driver.quit()
