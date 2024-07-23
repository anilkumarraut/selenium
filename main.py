from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep chrome open for long time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)


#  CODE to Loggin to Linkden automicailly
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account?trk=cold_join_sign_in")

# Navigate to 
username = driver.find_element(By.ID, value = "username")
username.send_keys('  //ENTER YOUR Username --OR -- Email // ')   #enter your username


password = driver.find_element(By.ID, value = "password")
password.send_keys('  // YOUR Password //')            # Your password

signin = driver.find_element(By.CLASS_NAME, value = "btn__primary--large")
signin.click()

driver.implicitly_wait(5)

search = driver.find_element(By.CLASS_NAME, "jobs-search-box__input-icon")
search.send_keys(' software engineer', Keys.ENTER()) 


driver.quit(10)