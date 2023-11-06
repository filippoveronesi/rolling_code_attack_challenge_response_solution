from pyflipper.pyflipper import PyFlipper
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import hashes
import binascii
import serial
import time
import base64
import os

# Chiave segreta condivisa tra il key e il car
shared_key = 'CryptoSentinelDefenderXAutomotive1984'.encode(encoding='ascii', errors='strict')

#id Friend
friend_id = "Ramuclo"




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



def validate_response(response, challenge):
    # Calcola l'HMAC del challenge utilizzando la chiave condivisa
    h = hmac.HMAC(shared_key, hashes.SHA256())
    h.update(challenge) 
    hmac_value = h.finalize()
    expected = hmac_value

    print("\n[CAR]  DECODED RESPONSE: ", response.hex())
    print("[CAR] EXPECTED RESPONSE: ", expected.hex())

    return response == expected


def main():
    # Apre la porta seriale
    flipper = serial.Serial('/dev/ttyACM1')

    time.sleep(2)
    # Invia il comando predefinito sulla porta seriale
    send_command(flipper, "subghz chat 433920000")    

    #encoded_wakeup = base64.b64encode('01010101')
    wakeup = "01010101"
    
    counter = 0

    while True:
        #Leggi linea per linea dalla porta seriale
        for line in flipper:
            line = line.decode().strip()  # Decodifica la riga e rimuove gli spazi bianchi
            # print(line)  # Stampa la riga

            string = "wakeup."
            if string in line:
                # Timestamp di inizio programma
                start_time = time.time()
                result = line
                # Esci dal ciclo
                break

        counter = counter + 1
        print("Received a new wakeup, nr: ", counter)
        status = "wakeup"
        wakeup_exctracted = extract_data(result, friend_id, status)
        print("\n[CAR] wakeup exctracted:  ", wakeup_exctracted )
        decoded_wakeup = base64.b64decode(wakeup_exctracted).decode('ascii')
        print("[CAR] wakeup decoded : ", decoded_wakeup)


        if wakeup in decoded_wakeup:
            print("\n[CAR] wakeup is VALID")

            # Genera una sequenza di 16 byte casuale come challenge
            challenge_raw = os.urandom(16)
   
            
            print("\n[CAR] challenge original:  ", challenge_raw.hex())
            challenge_base64 = base64.b64encode(challenge_raw).decode('ascii')
            print("[CAR] challenge base64: ", challenge_base64)
            challenge = "challenge." + challenge_base64
            
            time.sleep(1.4)
            send_command(flipper, challenge)
            time.sleep(1.4)
            print("[CAR] challenge sent:  ", challenge)        


            for line in flipper:
                line = line.decode().strip()  # Decodifica la riga e rimuove gli spazi bianchi
                # print(line)  # Stampa la riga
                
                # check se arrivato wakeup nuovo e non response, forse da sistemare perchè ritorna nel while e anche lì si aspetta un nuovo wakeup
                if "wakeup." in line:
                    print("\nReceived a new wakeup")
                    continue

                if "response." in line:
                    # Timestamp di fine programma
                    end_time = time.time()
                    result = line
                    # Esci dal ciclo
                    break
           
          
            status = "response"
            response_base64 = extract_data(result, friend_id, status)
            print("\n[CAR] response base64: ", response_base64)
            response_raw = base64.b64decode(response_base64)
            
            # Calcola la differenza di tempo
            elapsed_time = end_time - start_time
            
            if(elapsed_time < 10):
                if validate_response(response_raw, challenge_raw):
                    print("\nResponse is VALID\n")
                    print("======================================================================================\n")
                    #flipper.led.set(led='g', value=255)
                else:
                    print("\nResponse is INVALID\n")
                    print("======================================================================================\n")
                    #flipper.led.set(led='r', value=255)
            else:
                print("\nTimeout expired, invalid response\n")
                print("======================================================================================\n")
                print("Waiting to new wakeup...\n")
                continue
            
            time.sleep(2)
        else:
            print("\n[CAR] wakeup is INVALID\n")


if __name__ == "__main__":
    main()
