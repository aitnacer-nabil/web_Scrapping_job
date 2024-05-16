import time
import chromedriver_autoinstaller
import requests
from bs4 import BeautifulSoup
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


#Mysql
# import mysql.connector

def soccerParser():
    #Check Connection to Database
    # mydb = mysql.connector.connect(
    # host="localhost",
    # user="root",
    # password="",
    # database="sport"
    # )
    # mycursor = mydb.cursor()

    # mycursor.execute("CREATE TABLE IF NOT EXISTS news (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255),time VARCHAR(255),category VARCHAR(255) , paragraph TEXT,link TEXT,imglink TEXT)")
    sql = "INSERT INTO news (title, time, category, paragraph, link,imglink) VALUES (%s, %s, %s, %s, %s, %s)"
    print("------------------------Start Scrapping Yahoo Sport-----------------------")
    chromedriver_autoinstaller.install()
    print("Chrome driver installed")

    URL = "https://sports.yahoo.com/soccer/news/"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in the background
    # chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    # chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode
    # chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option('detach', True)

    print("Headless mode activated")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    print("Page opened")
    time.sleep(5)
    # Get page source
    html = driver.page_source
    print("Page source retrieved")
    #Select first row in table to get the first article
    # mycursor.execute("SELECT * FROM news ORDER BY id DESC LIMIT 1")
    # myresult = mycursor.fetchone()
    #print(myresult)
    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all('li', class_='stream-item')
    all_articles = []
    for element in elements:
        #print("---------------Article---------------")
        time_element = element.select_one('time').text
        title_element = element.select_one('h3')
        #print(title_element)
        if title_element is not None:
            title_a_element = title_element.find('a')
            if title_a_element is not None:
                title = title_a_element.text
                #Check if the article is already in the database
                # if myresult is not None:
                #     if title == myresult[1]:
                #         print("End Scrapping")
                #         break
                link = title_a_element['href']
                #print(title+" : "+link)
            else:
                print("No 'a' found in this 'h3' element")
        else:
            print("No 'h3' with class 'Title' found in this element")
        img_link_element = element.find('img')
        if img_link_element is not None:
            img_link = img_link_element['src']
            #print(img_link_element['src'])
        else:
            print("No 'img' found in this element")
        paragraph_element = element.select_one('p')
        if paragraph_element is not None:
            paragraph = paragraph_element.text
            #print(paragraph)
        else:
            print("No 'p' found in this element")
        #save to database
        all_articles.append((title, time_element, "Soccer", paragraph, link, img_link))
        """val=(title,time_element,"Soccer",paragraph,link,img_link)
        mycursor.execute(sql,val)
        mydb.commit()"""
    if len(all_articles) > 0:
        for article in reversed(all_articles):
            print(f"article {article}")
            val = (article[0], article[1], article[2], article[3], article[4], article[5])
            # mycursor.execute(sql,val)
            # mydb.commit()
    print("End Scrapping")
    time.sleep(15)
