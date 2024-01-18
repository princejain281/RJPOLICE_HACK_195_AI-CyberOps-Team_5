from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def analyze_text_content(html_content):
    # Use regular expressions for more flexible pattern matching
    fake_ad_patterns = [
    r'earn(ing)? money fast',
    r'guaranteed returns',
    r'secret method',
    r'limited time offer',
    r'get rich quick',
    r'no risk, high reward',
    r'easy money',
    r'cash in minutes',
    r'exclusive deal',
    r'never seen before',
    r'instant results',
    r'risk-free investment',
    r'100% guaranteed',
    r'limited spots available',
    r'secret formula',
    r'automatic profits',
    r'double your money',
    r'zero effort, maximum gain',
    r'overnight success'
]
    for pattern in fake_ad_patterns:
        if re.search(pattern, html_content, re.IGNORECASE):
            return True  # Fake ad detected
    return False

def check_for_unexpected_behavior(driver):
    try:
        # Use a more specific XPath to target potential fake ad elements
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "fake-ad")]')))
        return True  # Fake ad detected
    except Exception as e:
        print(f"No fake ads detected: {e}")
        return False

def main():
    url = input("Please enter the full URL of the webpage: ")

    # Fetch the HTML content of the webpage
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        html_content = driver.page_source

        # Analyze text content for fake ads
        fake_ad_detected = analyze_text_content(html_content)

        # Check for unexpected behavior related to fake ads
        fake_ad_behavior_detected = check_for_unexpected_behavior(driver)

        if fake_ad_detected or fake_ad_behavior_detected:
            print("Fake ads detected on the webpage.")
        else:
            print("No fake ads detected on the webpage.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
