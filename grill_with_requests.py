import requests
import time

# Ersetzen Sie die URL durch die tatsächliche URL Ihres Flask-Servers
base_url = "http://localhost:5007/api/"

def start_grill():
    url = base_url + "anzünden"
    response = requests.post(url)
    if response.status_code == 200:
        print("Grill gestartet")
    else:
        print("Fehler beim Starten des Grills")

def get_grill_status():
    url = base_url + "grill_status"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Fehler beim Abrufen des Grillstatus")
        return None

if __name__ == "__main__":
    start_grill()
    while True:
        time.sleep(10)
        status = get_grill_status()
        if status:
            print(f"Temperatur: {status['temperatur']} °C")