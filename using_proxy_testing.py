from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# Define the free proxy details
proxy_address = "157.245.97.60"
proxy_port = "80"

# Set up the proxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f"http://{proxy_address}:{proxy_port}"
proxy.ssl_proxy = f"https://{proxy_address}:{proxy_port}"

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy.ssl_proxy}')

# Create a Chrome webdriver instance with the proxy
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
login_url="https://www.linkedin.com/home"


username = "vivow74149@cumzle.com"
password = "shubham@24"

"""Here we get the login url"""
try:
    driver.get(login_url)
    print("inside")
except Exception as e:
    print(e)
try:

    username_field = driver.find_element(By.ID, "session_key")
    password_field = driver.find_element(By.ID, "session_password")

except Exception as e:
    print(e)

"""Using send keys method sent the username and password"""
try:

    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.implicitly_wait(50)

except Exception as e:
    print(e)
"""After filling username and password click on sign up button"""
try:
    click_on_button = driver.find_element(By.XPATH, '//button[@data-id="sign-in-form__submit-btn"]').click()
except Exception as e:
    print(e)

# Navigate to your webpage
driver.get("https://www.linkedin.com/in/michael-stokes-864795b1/")  # Replace with your actual URL
# "for section 8"""
# exp = None
# type_of_job_text = None
# job_duration_text = None
# job_location_text = None
# try:
#     driver.implicitly_wait(15)
#     match_header_as_exp = driver.find_element(By.XPATH,
#                                               "//main[@class='scaffold-layout__main']/section[4]/div[2]/div/div/div/h2/span[1]")
#     exp = match_header_as_exp.text
# except Exception as e:
#     print("Header is not locating in section 4")
# if exp == "Experience":
#     try:
#
#         driver.implicitly_wait(15)
#         job_title = driver.find_element(By.XPATH,
#                                         "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
#
#         job_title_text = job_title.text
#         print(job_title_text)
#
#         driver.implicitly_wait(15)
#         type_of_job = driver.find_element(By.XPATH,
#                                           "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
#         type_of_job_text = type_of_job.text
#         print(type_of_job_text)
#
#         driver.implicitly_wait(15)
#         job_duration = driver.find_element(By.XPATH,
#                                            "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
#         job_duration_text = job_duration.text
#         print(job_duration_text)
#
#         driver.implicitly_wait(15)
#         job_location = driver.find_element(By.XPATH,
#                                            "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
#         job_location_text = job_location.text
#         print(job_location_text)
#
#         print("located in single listing 4")
#     except Exception as e:
#         print("not located in single listing 4")
#         """here sub listed job title are coded"""
#         try:
#             try:
#                 driver.implicitly_wait(15)
#
#                 job_title = driver.find_element(By.XPATH,
#                                                 "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
#                 job_title_text = job_title.text
#                 print(job_title_text)
#             except Exception as e:
#                 job_title_text = "Job title not present"
#                 print(str(e))
#             try:
#                 driver.implicitly_wait(15)
#                 type_of_job = driver.find_element(By.XPATH,
#                                                   "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
#                 type_of_job_text = type_of_job.text
#
#
#             except Exception as e:
#                 type_of_job_text = None
#                 print(str(e))
#
#             try:
#                 driver.implicitly_wait(15)
#                 job_duration = driver.find_element(By.XPATH,
#                                                    "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
#                 job_duration_text = job_duration.text
#
#
#
#             except Exception as e:
#                 job_duration_text = "Job duration not present"
#                 print(str(e))
#
#             try:
#                 driver.implicitly_wait(15)
#                 job_location = driver.find_element(By.XPATH,
#                                                    "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
#                 job_location_text = job_location.text
#
#             except Exception as e:
#                 print(str(e))
#                 try:
#                     job_location_text = driver.find_element(By.XPATH,
#                                                             "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
#                 except Exception as e:
#                     job_location_text = "Job location not present"
#
#             print("located in sub listing 4")
#         except Exception as e:
#             print("Unable to locate nested job title in section 4")
#
# # Add your scraping logic here
#
# Close the browser
driver.quit()
