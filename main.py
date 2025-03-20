from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from selenium.webdriver.chrome.service import Service

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = "https://www.moneycontrol.com/markets/global-indices/"

# Set up Selenium WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection

# Set a real User-Agent
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36"
)

# Define the correct ChromeDriver path
service = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

def fetch_market_data():
    try:
        driver.get(URL)
        print(driver.title)

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        # Find the row that contains "GIFT NIFTY"
        row_xpath = "//tr[td//a[@title='GIFT NIFTY']]"
        row_element = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        if row_element:
            # Extract the second <td> inside that row
            value_xpath = f"{row_xpath}/td[3]"
            value_element = driver.find_element(By.XPATH, value_xpath)
            market_value = value_element.text.strip()

            logging.info(f"Extracted Market Value for GIFT NIFTY: {market_value}")
        else:
            logging.warning("Target row not found on the page.")

    except Exception as e:
        logging.error(f"Error fetching the page: {e}")

if _name_ == "_main_":
    try:
        while True:
            fetch_market_data()
            time.sleep(1)  # Poll every second
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    finally:
        driver.quit()  # Ensure browser closes properly
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from selenium.webdriver.chrome.service import Service

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = "https://www.moneycontrol.com/markets/global-indices/"

# Set up Selenium WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection

# Set a real User-Agent
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36"
)

# Define the correct ChromeDriver path
service = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

def fetch_market_data():
    try:
        driver.get(URL)
        print(driver.title)

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        # Find the row that contains "GIFT NIFTY"
        row_xpath = "//tr[td//a[@title='GIFT NIFTY']]"
        row_element = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        if row_element:
            # Extract the second <td> inside that row
            value_xpath = f"{row_xpath}/td[3]"
            value_element = driver.find_element(By.XPATH, value_xpath)
            market_value = value_element.text.strip()

            logging.info(f"Extracted Market Value for GIFT NIFTY: {market_value}")
        else:
            logging.warning("Target row not found on the page.")

    except Exception as e:
        logging.error(f"Error fetching the page: {e}")

if _name_ == "_main_":
    try:
        while True:
            fetch_market_data()
            time.sleep(1)  # Poll every second
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    finally:
        driver.quit()  # Ensure browser closes properly
