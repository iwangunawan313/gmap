from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

from selenium.common.exceptions import TimeoutException
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import pandas as pd


def scrape_places_links(query):
    # Inisialisasi WebDriver
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service)

    def visit_google_maps():
        # Encode query untuk URL
        encoded_query = urllib.parse.quote_plus(query)
        url = f'https://www.google.com/maps/search/{encoded_query}'
        driver.get(url)

        # Terima Cookies untuk pengguna Eropa (jika ada)
        try:
            agree_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'form:nth-child(2) > div > div > button'))
            )
            agree_button.click()
            driver.get(url)
        except Exception as e:
            print("Tidak ada prompt cookie:", e)

    def scroll_to_end_of_places_list():
        end_of_list_detected = False
        while not end_of_list_detected:
            try:
                # Scroll pada elemen daftar tempat
                places_list = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[role="feed"]'))
                )
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", places_list)
                print("Scrolling...")
                time.sleep(2)

                # Cek apakah sudah mencapai akhir daftar
                end_of_list_indicator = driver.find_elements(By.CSS_SELECTOR, "p.fontBodyMedium > span > span")
                if end_of_list_indicator:
                    end_of_list_detected = True
                    print("Successfully scrolled to the end of the places list.")
            except Exception as e:
                print("Error during scrolling:", e)
                end_of_list_detected = True

    def extract_place_links():
        try:
            # Ambil semua link tempat
            places_links = driver.find_elements(By.CSS_SELECTOR, '[role="feed"] > div > div > a')
            return [link.get_attribute("href") for link in places_links]
        except Exception as e:
            print("Error extracting links:", e)
            return []

    visit_google_maps()
    scroll_to_end_of_places_list()

    # Ekstraksi semua link
    places_links = extract_place_links()
    driver.quit()
    return places_links

# Menjalankan fungsi scrape
query = "salon kecantikan in brebes"
links = scrape_places_links(query)

# Menampilkan hasil
# print(links)

# Fungsi untuk mengonversi timestamp menjadi ISO date
def toiso(date):
    return date.isoformat()

def convert_timestamp_to_iso_date(timestamp):
    milliseconds = int(timestamp) / 1000
    date = datetime.utcfromtimestamp(milliseconds)
    return toiso(date)

# Fungsi untuk scraping data tempat
def scrape_place(link):
    try:
        # Inisialisasi WebDriver
        service = Service("./chromedriver")
        driver = webdriver.Chrome(service=service)

        print(f"Mengunjungi link: {link}")
        driver.get(link)

        # Terima Cookies jika ada (untuk pengguna Eropa)
        try:
            agree_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'form:nth-child(2) > div > div > button'))
            )
            agree_button.click()
            time.sleep(1)  # Tunggu sejenak sebelum lanjut
        except TimeoutException:
            print("Tidak ada prompt cookie.")

        # Ekstrak data
        title = driver.find_element(By.CSS_SELECTOR, 'h1').text if driver.find_elements(By.CSS_SELECTOR, 'h1') else None
        address = driver.find_element(By.CSS_SELECTOR, "button[data-item-id='address']").text if driver.find_elements(By.CSS_SELECTOR, "button[data-item-id='address']") else None
        rating = driver.find_element(By.CSS_SELECTOR, "div.F7nice > span").text if driver.find_elements(By.CSS_SELECTOR, "div.F7nice > span") else None

        reviews_text = driver.find_element(By.CSS_SELECTOR, "div.F7nice > span:last-child").text if driver.find_elements(By.CSS_SELECTOR, "div.F7nice > span:last-child") else None
        reviews = int(''.join(filter(str.isdigit, reviews_text))) if reviews_text else None

        website = driver.find_element(By.CSS_SELECTOR, "a[data-item-id='authority']").get_attribute('href') if driver.find_elements(By.CSS_SELECTOR, "a[data-item-id='authority']") else None

        phone_element = driver.find_elements(By.XPATH, "//button[starts-with(@data-item-id,'phone')]")
        phone = phone_element[0].get_attribute("data-item-id").replace("phone:tel:", "") if phone_element else None

        driver.quit()

        return {
            "title": title,
            "address": address,
            "phone": phone,
            "website": website,
            "reviews": reviews,
            "rating": rating,
            "link": link,
        }

    except Exception as e:
        print(f"Error scraping link {link}: {e}")
        return None

# Fungsi utama untuk scraping paralel
def scrape_places_parallel(links, max_workers=5):
    results = []

    # Menggunakan ThreadPoolExecutor untuk menjalankan browser paralel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scrape_place, link): link for link in links}
        for future in as_completed(futures):
            try:
                result = future.result()
                if result:
                    results.append(result)
            except Exception as e:
                print(f"Error in thread: {e}")

    return results

# Jalankan scraping paralel
hasil = scrape_places_parallel(links, max_workers=5)

# Simpan hasil ke Excel
df = pd.DataFrame(hasil)
excel_writer = pd.ExcelWriter(f"output/{query}.xlsx")
#excel_writer = pd.ExcelWriter('output/hasil_scrape_parallel.xlsx', engine='xlsxwriter')
df.to_excel(excel_writer, sheet_name='Sheet1', index=False)
excel_writer._save()

print("Scraping selesai. Data disimpan di 'output/hasil_scrape_parallel.xlsx'.")
