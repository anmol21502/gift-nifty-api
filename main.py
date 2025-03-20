from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time

app = Flask(__name__)

URL = "https://www.moneycontrol.com/markets/global-indices/"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_market_data():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Specify Chrome and ChromeDriver paths for Render
    options.binary_location = "/usr/bin/google-chrome"
    driver_service = Service("/usr/local/bin/chromedriver")

    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.get(URL)

    try:
        wait = WebDriverWait(driver, 10)

        # Find the row containing "GIFT NIFTY"
        row_xpath = "//tr[td//a[@title='GIFT NIFTY']]"
        row_element = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        if row_element:
            # Extract the second <td> inside that row
            value_xpath = f"{row_xpath}/td[3]"
            value_element = driver.find_element(By.XPATH, value_xpath)
            market_value = value_element.text.strip()
        else:
            market_value = "N/A"

    except Exception as e:
        market_value = f"Error: {str(e)}"

    driver.quit()
    return {"change": market_value}

@app.route('/gift-nifty', methods=['GET'])
def get_gift_nifty():
    return jsonify(fetch_market_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
