import time

import chromedriver_autoinstaller
import requests
from bs4 import BeautifulSoup
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

print("Start Scrapping")
chromedriver_autoinstaller.install()
print("Chrome driver installed")

URL = "https://ma.indeed.com/jobs?q=&l=Maroc&sort=date"
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in the background
# chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
# chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

chrome_options.add_experimental_option('detach',True)

print("Headless mode activated")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
print("Page opened")
time.sleep(5)
# Get page source
html = driver.page_source
print("Page source retrieved")
# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, "html.parser")
elements = soup.find_all('li', class_='css-5lfssm')
for element in elements:
    title_element = element.select_one('h2.jobTitle')
    if title_element is not None:
        title_span_element = title_element.find('span')
        if title_span_element is not None:
            title = title_span_element.text
            print(title)
        else:
            print("No 'span' found in this 'h2' element")
    else:
        print("No 'h2' with class 'jobTitle' found in this element")
print("End Scrapping")
time.sleep(15)






























