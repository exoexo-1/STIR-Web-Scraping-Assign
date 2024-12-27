#includes everything like proxy rotating ip address date time and what's happening titles of that date from twitter logged in by my own username and password

# the only problem with this project is twitter is not taking these non-premium prxoies in 

from selenium import webdriver  # Import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import uuid
import random
from pymongo import MongoClient
from flask import Flask, render_template
import requests  # Import requests to get your own IP address

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client['twitter_trends']
collection = db['trends']

# Webshare proxy credentials (Multiple Proxies)
webshare_proxies = [
    "lakshyaa-rotate:abcddcba@p.webshare.io:80",
    "lakshyaa-rotate:abcddcba@p.webshare.io:80"
]

# Function to rotate proxies
def get_random_proxy():
    return random.choice(webshare_proxies)

# Function to fetch your own IP address
def get_own_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json().get("ip")
    except Exception as e:
        print(f"Error fetching own IP: {e}")
        return "N/A"

# Function to configure and fetch trends using Selenium
def fetch_trends():
    proxy = get_random_proxy()  # Rotate proxy
    # Specify the path to the Edge driver
    service = Service("C:\\Users\\LAKSHYA\\Downloads\\edgedriver_win64\\msedgedriver.exe")
    options = Options()
    options.add_argument("--headless")
    
    # Set the proxy in the options
    options.add_argument(f'--proxy-server=http://{proxy}')

    trends = []
    ip_address = proxy.split("@")[1]  # Default to proxy IP
    try:
        driver = webdriver.Edge(service=service, options=options)
        
        # Navigate to Twitter login
        driver.get("https://x.com/i/flow/login?lang=en")

        # Wait for the username field to load
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
        username = driver.find_element(By.NAME, "text")
        username.send_keys("Lakshya__88")
        driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

        # Optional: Handle email step
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "text")))
            email = driver.find_element(By.NAME, "text")
            email.send_keys("Lakshyagrawal007@gmail.com")
            driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
        except Exception:
            pass

        # Wait for password field and log in
        password="your_password" # i have changed it due to privacy reasons
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        password = driver.find_element(By.NAME, "password")
        password.send_keys(password)
        driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]").click()

        # Wait for the trends section to load
        WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-testid, 'trend')]")))

        # Scrape trends
        trends_elements = driver.find_elements(By.XPATH, "//div[contains(@data-testid, 'trend')]//span[contains(@class,'r-18u37iz')]")
        trends = [trend.text for trend in trends_elements[:4]]  # Fetch top 4 trends as now twitter home page shows max what's happening titles

    except Exception as e:
        print(f"Proxy Error: {e}")
        # If proxy fails, try without proxy
        print("Trying to fetch trends without proxy...")
        try:
            # Reset options to not use a proxy
            options = Options()
            driver = webdriver.Edge(service=service, options=options)

            # Navigate to Twitter login
            driver.get("https://x.com/i/flow/login?lang=en")

            # Wait for the username field to load
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
            username = driver.find_element(By.NAME, "text")
            username.send_keys("Lakshya__88")
            driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

            # Optional: Handle email step
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "text")))
                email = driver.find_element(By.NAME, "text")
                email.send_keys("Lakshyagrawal007@gmail.com")
                driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
            except Exception:
                pass

            # Wait for password field and log in
            password="your_password" # i have changed it due to privacy reasons
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
            password = driver.find_element(By.NAME, "password")
            password.send_keys(password)
            driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]").click()

            # Wait for the trends section to load
            WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-testid, 'trend')]")))

            # Scrape trends
            trends_elements = driver.find_elements(By.XPATH, "//div[contains(@data-testid, 'trend')]//span[contains(@class,'r-18u37iz')]")
            trends = [trend.text for trend in trends_elements[:4]]  # Fetch top 4 trends
            ip_address = get_own_ip()  # Get actual IP address

        except Exception as e:
            print(f"Error without proxy: {e}")
            ip_address = get_own_ip()  # Ensure we get the IP even if there's an error

    finally:
        driver.quit()

    # Metadata and MongoDB storage
    unique_id = str(uuid.uuid4())
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = {
        "unique_id": unique_id,
        "trends": trends,
        "end_time": end_time,
        "ip_address": ip_address
    }
    collection.insert_one(record)
    return trends, end_time, ip_address

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-trends', methods=['GET'])
def fetch_trends_button():
    trends, end_time, ip_address = fetch_trends()
    return render_template('index.html', trends=trends, time=end_time, ip_address=ip_address)

if __name__ == "__main__":
    app.run(debug=True)