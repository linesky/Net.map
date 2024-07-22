
import os
import subprocess
import time
print("\x1bc\x1b[47;34m")
# Definir o intervalo de IPs
ip_base = "192.168.1."
ip_range = range(1, 19)
timeout = 20  # Tempo máximo de espera em segundos para o ping

# Apagar o arquivo list.txt se existir
if os.path.exists("list.txt"):
    os.remove("list.txt")

# Função para verificar o ping
def check_ping(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", str(timeout), ip],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        return not("erro" in result.stdout.lower())
    except subprocess.TimeoutExpired:
        return False

# Função para obter o nome do computador
def get_hostname(ip):
    try:
        result = subprocess.run(["nslookup", ip],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        # Parsing o nome do computador da saída do nslookup
        for line in result.stdout.split("\n"):
            if "name =" in line.lower():
                return line.split("=")[1].strip()
    except Exception as e:
        return None
    return None

# Verificar todos os IPs na faixa
for i in ip_range:
    ip = ip_base + str(i)
    print(f"Verificando {ip}...")

    if check_ping(ip):
        hostname = get_hostname(ip)
        #if hostname:
        if 0==0:
            print(f"{ip} - {hostname}")
            with open("list.txt", "a") as f:
                f.write(f"{ip} - {hostname}\n")

# Copiar list.txt para map.txt
if os.path.exists("list.txt"):
    with open("list.txt", "r") as f:
        with open("map.txt", "w") as map_file:
            map_file.write(f.read())

print("Mapeamento completo.")
