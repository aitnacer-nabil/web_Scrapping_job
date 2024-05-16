import time
import psycopg2
import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup


def mlb_scrapper():
    print("------------------------Start Scrapping MLB Sport-----------------------")

    print("Start Scraping")
    chromedriver_autoinstaller.install()
    print("Chrome driver installed")

    # # Establish connection to PostgreSQL database
    # conn = psycopg2.connect(
    #     dbname="scrap",
    #     user="postgres",
    #     password="newlife@22",
    #     host="localhost",
    #     port="5432"
    # )
    # cursor = conn.cursor()
    #
    # # Create table if not exists
    # cursor.execute('''CREATE TABLE IF NOT EXISTS articles
    #                   (id SERIAL PRIMARY KEY,
    #                   title TEXT, description TEXT, url TEXT,
    #                   author TEXT, twitter_handle TEXT,
    #                   import_time TEXT, media_image TEXT)''')
    # conn.commit()

    URL = "https://www.mlb.com/news"
    chrome_options = webdriver.ChromeOptions()
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

    # Extracting all articles
    articles = soup.find_all('article', class_='l-grid__content--card')

    # Loop through each article
    for article in articles:
        # Extracting title
        title_element = article.find('h1', class_='article-item__headline')
        title = title_element.text.strip() if title_element else "Title not found"

        # # Check if title already exists
        # cursor.execute("SELECT * FROM articles WHERE title = %s", (title,))
        # existing_article = cursor.fetchone()
        #
        # if existing_article:
        #     print(f"Article with title '{title}' already exists. Skipping...")
        #     continue

        # Extracting description
        description_element = article.find('div', class_='article-item__preview')
        description = description_element.text.strip() if description_element else "Description not found"

        # Extracting URL
        url = article.find('a')['href'] if article.find('a') else "URL not found"

        # Extracting author information
        author_info = article.find('div', class_='article-item__contributor-container')
        author_name = author_info.find('span', class_='article-item__contributor-byline').text.strip() if author_info else "Author not found"
        author_twitter = author_info.find('span', class_='article-item__contributor-twitter').text.strip() if author_info else "Twitter Handle not found"

        # Extracting import time
        import_time_element = article.find('div', class_='article-item__contributor-date')
        import_time = import_time_element.text.strip() if import_time_element else "Import time not found"

        # Extracting media information
        media_container = article.find('div', class_='article-item__media-container')
        media_image = media_container.find('img')['data-srcset'] if media_container.find('img') else "Media Image not found"

        # # Insert data into database
        # cursor.execute("INSERT INTO articles (title, description, url, author, twitter_handle, import_time, media_image) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        #                (title, description, url, author_name, author_twitter, import_time, media_image))
        # conn.commit()

        # Print results
        print("Title:", title)
        print("Description:", description)
        print("URL:", url)
        print("Author:", author_name)
        print("Twitter Handle:", author_twitter)
        print("Import Time:", import_time)
        print("Media Image:", media_image)
        print()

    print("End Scraping")

    # Close the connection to the database
    # conn.close()
    time.sleep(15)
