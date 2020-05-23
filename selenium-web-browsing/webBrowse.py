
# Simple bot interacting with a multi-input field webpage
from selenium import webdriver;

# URL
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html';


######### Single Input Field

# Initializing driver
driver = webdriver.Chrome();
driver.get(url);

# We will now access the text box by through its XPath
messageField = driver.find_element_by_xpath('//*[@id="user-message"]');

# Interacting with the text box
messageField.send_keys("Hello World!");

# Activating the Show Message button
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button');
showMessageButton.click();


######### Double Input Field

# We will now access the text box by through its XPath
inputField1 = driver.find_element_by_xpath('//*[@id="sum1"]');
inputField2 = driver.find_element_by_xpath('//*[@id="sum2"]');

# Interacting with the text box
inputField1.send_keys("10");
inputField2.send_keys("201");

# Activating the Show Message button
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button');
getTotalButton.click(); 