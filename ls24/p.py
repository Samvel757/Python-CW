from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json  

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)


def search_jobs():
    driver = setup_driver()

    try:
        driver.get("https://hh.kz")

        time.sleep(1)

        search_box = driver.find_element(By.NAME, "text")  
        search_box.send_keys("Web-разработчик")
        search_box.send_keys(Keys.RETURN)  
        time.sleep(2)  
        
        close_button = driver.find_element(By.CLASS_NAME, "bloko-modal-close-button")
        close_button.click()

        time.sleep(5)  
        change_city_button = driver.find_element(By.CLASS_NAME, "supernova-navi-item_area-switcher-button")
        change_city_button.click()

        time.sleep(1)

        cities = driver.find_elements(By.CLASS_NAME, "bloko-link")
        almaty_link = None
        for city in cities:
            if city.text == "Алматы":
                almaty_link = city
        almaty_link.click()

        time.sleep(5) 

        jobs = driver.find_elements(By.CLASS_NAME, "magritte-redesign")
        print(jobs)
        jobs_data = []

        for job in jobs:
            try:
                title = job.find_element(By.CSS_SELECTOR,
                                         'span[data-qa="serp-item__title-text"]').text

                try:
                    zp = job.find_element(By.CLASS_NAME, "magritte-text___pbpft_3-0-22").text
                except Exception:
                    zp = ''

                company = job.find_element(By.CSS_SELECTOR,
                                           'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
                link = job.find_element(By.CLASS_NAME, "magritte-link___b4rEM_4-3-16").get_attribute("href")

                jobs_data.append({
                    "title": title,
                    "zp": zp,
                    "company": company,
                    "link": link,
                })

                print(f"Данные о вакансии '{title}' получены")
            finally:
                pass

        with open("jobs_data.json", "w", encoding="utf-8") as file:
            json.dump(jobs_data, file, ensure_ascii=False, indent=4)
            print("Данные сохранены в файл 'jobs_data.json'")

    finally:
        driver.quit()


if __name__ == "__main__":
    search_jobs()
