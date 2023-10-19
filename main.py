from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pyfiglet
from colorama import Fore
import os

def get_info_by_ip(ip='', option=1):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    actionChains = ActionChains(driver)
    info = {
        "query": None,
        "status": None,
        "continent": None,
        "continentCode": None,
        "country": None,
        "countryCode": None,
        "region": None,
        "regionName": None,
        "city": None,
        "district": None,
        "zip": None,
        "lat": None,
        "lon": None,
        "timezone": None,
        "offset": None,
        "currency": None,
        "isp": None,
        "org": None,
        "as": None,
        "asname": None,
        "mobile": None,
        "proxy": None,
        "hosting": None
    }
    keys = list(info.keys())
    try:
        driver.get('https://members.ip-api.com/')
        time.sleep(3)
        if option == 1:
            driver.find_element(By.CSS_SELECTOR, '#sc > div > div.col-md-8.mx-auto > form > div > div.col-auto > button').click()
            for i in range(2, 47, 2):
                data = driver.find_element(By.CSS_SELECTOR, f'#codeOutput > span:nth-child({i})')
                info[keys[0]] = data.text
                keys = keys[1:]
        elif option == 2:
            input_place = driver.find_element(By.CSS_SELECTOR, '#sc > div > div.col-md-8.mx-auto > form > div > div.col > div > input')
            actionChains.double_click(input_place).perform()
            time.sleep(1)
            input_place.send_keys(ip)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, '#sc > div > div.col-md-8.mx-auto > form > div > div.col-auto > button').click()
            time.sleep(1)
            status = driver.find_element(By.CSS_SELECTOR, '#codeOutput > span:nth-child(6)')
            time.sleep(1)
            if status.text == '"fail"':
                return 'Wrong IP!'
            else:
                for i in range(2, 47, 2):
                    data = driver.find_element(By.CSS_SELECTOR, f'#codeOutput > span:nth-child({i})')
                    info[keys[0]] = data.text
                    keys = keys[1:]
        elif option == 3:
            exit()
        else:
            return False
        return info
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def txt_file(info):
    with open('info.txt', 'a') as fl:
        for i in info:
            fl.write(f'{i}: {info[i]}\n')

def welcome_message():
    Banner = pyfiglet.figlet_format('Python  IP  INFO', font='standard')
    print(Fore.MAGENTA + Banner)

    print(Fore.BLUE + '[1] - My IP')
    print(Fore.MAGENTA + '[2] - Other IP')
    print(Fore.LIGHTGREEN_EX + '[3] - Exit')
    try:
        option = int(input('Choose the option: '))
        if option == 3:
            exit()
        elif option == 2:
            ip = input(Fore.MAGENTA + 'Enter the ip: ')
            info = get_info_by_ip(ip, 2)
        elif option == 1:
            info = get_info_by_ip(option=1)
        if info == 'Wrong IP!':
            print(info)
            exit()
        txt_file(info)
        print(Fore.LIGHTBLUE_EX + 'The information saved in info.txt')
    except Exception:
        print('Choose the correct option!')
        exit()

def main():
    os.system('cls')
    welcome_message()
    

if __name__ == '__main__':
    main()
