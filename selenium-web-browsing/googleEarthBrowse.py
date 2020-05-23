
# Launching Google Earth by implementing wait function

from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;


# Launching driver

driver = webdriver.Chrome();
driver.maximize_window(); #Maximizes the viewing window

# URL 
driver.get('https://www.google.com/intl/en_in/earth/');

# Implementing wait
wait = WebDriverWait(driver, 5); # Waits for 5 sec before clicking
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a')));
launchEarthButton.click();