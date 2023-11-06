import serial
import time
from pyflipper.pyflipper import PyFlipper
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import hashes
import binascii
import base64


# time.sleep(1)
# Chiave segreta condivisa tra il key e il car
shared_key = 'CryptoSentinelDefenderXAutomotive1984'.encode(encoding='ascii', errors='strict')

#id Friend
friend_id = "Invaye"


def send_command(serial_port, command):
    # Invia il comando sulla porta seriale
    command = command + '\r'
    serial_port.write(command.encode(encoding='ascii', errors='strict'))



def extract_data(line, friend_id, status):
    parts = line.partition(status + '.')
    # print(parts)
    if len(parts) == 3:
        header = parts[0].removeprefix('\x1b[0').removesuffix('\x1b[0m: ')
        # header_parts = parts[0].strip().split(':', 1)
        # header = header_parts[0].strip()
        # assert header_raw.startswith(';')
        # header = header_raw[header_raw.find('m'):]
        encoded_data = parts[2].strip()
        if friend_id in header:
            return encoded_data
    return None


def calculate_response(challenge):
    # Calcola l'HMAC del challenge utilizzando la chiave condivisa
    h = hmac.HMAC(shared_key, hashes.SHA256())
    h.update(challenge) 
    hmac_value = h.finalize()

    return hmac_value


def main():
    # Apre la porta seriale
    flipper = serial.Serial('/dev/ttyACM0')


    time.sleep(1)
    # Invia il comando predefinito sulla porta seriale
    send_command(flipper, "subghz chat 433920000")

    time.sleep(1.4)

    wakeup_base64 = base64.b64encode(b'01010101').decode('ascii')
    print("[KEY] wakeup base64:  ", wakeup_base64)
    wakeup = "wakeup." + wakeup_base64
    print("[KEY] wakeup sent:  ", wakeup)

    send_command(flipper, wakeup)
    time.sleep(1.4)

    #Leggi linea per linea dalla porta seriale
    for line in flipper:
        line = line.decode().strip()  # Decodifica la riga e rimuove gli spazi bianchi
        # print(line)  # Stampa la riga

        string = "challenge."
        if string in line:
            result = line
            # Esci dal ciclo
            break

    status = "challenge"
    challenge_base64 = extract_data(result, friend_id, status)
    print("\n[KEY] challenge extracted:   ", challenge_base64)
    challenge_raw = base64.b64decode(challenge_base64)
    print("\n[KEY] challenge decoded:   ", challenge_raw.hex())

    response_raw = calculate_response(challenge_raw)
    print("[KEY] challenge resolved: ", response_raw.hex())
    response_base64  = base64.b64encode(response_raw).decode('ascii')
    response = "response." + response_base64

    time.sleep(1.4)
    send_command(flipper, response)
    print("\n[KEY] response sent: ", response)
    time.sleep(2)



if __name__ == "__main__":
    main()
