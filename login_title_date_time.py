# *login+date+time+fething_data*
# doesn't include proxy and ip address part yet
# stir_project.py is the main file

from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import uuid
import socket
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client['twitter_trends']
collection = db['trends']

# Function to run the Selenium query
def fetch_trends():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")  # Run the browser in headless mode

    driver = webdriver.Chrome(service=service, options=options)
    trends = []

    try:
        # Navigate to Twitter login
        driver.get("https://x.com/i/flow/login?lang=en")

        # Login Process
        sleep(3)
        username = driver.find_element(By.XPATH, "//input[@name='text']")
        username.send_keys("Lakshya__88")
        driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

        sleep(3)
        try:
            email = driver.find_element(By.XPATH, "//input[@name='text']")
            email.send_keys("Lakshyagrawal007@gmail.com")
            driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
        except Exception:
            print("Email input not required.")

        sleep(3)
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("Your_password") # i have changed it due to privacy reasons
        driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]").click()

        # Wait for the page to load fully
        WebDriverWait(driver, 25).until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@data-testid, 'trend')]//span")))

        sleep(7)
        # Fetch the trending topics after ensuring the page is fully loaded
        trends_elements = driver.find_elements(By.XPATH, "//div[contains(@data-testid, 'trend')]//span[contains(@class,'r-18u37iz')]")
        for trend in trends_elements[:4]:  # Limit to top 4 trends
            trends.append(trend.text)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

    # Capture metadata
    unique_id = str(uuid.uuid4())  # Generate a unique ID
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp
    ip_address = socket.gethostbyname(socket.gethostname())  # Fetch system IP

    # Store data in MongoDB
    record = {
        "unique_id": unique_id,
        "trend1": trends[0] if len(trends) > 0 else None,
        "trend2": trends[1] if len(trends) > 1 else None,
        "trend3": trends[2] if len(trends) > 2 else None,
        "trend4": trends[3] if len(trends) > 3 else None,
        "trend5": trends[4] if len(trends) > 4 else None,
        "end_time": end_time,
        "ip_address": ip_address
    }
    collection.insert_one(record)  # Insert into MongoDB
    return trends, end_time, ip_address

# Flask route to serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to trigger the query and return the trends
@app.route('/fetch-trends', methods=['GET'])
def fetch_trends_button():
    trends, end_time, ip_address = fetch_trends()
    return render_template('index.html', trends=trends, time=end_time, ip_address=ip_address)

if __name__ == "__main__":
    app.run(debug=True)
