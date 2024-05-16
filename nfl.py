import time

import chromedriver_autoinstaller
import requests
from bs4 import BeautifulSoup
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def nfl_scrapper():
    print("------------------------Start Scrapping NFL Sport-----------------------")
    chromedriver_autoinstaller.install()
    print("Chrome driver installed")

    URL = "https://www.nfl.com/news/all-news"
    BASE_URL = "https://www.nfl.com"
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in the background
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')



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
    # Find the 'section' element
    sections = soup.find_all('section', class_='d3-l-module--lifestyle')
    time.sleep(5)
    for section in sections:
        # Find all 'div' elements within the 'section'
        divs = section.find_all('div', class_='d3-l-col__col-12')
        # For each 'div', find the 'h3' element with the class 'd3-o-media-object__title'
        for div in divs:
            a_tag = div.find('a', href=True)
            if a_tag is not None:
                href = a_tag['href']
                print(f"Link: {BASE_URL}{href}")

            h3 = div.find('h3', class_='d3-o-media-object__title')
            if h3 is not None:
                print(f"Title: {h3.text.strip()}")

            p_date = div.find('p', class_='d3-o-media-object__date')
            if p_date is not None:
                print(f"Date: {p_date.text.strip()}")

            div_summary = div.find('div', class_='d3-o-media-object__summary')
            if div_summary is not None:
                print(f"Summary: {div_summary.text.strip()}")

            picture = div.find('picture')
            if picture is not None:
                source = picture.find('source')
                if source is not None:
                    # img_src = source['srcset'].split(",")[0].split(" ")[0]  # Get the first URL from srcset
                    print(f"Image Source: {type(source)}")

            break
        break
    print("End Scrapping")
    time.sleep(15)
