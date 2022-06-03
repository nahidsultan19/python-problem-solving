from selenium import webdriver

PATH="C:\Program Files (x86)\chromedirve.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")