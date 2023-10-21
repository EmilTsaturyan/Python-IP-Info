import requests
import pyfiglet
from colorama import Fore
import os
import platform

colors = [
          Fore.RED, Fore.LIGHTRED_EX, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.CYAN, Fore.LIGHTCYAN_EX, 
          Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.LIGHTRED_EX, Fore.RED, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX
          ]

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def get_public_ip():
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    return data

def get_info_by_ip(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    response = response.json()
    if response['status'] == 'success':
        return response
    else:
        return False

def printing_info(info):
    for k, i in zip(colors, info):
        print(k + f'{i}: {info[i]}')

def txt_file(info):
    with open('info.txt0', 'w'):
        pass
    with open('info.txt', 'a') as fl:
        for i in info:
            fl.write(f'{i}: {info[i]}\n')
    print('All inforamtion succesfully saved in info.txt')

def google_maps(info):
    link = f'https://www.google.com/maps/@{info["lat"]},{info["lon"]},19z?entry=ttu'
    info['google maps'] = link
    return link

def welcome_message():
    clear()
    Banner = pyfiglet.figlet_format('Python  IP  INFO', font='standard')
    print(Fore.MAGENTA + Banner)

def choosing_options():
    print(Fore.BLUE + '[1] - My IP')
    print(Fore.MAGENTA + '[2] - Other IP')
    print(Fore.LIGHTGREEN_EX + '[3] - Exit')
    try:
        option = int(input('Choose the option: '))
        if option in (1, 2, 3):
            return option
        else:
            return False
    except ValueError:
        print('Please select right option')
        exit()
    
def main():
    welcome_message()
    option = choosing_options()
    if option == 1:
        info = get_public_ip()
    elif option == 2:
        welcome_message()
        ip = input(Fore.LIGHTMAGENTA_EX + 'Enter the ip: ')
        info = get_info_by_ip(ip)
        if not info:
            print('Wrong IP')
            exit()
    elif option == 3:
        exit()
    else:
        print('Please select right option')
        exit()
    
    google_maps(info)
    printing_info(info)
    txt_file(info)
    

if __name__ == '__main__':
    main()
