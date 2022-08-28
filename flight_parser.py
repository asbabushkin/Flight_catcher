"""
Реализация через telethon & schedule

Запрос все рейсы
https://www.onetwotrip.com/_avia-search-proxy/search/v3?route=0110CEKMOW0710&ad=2&cn=1&in=1&showDeeplink=false&cs=E&source=yandex_direct&priceIncludeBaggage=true&noClearNoBags=true&noMix=true&srcmarker=airlines_airport_desk_all_agency1_cpa_k36332661070&cryptoTripsVersion=61&doNotMap=true

Лучший рейс на плавающие даты
https://www.onetwotrip.com/_avia/deals_v4/directApiTop?origin=CEK&destinations=MOW&departure_date_from=2022-09-29&departure_date_to=2022-10-03&roundtrip_flights=true&noPricing=false&group_by_date=true&deals_limit=50&all_combinations=true&source=yandex_direct&return_date_from=2022-10-05&return_date_to=2022-10-09
"""

import schedule
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from telethon import TelegramClient, events, sync, connection


from fl_catcher_data import telegram_api, telegram_hash, url_ottrip

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('/home/asb/Python/Parsing_course/coordinates.crx')




def get_one_two_trip(url):
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get(url)
        if WebDriverWait(browser, 100, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'c27ZC'))):
            div = browser.find_element(By.CLASS_NAME, 'jC6yz')
            return div.find_elements(By.CLASS_NAME, '_4-iO8')[1].text


def main():
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options_chrome.add_argument(f'user-agent={user_agent}')
    price = get_one_two_trip(url_ottrip)
    print(price)
    with TelegramClient('flight_catcher', telegram_api, telegram_hash) as client:
        client.send_message('@asbabushkin', message=f'Flight catcher: цена перелета {price}')


if __name__ == '__main__':

    schedule.every().minute.do(main)
    while True:
        schedule.run_pending()