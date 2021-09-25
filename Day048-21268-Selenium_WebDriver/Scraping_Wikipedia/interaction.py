from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gecko_driver = "C:/Users/divxd/Development/geckodriver.exe"
driver = webdriver.Firefox(executable_path=gecko_driver)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# Finding the number of articles on wikipedia
article_count = driver.find_element_by_css_selector(css_selector="#articlecount a[title='Special:Statistics']")
# print(article_count.text)

# Clicking on the article count tag
# article_count.click()

# Find elements by the text of a link
all_portals_link = driver.find_element_by_link_text(link_text="All portals")
# all_portals_link.click()

search = driver.find_element_by_name(name="search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

driver.quit()
