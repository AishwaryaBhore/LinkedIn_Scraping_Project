import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import undetected_chromedriver as uc

"""Here created object of webdriver"""
options = webdriver.ChromeOptions()
options.add_argument('proxy-server=181.65.200.53:80')

try:
    driver = uc.Chrome(options=options, )
except Exception as e:
    print(str(e))

    """Execution starts from here"""
job_types = ["full-time", "Full-time", "part-time", "Part-time", "Intern",
             "intern", "Contract", "contract", "in trim", "In Trim", "Freelancer", "Permanent", "permanent"]


def main():
    global username_field, password_field, login_url, job_title1, job_title
    """Login url for linkedIn"""
    try:
        login_url = "https://www.linkedin.com/home"
    except Exception as e:
        print(str(e))

    """To scrape information from linkedIn first have to login so here is credentials"""

    username = "temik43060@cumzle.com"
    password = "shubham@24"

    """Here we get the login url"""

    try:
        driver.get(login_url)
        driver.maximize_window()
    except Exception as e:
        print(str(e))
    """Located username and password field """
    try:
        username_field = driver.find_element(By.ID, "session_key")
        password_field = driver.find_element(By.ID, "session_password")
    except Exception as e:
        print(str(e))

    """Using send keys method sent the username and password"""
    try:
        username_field.send_keys(username)
        password_field.send_keys(password)
    except Exception as e:
        print(str(e))

    """After filling username and password click on sign up button"""
    try:
        driver.implicitly_wait(5)
        click_on_button = driver.find_element(By.XPATH, '//button[@data-id="sign-in-form__submit-btn"]').click()
    except Exception as e:
        print(str(e))

    """To take linkedIn link of prospect here we use excel file """
    file_path = 'File1.xlsb'

    """Column name from excel file """
    column_name = 'Job Title Link'

    """read excel file and extract column"""
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        # Extract the specified column as a list
        column_data = df[column_name].tolist()
        column_data = [link for link in column_data if pd.notna(link)]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except KeyError:
        print(f"Column '{column_name}' not found in the Excel file.")

    """Created pattern to validate the linkedIn link"""
    linkedin_pattern = r'https:\/\/www\.linkedin\.com\/in\/[A-Za-z0-9-]+\/?'

    """Empty list to store prospect details"""
    scraped_data = []

    new_data_list = [
        'https://www.linkedin.com/in/michael-stokes-864795b1/','https://www.linkedin.com/in/imranhusain1/','https://www.linkedin.com/in/kate-silverman/']
    # 'https://www.linkedin.com/in/aaroninsecurity/'
    # 'https://www.linkedin.com/in/carrie-mccomb-64451124/?originalSubdomain=uk']
    # 'https://www.linkedin.com/in/leonspight/']
    # 'https://www.linkedin.com/in/gordon-turnbull-868b4813/?originalSubdomain=uk',
    # 'https://www.linkedin.com/in/mandyscullion/?originalSubdomain=uk',
    # 'https://www.linkedin.com/in/imranhusain1/', 'https://www.linkedin.com/in/conor-jones-aa6590141/','https://www.linkedin.com/in/kate-silverman/']
    # Iterate through the links
    for link in new_data_list:
        name = None,
        count_of_connections = None,
        # job_title = None,
        job_title_text = None,
        type_of_job = None,
        type_of_job_text = None
        job_duration = None,
        job_duration_text = None,
        job_location = None,
        job_location_text = None,
        company_name = None,
        company_website = None,
        industry_type = None,
        No_of_emp = None,
        count_of_employee = None,
        get_associated_member_text = None,
        get_href = None,
        get_industry = None,
        get_company_size_text = None,
        user_link = None,
        exp = None
        match_header_as_exp = None
        """Match link with LinkedIn pattern"""
        if re.match(linkedin_pattern, link):
            print(f"Valid LinkedIn Link: {link}")
            driver.get(link)
            user_link = link
        else:
            print(f"Skipping: {link}" "This is not linkedIn link")

        """Here we locate and scrape the name of user"""
        try:
            driver.implicitly_wait(5)
            name = driver.find_element(By.XPATH,
                                       "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']").text
        except Exception as e:
            print(str(e))

        """Here we locate and scrape the count of connections of user"""
        try:
            driver.implicitly_wait(5)
            count_of_connections = driver.find_element(By.XPATH, "//span[@class='t-bold']").text
        except Exception as e:
            try:
                driver.implicitly_wait(5)
                count_of_connections = driver.find_element(By.XPATH, "//span[@class='t-bold']").text
            except Exception as e:
                print(str(e))
                print("this user dont have any connection")
                count_of_connections = "Connections not present"

        """To locate Experience """
        try:
            """For 3rd section"""
            try:
                driver.implicitly_wait(10)
                match_header_as_exp = driver.find_element(By.XPATH,
                                                          "//main[@class='scaffold-layout__main']/section[3]/div[2]/div/div/div/h2/span[1]")
                exp = match_header_as_exp.text
            except Exception as e:
                print(str(e))
            # if experience keyword matches with scraped text
            if exp == "Experience":
                try:
                    """Job title"""
                    driver.implicitly_wait(15)
                    job_title = driver.find_element(By.XPATH,
                                                    "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
                    job_title_text = job_title.text
                    """Job Type"""
                    driver.implicitly_wait(15)
                    type_of_job = driver.find_element(By.XPATH,
                                                      "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
                    type_of_job_text = type_of_job.text
                    """Job Duration"""
                    driver.implicitly_wait(15)
                    job_duration = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
                    job_duration_text = job_duration.text
                    """Job location"""
                    driver.implicitly_wait(15)
                    job_location = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
                    job_location_text = job_location.text
                except Exception as e:
                    print(str(e))
                    """sub listed job title are coded"""
                    try:
                        try:
                            """Job Title"""
                            driver.implicitly_wait(15)
                            job_title = driver.find_element(By.XPATH,
                                                            "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            job_title_text = job_title.text
                        except Exception as e:
                            job_title_text = "Job title not present"
                            print(str(e))
                        try:
                            """Job Type"""
                            driver.implicitly_wait(15)
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
                            type_of_job_text = type_of_job.text
                            job_types = ["full-time", "Full-time", "part-time", "Part-time", "Intern",
                                         "intern", "Contract", "contract", "in trim", "In Trim", "Freelancer"]
                            if not type_of_job_text in job_types:
                                type_of_job = driver.find_element(By.XPATH,
                                                                  "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li/div/div[2]/div/a/span/span")
                                type_of_job_text = type_of_job.text
                        except Exception as e:
                            type_of_job_text = "Job type not present"
                            print(str(e))
                        try:
                            """Job Duration"""
                            driver.implicitly_wait(15)
                            job_duration = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
                            job_duration_text = job_duration.text
                        except Exception as e:
                            job_duration_text = "Job duration not present"
                            print(str(e))
                        try:
                            """Job Location"""
                            driver.implicitly_wait(15)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
                            job_location_text = job_location.text
                        except Exception as e:
                            print(str(e))
                            try:
                                job_location_text = driver.find_element(By.XPATH,
                                                                        "//main[@class='scaffold-layout__main']/section[3]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
                            except Exception as e:
                                try:
                                    job_location_text = driver.find_element(By.XPATH,
                                                                            "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span").text
                                except Exception as e:
                                    job_location_text = "Job location not present"

                    except Exception as e:
                        print(str(e))

            """For 4th section"""
            try:
                driver.implicitly_wait(15)
                match_header_as_exp = driver.find_element(By.XPATH,
                                                          "//main[@class='scaffold-layout__main']/section[4]/div[2]/div/div/div/h2/span[1]")
                exp = match_header_as_exp.text
            except Exception as e:
                print(str(e))
            # if experience keyword matches with scraped text
            if exp == "Experience":
                job_title_temp = False
                try:
                    """Job Title"""
                    # here we check prospect is having single position in one company or got promoted on same company
                    try:
                        time.sleep(5)
                        driver.implicitly_wait(15)
                        job_title = driver.find_element(By.XPATH,
                                                        "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
                        job_title_text = job_title.text

                    except Exception as e:
                        job_title = None
                        print(str(e))
                        try:
                            time.sleep(5)
                            driver.implicitly_wait(15)
                            job_title1 = driver.find_element(By.XPATH,
                                                             "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            jb = job_title1.text
                            print(jb)
                        except Exception as e:
                            print(str(e))
                    # if user is having single position on most recent company

                    if not job_title is None:
                        try:
                            """Job Type"""
                            time.sleep(5)
                            driver.implicitly_wait(15)
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
                            type_of_job_text = type_of_job.text
                        except Exception as e:
                            type_of_job_text = "Job type not present"
                        try:
                            """Job Duration"""
                            time.sleep(5)
                            driver.implicitly_wait(15)
                            job_duration = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
                            job_duration_text = job_duration.text
                        except Exception as e:
                            print(str(e))
                            job_duration_text = "Job duration not present"
                        try:
                            """Job Location"""
                            time.sleep(5)
                            driver.implicitly_wait(15)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
                            job_location_text = job_location.text
                        except Exception as e:
                            print(str(e))
                            job_location_text = "Job location not present"
                    # otherwise we'll check prospect get promoted on same company then we'll scrape accordingly
                    elif job_title1:
                        try:
                            time.sleep(5)
                            """Job Title"""
                            driver.implicitly_wait(15)
                            job_title = driver.find_element(By.XPATH,
                                                            "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            job_title_text = job_title.text
                        except Exception as e:
                            job_title_text = "Job title not present"
                            print(str(e))
                        try:
                            time.sleep(4)
                            driver.implicitly_wait(15)
                            """Job Type"""
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
                            type_of_job_text = type_of_job.text
                        except Exception as e:
                            type_of_job_text = None
                            print(str(e))
                        try:
                            """Job Duration"""
                            time.sleep(4)
                            driver.implicitly_wait(15)
                            job_duration = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
                            job_duration_text = job_duration.text
                        except Exception as e:
                            job_duration_text = "Job duration not present"
                            print(str(e))
                        try:
                            """Job Location"""
                            time.sleep(4)
                            driver.implicitly_wait(15)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
                            job_location_text = job_location.text
                        except Exception as e:
                            print(str(e))
                            try:
                                time.sleep(5)
                                job_location_text = driver.find_element(By.XPATH,
                                                                        "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
                            except Exception as e:
                                try:
                                    time.sleep(5)
                                    job_location_text = driver.find_element(By.XPATH,
                                                                            "//main[@class='scaffold-layout__main']/section[4]/div[3]/ul/li/div/div[2]/div/a/span/span").text
                                except Exception as e:
                                    job_location_text = "Job location not present"
                    else:
                        print("hi")
                except Exception as e:
                    print(str(e))

            """For 5th section"""
            try:
                driver.implicitly_wait(15)
                match_header_as_exp = driver.find_element(By.XPATH,
                                                          "//main[@class='scaffold-layout__main']/section[5]/div[2]/div/div/div/h2/span[1]")
                exp = match_header_as_exp.text
            except Exception as e:
                print(str(e))
            # if experience keyword matches with scraped text
            if exp == "Experience":
                try:
                    """Job Title"""
                    driver.implicitly_wait(15)
                    job_title = driver.find_element(By.XPATH,
                                                    "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
                    job_title_text = job_title.text
                    """Job Type"""
                    driver.implicitly_wait(15)
                    type_of_job = driver.find_element(By.XPATH,
                                                      "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
                    type_of_job_text = type_of_job.text
                    """Job Duration"""
                    driver.implicitly_wait(15)
                    job_duration = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
                    job_duration_text = job_duration.text
                    """Job Location"""
                    driver.implicitly_wait(15)
                    job_location = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
                    job_location_text = job_location.text
                except Exception as e:
                    print(str(e))
                    """sub listed job title are coded"""
                    try:
                        try:
                            """Job Title"""
                            driver.implicitly_wait(15)
                            job_title = driver.find_element(By.XPATH,
                                                            "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            job_title_text = job_title.text
                        except Exception as e:
                            print(str(e))
                            job_title_text = "job title not present"
                        try:
                            """Job Type"""
                            driver.implicitly_wait(15)
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
                            type_of_job_text = type_of_job.text
                            job_types = ["full-time", "Full-time", "part-time", "Part-time", "Intern",
                                         "intern", "Contract", "contract", "in trim", "In Trim", "Freelancer",
                                         "Permanent", "permanent"]
                            if not type_of_job_text in job_types:
                                type_of_job = driver.find_element(By.XPATH,
                                                                  "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li/div/div[2]/div/a/span/span")
                                type_of_job_text = type_of_job.text

                        except Exception as e:
                            type_of_job_text = None
                            print(str(e))
                        try:
                            """Job Duration"""
                            driver.implicitly_wait(15)
                            job_duration = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
                            job_duration_text = job_duration.text
                        except Exception as e:
                            job_duration_text = "Job duration not present"
                        try:
                            """Job Location"""
                            driver.implicitly_wait(14)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
                            job_location_text = job_location.text
                        except Exception as e:
                            print(str(e))
                            try:
                                job_location_text = driver.find_element(By.XPATH,
                                                                        "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
                            except Exception as e:
                                try:
                                    job_location_text = driver.find_element(By.XPATH,
                                                                            "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span").text
                                except Exception as e:
                                    job_location_text = "Job location not present"

                    except Exception as e:
                        print(str(e))

            """For section 6"""
            try:
                driver.implicitly_wait(15)
                match_header_as_exp = driver.find_element(By.XPATH,
                                                          "//main[@class='scaffold-layout__main']/section[6]/div[2]/div/div/div/h2/span[1]")
                exp = match_header_as_exp.text
            except Exception as e:
                print("experience not locating")
            # if experience keyword matches with scraped text
            if exp == "Experience":
                try:
                    """Job Title"""
                    driver.implicitly_wait(15)
                    job_title = driver.find_element(By.XPATH,
                                                    "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
                    job_title_text = job_title.text
                    """Job Type"""
                    driver.implicitly_wait(15)
                    type_of_job = driver.find_element(By.XPATH,
                                                      "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
                    type_of_job_text = type_of_job.text
                    """Job Duration"""
                    driver.implicitly_wait(15)
                    job_duration = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
                    job_duration_text = job_duration.text
                    """Job Location"""
                    driver.implicitly_wait(15)
                    job_location = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
                    job_location_text = job_location.text
                except Exception as e:
                    try:
                        try:
                            """Job Title"""
                            driver.implicitly_wait(15)
                            nested_job_title = driver.find_element(By.XPATH,
                                                                   "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            job_title_text = nested_job_title.text
                        except Exception as e:
                            job_title_text = "Job title not present"
                            print(str(e))
                        try:
                            """Job Type"""
                            driver.implicitly_wait(15)
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
                            type_of_job_text = type_of_job.text
                            job_types = ["full-time", "Full-time", "part-time", "Part-time", "Intern",
                                         "intern", "Contract", "contract", "in trim", "In Trim", "Freelancer"]
                            if not type_of_job_text in job_types:
                                type_of_job = driver.find_element(By.XPATH,
                                                                  "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li/div/div[2]/div/a/span/span")
                                type_of_job_text = type_of_job.text

                        except Exception as e:
                            type_of_job_text = None
                            print(str(e))

                        try:
                            """Job Duration"""
                            driver.implicitly_wait(15)
                            job_duration = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
                            job_duration_text = job_duration.text
                        except Exception as e:
                            job_duration_text = "Jon duration not present"
                            print(str(e))
                        try:
                            """Job Location"""
                            driver.implicitly_wait(15)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
                            job_location_text = job_location.text
                        except Exception as e:
                            try:
                                job_location_text = driver.find_element(By.XPATH,
                                                                        "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
                            except Exception as e:
                                try:
                                    job_location_text = driver.find_element(By.XPATH,
                                                                            "//main[@class='scaffold-layout__main']/section[6]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span").text
                                except Exception as e:
                                    job_location_text = "Job location not present"

                    except Exception as e:
                        print(str(e))

            """For section 7"""
            try:
                driver.implicitly_wait(5)
                match_header_as_exp = driver.find_element(By.XPATH,
                                                          "//main[@class='scaffold-layout__main']/section[7]/div[2]/div/div/div/h2/span[1]")
                exp = match_header_as_exp.text
            except Exception as e:
                print(str(e))
            # if experience keyword matches with scraped text
            if exp == "Experience":
                try:
                    """Job Title"""
                    driver.implicitly_wait(5)
                    job_title = driver.find_element(By.XPATH,
                                                    "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
                    job_title_text = job_title.text
                    """Job Type"""
                    driver.implicitly_wait(5)
                    type_of_job = driver.find_element(By.XPATH,
                                                      "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
                    type_of_job_text = type_of_job.text
                    """Job Duration"""
                    driver.implicitly_wait(5)
                    job_duration = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
                    job_duration_text = job_duration.text
                    """Job Location"""
                    driver.implicitly_wait(5)
                    job_location = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
                    job_location_text = job_location.text
                except Exception as e:
                    try:
                        try:
                            driver.implicitly_wait(5)
                            nested_job_title = driver.find_element(By.XPATH,
                                                                   "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            job_title_text = nested_job_title.text
                        except Exception as e:
                            job_title_text = "Job title not present"
                            print(str(e))
                        try:
                            driver.implicitly_wait(5)
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
                            type_of_job_text = type_of_job.text
                        except Exception as e:
                            type_of_job_text = None
                            print(str(e))
                        try:
                            driver.implicitly_wait(5)
                            duration = driver.find_element(By.XPATH,
                                                           "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
                            job_duration_text = duration.text
                        except Exception as e:
                            job_duration_text = "Job duration not present"
                            print(str(e))
                        try:
                            driver.implicitly_wait(5)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
                            job_location_text = job_location.text
                        except Exception as e:
                            try:
                                job_location_text = driver.find_element(By.XPATH,
                                                                        "//main[@class='scaffold-layout__main']/section[7]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
                            except Exception as e:
                                job_location_text = "Job location not present"
                    except Exception as e:
                        print("Unable to locate nested job title 7")

            """for section 8"""
            try:
                driver.implicitly_wait(5)
                match_header_as_exp = driver.find_element(By.XPATH,
                                                          "//main[@class='scaffold-layout__main']/section[8]/div[2]/div/div/div/h2/span[1]")
                exp = match_header_as_exp.text
            except Exception as e:
                print("Experience nor locating in section 8")
            if exp == "Experience":
                try:
                    """Job Title"""
                    driver.implicitly_wait(5)
                    job_title = driver.find_element(By.XPATH,
                                                    "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]")
                    job_title_text = job_title.text
                    """Job Type"""
                    driver.implicitly_wait(5)
                    type_of_job = driver.find_element(By.XPATH,
                                                      "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li[1]/div/div[2]/div/div/span[1]/span[1]")
                    type_of_job_text = type_of_job.text
                    """Job Duration"""
                    driver.implicitly_wait(5)
                    job_duration = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li[1]/div/div[2]/div/div/span[2]/span[1]")
                    job_duration_text = job_duration.text
                    """Job Location"""
                    driver.implicitly_wait(5)
                    job_location = driver.find_element(By.XPATH,
                                                       "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li[1]/div/div[2]/div/div/span[3]/span[1]")
                    job_location_text = job_location.text
                except Exception as e:
                    try:
                        try:
                            driver.implicitly_wait(5)
                            nested_job_title = driver.find_element(By.XPATH,
                                                                   "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/div/div/div/div/span")
                            job_title_text = nested_job_title.text
                        except Exception as e:
                            job_title_text = "Job title not present"
                        try:
                            driver.implicitly_wait(5)
                            type_of_job = driver.find_element(By.XPATH,
                                                              "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[2]/span")
                            type_of_job_text = type_of_job.text
                        except Exception as e:
                            type_of_job_text = None
                            print(str(e))
                        try:
                            driver.implicitly_wait(5)
                            job_duration = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span/span[2]")
                            job_duration_text = job_duration.text
                        except Exception as e:
                            print(str(e))
                        try:
                            driver.implicitly_wait(5)
                            job_location = driver.find_element(By.XPATH,
                                                               "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li[1]/div/div[2]/div/a/span[2]/span")
                            job_location_text = job_location.text
                        except Exception as e:
                            try:
                                job_location_text = driver.find_element(By.XPATH,
                                                                        "//main[@class='scaffold-layout__main']/section[8]/div[3]/ul/li/div/div[2]/div[2]/ul/li/div/div[2]/div/a/span[3]/span").text
                            except Exception as e:
                                job_location_text = "Job location not present"
                    except Exception as e:
                        print(str(e))
        except Exception as e:
            print("This user dont have experience.....how do I locate ?")

        """Here classify_exp_attribute  function is called """
        # it returns job type, job duration and job location after classifying
        after_classifying_type_of_job_text, after_classifying_job_duration, after_classifying_job_location = classify_exp_attribute(
            type_of_job_text, job_duration_text, job_location_text)
        print("Job_Type", after_classifying_type_of_job_text)
        print("Job_duration", after_classifying_job_duration)
        print("Job location", after_classifying_job_location)

        # try:
        #     after_classifying_type_of_job_text = driver.find_element(By.XPATH,
        #                                                              "//main[@class='scaffold-layout__main']/section[5]/div[3]/ul/li/div/div[2]/div/a/span/span").text
        #
        # except Exception as e:
        #     print(str(e))

        """Locate company logo url to click on company's page"""
        try:
            driver.implicitly_wait(5)
            company_logo_url = driver.find_element(By.XPATH,
                                                   "//a[@data-field='experience_company_logo']").get_attribute('href')
            # By using driver we get company page
            driver.get(company_logo_url)
        except Exception as e:
            print("Unable to get url of the company")
            company_logo_url = None

        """Here we find name of the company"""
        try:
            driver.implicitly_wait(5)
            company_name = driver.find_element(By.XPATH, "//span[@dir='ltr']").text
        except Exception as e:
            print(str(e))
            company_name = "Company not present"

        """Here we locate the company about page link"""

        company_about_link = None
        try:
            driver.implicitly_wait(5)
            company_about_link = driver.find_element(By.XPATH,
                                                     "//ul[@class='org-page-navigation__items ']/li[2]/a").get_attribute(
                "href")
        except Exception as e:
            print(str(e))
            company_about_link = None

        """By using driver we get the company about page"""
        try:
            driver.get(company_about_link)
        except Exception as e:
            print(str(e))

        """Here we find the website of the company"""

        try:
            driver.implicitly_wait(5)
            website_match = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dt[1]")
            website_match_text = website_match.text
            if website_match_text == "Website":
                driver.implicitly_wait(5)
                get_website = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[1]/a")
                get_href = get_website.get_attribute("href")
        except Exception as e:
            get_href = "Company website not present"

        """Industry type of company"""

        try:
            driver.implicitly_wait(5)
            industry_match = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dt[2]")
            industry_match_text = industry_match.text
            if industry_match_text == "Industry":
                driver.implicitly_wait(5)
                get_industry = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[2]").text
            else:
                driver.implicitly_wait(5)
                industry_match = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dt[3]")
                industry_match_text = industry_match.text
                if industry_match_text == "Industry":
                    driver.implicitly_wait(5)
                    get_industry = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[3]").text
        except Exception as e:
            print("not located industry")
            get_industry = "Industry type not present"

        """Company employee size"""

        try:
            driver.implicitly_wait(5)
            company_size_match = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dt[3]")
            company_size_match_text = company_size_match.text
            if company_size_match_text == "Company size":
                driver.implicitly_wait(5)
                get_company_size = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[3]")
                get_company_size_text = get_company_size.text
            else:
                driver.implicitly_wait(5)
                company_size_match = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dt[4]")
                company_size_match_text = company_size_match.text
                if company_size_match_text == "Company size":
                    driver.implicitly_wait(5)
                    get_company_size = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[4]")
                    get_company_size_text = get_company_size.text
        except Exception as e:
            print(str(e))
            get_company_size_text = "Company size not mentioned"

        """Associated member of company"""

        try:
            driver.implicitly_wait(5)
            get_associated_member = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[4]/a/span")
            get_associated_member_text = get_associated_member.text
        except Exception as e:
            try:
                driver.implicitly_wait(5)
                get_associated_member = driver.find_element(By.XPATH, "//dl[@class='overflow-hidden']/dd[5]/a/span")
                get_associated_member_text = get_associated_member.text
            except Exception as e:
                get_associated_member_text = "Associated member not present"

        """Append data in list"""

        scraped_data.append({
            'Name': name,
            'Connections': count_of_connections,
            'Job Title': job_title_text,
            'Job duration': after_classifying_job_duration,
            'Job Type': after_classifying_type_of_job_text,
            'Job location': after_classifying_job_location,
            'Company Name': company_name,
            'Company Website': get_href,
            'Industry Type': get_industry,
            'No Of Employees': get_company_size_text,
            'Associated Employees': get_associated_member_text,
            'User Link': user_link
        })

        # Create a DataFrame from the scraped data
        df = pd.DataFrame(scraped_data)

        # Export the DataFrame to an Excel file
        df.to_excel('data4.xlsx', index=False)

        print("name of user", name, "Count of connections:", count_of_connections, "Job title:", job_title_text,
              "Job duration of user:", job_duration_text, "Job type of user:", type_of_job_text,
              "Job location of user:", job_location_text,
              "Company name of user:", company_name, "Company website of user:", get_href,
              "Industry type of user:", get_industry, "Company size :", get_company_size_text,
              "associated member to company", get_associated_member_text)


    return


def classify_exp_attribute(jt, jd, jl):
    job_type_temp = jt
    job_duration_temp = jd
    job_location_temp = jl

    """1 Job Type"""
    try:
        if job_type_temp == "Job type not present":
            jt = job_type_temp
        else:
            month_match = None
            try:
                month_match = re.findall(r'\d', job_type_temp)
            except Exception as e:
                print(str(e))
            if month_match:
                jd = job_type_temp
                print("yes", jd)
            else:
                if any(job_type.lower() in job_type_temp.lower() for job_type in job_types):
                    jt = job_type_temp
                    print("Job Type:", jt)
                else:
                    jl = job_type_temp
                    print("Job location", jl)
    except Exception as e:
        print(str(e))

    """ 2 Job duration"""
    try:
        if job_duration_temp == "Job duration not present":
            jd = job_duration_temp
        else:
            month_match = None
            try:
                month_match = re.findall(r'\d', job_duration_temp)
            except Exception as e:
                print(str(e))
            if month_match:
                jd = job_duration_temp

            else:
                if any(job_type.lower() in job_duration_temp.lower() for job_type in job_types):
                    jt = job_duration_temp
                else:
                    jl = job_duration_temp
    except Exception as e:
        print(str(e))

    """3 Job location"""
    try:
        if job_location_temp == "Job location not present":
            jl = job_location_temp
        else:
            month_match = None
            try:
                month_match = re.findall(r'\d', job_location_temp)
            except Exception as e:
                print(str(e))
            if month_match:
                jd = job_location_temp

            else:
                if any(job_type.lower() in job_location_temp.lower() for job_type in job_types):
                    jt = job_location_temp
                else:
                    jl = job_location_temp

    except Exception as e:
        print(str(e))
    return jt, jd, jl


if __name__ == "__main__":
    main()
