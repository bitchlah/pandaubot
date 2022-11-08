# /usr/bin/python3
# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# Please read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# Recode Panda Userbot
## Thanks full Ultroid For installer termux env


from time import sleep
from os import system, path

PANDA = "★ PANDA USERBOT DEPLOY★"


def clear():
    system("clear")


def with_header(text):
    return PANDA + "\n\n" + text

def telethon():
    yes_no = input("").strip().lower()
    if yes_no in ["telethon", "t"]:
        return True
    elif yes_no in ["notelethon", "not"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return telethon()

def pyrogram():
    yes_no = input("").strip().lower()
    if yes_no in ["pyrogram", "p"]:
        return True
    elif yes_no in ["nopyrogram", "nop"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return pyrogram()

def ask_process_info_text():
    strm = input("").lower().strip()
    if strm == "e":
        print("Exiting...")
        exit(0)
    elif strm != "a":
        print("Invalid Input")
        print("Enter 'A' to Continue or 'E' to exit...")
        ask_process_info_text()
    elif strm != "ap":
        print("Invalid Input")
        print("Enter 'A' to Continue or 'E' to exit...")
        ask_process_info_text()


def envtelethon():
    start = input("").strip().lower()
    if start in ["telethon", "t"]:
        print(f"Ketik t untuk Creating .env file.. Telethon")
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "SESSION", "DATABASE_URL", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN", "BOT_USERNAME"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        print("* Created '.env' file successfully!")
        sleep(0.1)
        system("screen -S PandaX_Userbot")
        system("bash start")
   
def envpyrogram():
    startp = input("").strip().lower()
    if startp in ["pyrogram", "p"]:
        print(f"Ketik p untuk Creating .env file.. Pyrogram")
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "PyroSESSION", "DATABASE_URL", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN", "BOT_USERNAME"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        print("* Created '.env' file successfully! 😃 klik enter")
        sleep(0.1)
        system("screen -S PandaX_Userbot")
        system("bash start")

if not path.exists(".env"):
    print(with_header("Silahkan ketik t untuk telethon"))
    envtelethon()
   
    
if not path.exists(".env"):
    print(with_header("Silahkan ketik p untuk pyrogram "))
    envpyrogram()
