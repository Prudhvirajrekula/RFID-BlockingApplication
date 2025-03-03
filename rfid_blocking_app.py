import nfc
import time
import threading

def detect_rfid():
    """Function to detect RFID signals and alert the user."""
    try:
        clf = nfc.ContactlessFrontend('usb')  # Connect to an NFC reader
        while True:
            tag = clf.connect(rdwr={'on-connect': lambda tag: False})
            print("⚠ Unauthorized RFID Scan Detected! ⚠")
            print(f"Tag ID: {tag}")
            print("Take necessary precautions!")
            time.sleep(1)
    except Exception as e:
        print("Error: ", e)
    finally:
        clf.close()

if __name__ == "__main__":
    print("Starting RFID Blocking Application...")
    detection_thread = threading.Thread(target=detect_rfid)
    detection_thread.start()
