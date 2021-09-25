from selenium import webdriver
import time

gecko_driver = "C:/Users/divxd/Development/geckodriver.exe"
driver = webdriver.Firefox(executable_path=gecko_driver)

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Get to the cookie
cookie = driver.find_element_by_id(id_="cookie")

# Set the timers
current_time = time.time()
timeout = current_time + 5
five_min = current_time + 300

while True:
    cookie.click()

    # Timeout happens, i.e. after 5 seconds. Check store now.
    if time.time() > timeout:
        # Build the store first
        # store = [driver.find_element_by_id(id_="buyCursor"),
        #          driver.find_element_by_id(id_="buyGrandma"),
        #          driver.find_element_by_id(id_="buyFactory"),
        #          driver.find_element_by_id(id_="buyMine"),
        #          driver.find_element_by_id(id_="buyShipment"),
        #          driver.find_element_by_id(id_="buyAlchemy lab"),
        #          driver.find_element_by_id(id_="buyPortal"),
        #          driver.find_element_by_id(id_="buyTime machine")]
        store = driver.find_elements_by_css_selector(css_selector="#store>div")
        for item_index in range(len(store) - 1, -1, -1):
            if store[item_index].get_attribute(name="class") == "":
                print(f"Store item {store[item_index].find_element_by_tag_name('b').text} is available. Buying")
                store[item_index].click()
                print("Resetting timeout")
                timeout = time.time() + 5
                break
    if time.time() > five_min:
        print("Five minutes up.")
        break

cps = driver.find_element_by_id(id_="cps").text
print(f"Final score = {cps} cookie/second")
