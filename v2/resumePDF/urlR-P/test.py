from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
service = Service('../chromedriver/chromedriver.exe')  # Update with the path to your chromedriver

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.indeed.com/?advn=921708835097726&vjk=4a0075382e5a3043'
driver.get(url)

try:
    # Wait until the job title is present
    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="vjs-container"]/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/h2/span'))
    )
    title = title_element.text

    # Wait until the job description is present
    description_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="jobDescriptionText"]'))
    )
    description = description_element.text

    print(f"Job Title: {title}")
    print(f"Job Description: {description[:200]}...")  # Print a preview of the description

finally:
    driver.quit()
