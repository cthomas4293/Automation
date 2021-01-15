from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')


input_text = chrome_browser.find_element_by_id('user-message')
input_text.clear()
input_text.send_keys('I AM EXTRA COOOOOLLL')

close_ad = chrome_browser.find_element_by_id('at-cv-lightbox-close')

close_ad.click()

show_message_button.click()

displayed_message_element = chrome_browser.find_element_by_id('display')

displayed_message = displayed_message_element.get_attribute('innerHTML')
print(displayed_message)

