
# Bot implementation of drag and drop on a webpage
from selenium import webdriver;

# For drag and drop, we need a new extension, ActionChains
from selenium.webdriver.common.action_chains import ActionChains;


driver = webdriver.Chrome();
driver.maximize_window(); #Maximizes the viewing window

# URL 
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html');

# Specify the source and destination for the drag and drop
source = driver.find_element_by_xpath('//*[@id="box3"]');
destination = driver.find_element_by_xpath('//*[@id="box103"]');

# Performing drag and drop
action = ActionChains(driver);
action.drag_and_drop(source, destination).perform();
