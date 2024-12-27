
#fetching and taking input from twitter webpage


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to Twitter login
driver.get("https://x.com/i/flow/login?lang=en")
listoftrend = []
def script():
    try:
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

        # Wait for the page to load fully (wait for the trends section to be visible)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@data-testid, 'trend')]//span")))

        sleep(20)
        # Fetch the trending topics again after ensuring the page is fully loaded
        trends = driver.find_elements(By.XPATH, "//div[contains(@data-testid, 'trend')]//span[contains(@class,'css-1jxf684')]")
        for trend in trends:
            listoftrend.append(trend.text)

        print(f"Trends found: {listoftrend[:5]}")  # Print the top 5 trends
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sleep(4)
        driver.quit()

script()