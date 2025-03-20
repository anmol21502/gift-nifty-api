#!/usr/bin/env bash
echo "Updating system and installing dependencies..."
apt-get update && apt-get install -y wget unzip curl

echo "Installing Google Chrome..."
wget -qO- https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > google-chrome.deb
apt install -y ./google-chrome.deb
rm google-chrome.deb

echo "Installing ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
wget -q "https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv chromedriver /usr/local/bin/
rm chromedriver_linux64.zip

echo "Installation complete."
