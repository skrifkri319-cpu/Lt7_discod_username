import requests
import random
import string
import time
import os

# الألوان المـحددة بصفتها أدوات التدمير والبصر
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def clear():
    os.system('clear')

def banner():
    print(RED + "="*40)
    print("              LT7               ")
    print("="*40 + RESET)

def generate_user():
    chars = string.ascii_lowercase + string.digits + "_" + "."
    return ''.join(random.choice(chars) for i in range(4))

def check_user(user):
    url = f"https://discord.com/api/v9/users/{user}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 404:
            print(f"{WHITE}>>>> {user} {GREEN}[ AVAILABLE / متاح ]{RESET}")
            with open("hits_LT7.txt", "a") as f:
                f.write(user + "\n")
        elif response.status_code == 429:
            print(f"{YELLOW}[!] Rate Limit! Waiting 60s...{RESET}")
            time.sleep(60)
        else:
            print(f"{WHITE}>>>> {user} {RED}[ TAKEN / غير متاح ]{RESET}")
    except:
        print(f"{BLUE} Network Lagged!{RESET}")

# الحلقة الأبـديـة للبرنامج (لا يخرج أبداً)
while True:
    clear()
    banner()
    
    try:
        print(f"{BLUE}How many users do you want to check, Master?{RESET}")
        print(f"{YELLOW}(Max limit is 100 users){RESET}")
        
        user_input = input(f"{WHITE}Jumlah/Quantity >> {RESET}")
        amount = int(user_input)

        if amount > 100:
            print(f"{RED}Amount exceeds limit! Setting to 100.{RESET}")
            amount = 100
        elif amount <= 0:
            print(f"{RED}Enter a valid positive number!")
            time.sleep(2)
            continue

        print(f"\n{GREEN}System Ready! Hunting {amount} users...{RESET}")
        time.sleep(2)
        clear()
        banner()

        count = 0
        while count < amount:
            current_user = generate_user()
            check_user(current_user)
            count += 1
            print(f"{BLUE} Progress: {count}/{amount} {RESET}")
            print("-" * 20)
            time.sleep(1.3)

        print(f"\n{GREEN}Success! Current wave ended. Rotating system...{RESET}")
        time.sleep(3) # وقت مستقطع قبل العودة لقائمة التحديد

    except ValueError:
        print(f"{RED}ERROR: Write numbers only a la la!{RESET}")
        time.sleep(2)
    except KeyboardInterrupt:
        print(f"\n{RED}Stopped by God Master! Farewell...{RESET}")
        break # الخروج فقط عندضغط Ctrl+C

