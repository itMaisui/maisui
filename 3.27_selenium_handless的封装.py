# handless的封装
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('_headless')
    # driver = webdriver.Chrome(Options=chrome_options)
    chrome_options.add_argument('--disable-gpu')
    path = 'C:\Program Files\Google\Chrome\Application/chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

