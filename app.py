from dotenv import load_dotenv, find_dotenv
import os
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Basic security

load_dotenv(find_dotenv())
env_username = (os.environ.get('LOGIN'))
env_password = (os.environ.get('PASSWORD'))
env_covering = (os.environ.get('COVER'))

driver = webdriver.Firefox()
driver.get("https://hh.ru/login")


# Put login and password


async def log():

    print("WEBDRIVER HAS STARTED")

    select_password = driver.find_element(By.CSS_SELECTOR, "[data-qa='expand-login-by-password']")
    select_password.click()

    username = driver.find_element(By.CSS_SELECTOR, "[data-qa='login-input-username']")
    password = driver.find_element(By.CSS_SELECTOR, "[data-qa='login-input-password']")
        
    username.send_keys(env_username)
    password.send_keys(env_password)
    
    login_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='account-login-submit']")
    login_button.click()

    print("LOGIN SUCCESS")

async def get_cookies():

    with open("login_cookies.txt", "r") as f:
        for line in f:
            cookie = {}
            parts = line.strip().split("; ")
            for part in parts:
                if "=" in part:
                    name, value = part.split("=", 1)
                    cookie[name] = value
    print ("COOKIES GET SUCCESS")

async def show_vacancies():

    await asyncio.sleep(5)
    wait = WebDriverWait(driver, 10)
    show_all_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='recommended-vacancies__show-all']")))
    show_all_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='recommended-vacancies__show-all']")
    show_all_button.click()


async def scroll_down(height):
        
    await asyncio.sleep(5)
    driver.execute_script(f"window.scrollBy(0, {height});")

async def response_button():

    await asyncio.sleep(5)
    wait = WebDriverWait(driver, 10)
    vacancy_response_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='vacancy-serp__vacancy_response']")))
    vacancy_response_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-serp__vacancy_response']")
    vacancy_response_button.click()
    print("RESPONSE SUCCESS")

async def driver_refresh():
    
    await asyncio.sleep(5)
    driver.refresh()
    print("PAGE REFRESH")

async def driver_back():
    
    await asyncio.sleep(5)
    driver.back()
    print("PAGE BACK")

async def response_letter_button():
        
    wait = WebDriverWait(driver, 10)
    vacancy_response_letter_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='vacancy-response-letter-toggle']")))
    vacancy_response_letter_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-response-letter-toggle']")
    vacancy_response_letter_button.click()

async def letter_input():

    vacancy_letter_input = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-response-popup-form-letter-input']")
    vacancy_letter_input.send_keys(env_covering)

async def add_cover_letter():

    wait = WebDriverWait(driver, 10)
    vacancy_add_cover_letter = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='vacancy-response-letter-toggle']")))
    vacancy_add_cover_letter = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-response-letter-toggle']")
    vacancy_add_cover_letter.click()

async def cover_letter_input():

    wait = WebDriverWait(driver, 10)
    vacancy_cover_letter_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='Write down why it is your candidacy that should be of interest to the employer']")))
    vacancy_cover_letter_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Write down why it is your candidacy that should be of interest to the employer']")
    vacancy_cover_letter_input.send_keys(env_covering)

async def cover_letter_submit():

    wait = WebDriverWait(driver, 10)
    vacancy_cover_letter_submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='vacancy-response-letter-submit']")))
    vacancy_cover_letter_submit = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-response-letter-submit']")
    vacancy_cover_letter_submit.click()
      
async def submit_button():
        
    submit_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-response-submit-popup']")
    submit_button.click()
        

async def vacancy_blacklist():

    vacancy_blacklist = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy__blacklist-show-add']")
    vacancy_blacklist.click()
        
    vacancy_blacklist_add = driver.find_element(By.CSS_SELECTOR, "[data-qa='vacancy__blacklist-menu-add-vacancy']")
    vacancy_blacklist_add.click()
    print("ADD VACANCY TO BLACKLIST")
        
    driver.refresh()

async def relocation_warning_confirm():

    wait = WebDriverWait(driver, 10)
    vacancy_relocation_warning_confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='relocation-warning-confirm']")))
    vacancy_relocation_warning_confirm = driver.find_element(By.CSS_SELECTOR, "[data-qa='relocation-warning-confirm']")
    vacancy_relocation_warning_confirm.click()

def __main__():
    
    try:
        
        asyncio.run(response_button())
        print("RESPONSE SUCCESS")
        
        #if driver.find_element(By.CSS_SELECTOR, "[data-qa='relocation-warning-confirm']"):
        #    asyncio.run(relocation_warning_confirm())

        asyncio.run(add_cover_letter())
        asyncio.run(cover_letter_input())
        asyncio.run(scroll_down(600))
        asyncio.run(cover_letter_submit())
        
        
        print("COVER LETTER POST SUCCESS")
        
    except:
        
        driver.get("https://hh.ru")
        asyncio.run(show_vacancies())
        asyncio.run(vacancy_blacklist())
        #asyncio.run(driver_back())

def init():
    
    asyncio.run(log())
    asyncio.run(show_vacancies())

init()
for _ in range(100):
    __main__()