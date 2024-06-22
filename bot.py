import requests
import time
from datetime import datetime
import json
import sys
import os
from colorama import *

init(autoreset=True)

red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
black = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL
white = Fore.LIGHTWHITE_EX


# Clear the terminal
def clear_terminal():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For macOS and Linux
    else:
        _ = os.system("clear")


# Claim
def meow_claimer(telegram_id, is_on_chain, auth_data):
    url = f"https://api.supermeow.vip/meow/claim?telegram={telegram_id}&is_on_chain={is_on_chain}&auth_data={auth_data}"

    headers = {
        "authority": "api.supermeow.vip",
        "medthod": "POST",
        "path": f"/meow/claim?telegram={telegram_id}&is_on_chain={is_on_chain}&auth_data={auth_data}",
        "scheme": "https",
        "Accept": "application/json; indent=2",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "0",
        "Content-Type": "application/json",
        "Origin": "https://lfg.supermeow.vip",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://lfg.supermeow.vip/",
        "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"{green}Claim: Done")
    else:
        print(f"{red}Error! Try again")


# Check in
def meow_checkin(telegram_id, is_on_chain, auth_data):
    url = f"https://api.supermeow.vip/meow/serial-checkin?telegram={telegram_id}&is_on_chain={is_on_chain}&auth_data={auth_data}"

    headers = {
        "authority": "api.supermeow.vip",
        "medthod": "POST",
        "path": f"/meow/serial-checkin?telegram={telegram_id}&is_on_chain={is_on_chain}&auth_data={auth_data}",
        "scheme": "https",
        "Accept": "application/json; indent=2",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "0",
        "Content-Type": "application/json",
        "Origin": "https://lfg.supermeow.vip",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://lfg.supermeow.vip/",
        "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }

    response = requests.post(url, headers=headers)
    data = response.text
    try:
        info = data.split(": ", 1)[1].split("\n", 1)[0]
        if info == "true":
            print(f"{green}Check in: Done")
        if info == "false":
            print(f"{yellow}Checked in already")
        else:
            print(f"{red} Check in error")
    except Exception as e:
        print(f"{red}Check in error")


def main():
    clear_terminal()
    banner = f"""

    {blue}Smart Airdrop {white}Supermeow Auto Claimer
    t.me/smartairdrop2120

    """
    print(banner)
    while True:
        data = json.loads(open("data.json", "r").read())
        is_on_chain = json.loads(open("config.json", "r").read())["is_on_chain"]
        for name, values in data.items():
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"[{now}] --- Account name: {name} ---")
            meow_claimer(
                telegram_id=values["telegram_id"],
                is_on_chain=is_on_chain,
                auth_data=values["auth_data"],
            )
            meow_checkin(
                telegram_id=values["telegram_id"],
                is_on_chain=is_on_chain,
                auth_data=values["auth_data"],
            )
        wait_time = 60 * 60
        print(f"{yellow}Wait for {int(wait_time/60)} minutes!")
        print()
        time.sleep(wait_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
