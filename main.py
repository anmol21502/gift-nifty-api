from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Moneycontrol URL
URL = "https://www.moneycontrol.com/markets/global-indices/"

# More specific class targeting
TARGET_CLASS_1 = "marketData_web_greentext__D2nTQ"
TARGET_CLASS_2 = "marketData_web_tright__qE8_a"

# Set up Selenium WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36"
)

# Auto-download ChromeDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def fetch_market_data():
    try:
        driver.get(URL)
        logging.info(f"Page Title: {driver.title}")

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        # More specific XPath targeting both class names
        xpath = f"//td[contains(@class, '{TA
