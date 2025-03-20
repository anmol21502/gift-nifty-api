from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

MONEYCNTL_URL = "https://www.moneycontrol.com/markets/global-indices/"

def fetch_gift_nifty():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(MONEYCNTL_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Locate Gift NIFTY data
    nifty_section = soup.find("div", class_="gIwnfA")  # Adjust this class based on Moneycontrol's structure
    if nifty_section:
        change = nifty_section.find("span", class_="chg").text.strip()
        return {"change": change}
    
    return {"change": "N/A"}

@app.route('/gift-nifty', methods=['GET'])
def get_gift_nifty():
    data = fetch_gift_nifty()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
