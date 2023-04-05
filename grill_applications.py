import time
from grill_client import GrillClient

def berechne_temperaturerhoehungsrate(grill_client, messungsintervall):
    # Erste Temperaturmessung
    start_temperatur = grill_client.get_temperatur()
    start_zeit = time.time()

    # Warte für das Messungsintervall
    time.sleep(messungsintervall)

    # Zweite Temperaturmessung
    end_temperatur = grill_client.get_temperatur()
    end_zeit = time.time()

    # Berechnung der Temperaturerhöhungsrate
    temperaturerhoehung = end_temperatur - start_temperatur
    zeitdifferenz = end_zeit - start_zeit
    rate = temperaturerhoehung / zeitdifferenz

    return rate


def berechne_temperatur_erhoehungsrate():
    grill_client = GrillClient('http://localhost:5007')
    messungsintervall = 10  # Messungsintervall in Sekunden

    # Zünde den Grill an und warte ein wenig, um die Temperatur steigen zu lassen
    grill_client.anzünden()
    time.sleep(20)

    # Berechne die Temperaturerhöhungsrate
    rate = berechne_temperaturerhoehungsrate(grill_client, messungsintervall)
    print(f"Temperaturerhöhungsrate: {rate} °C/s")


def regle_temperatur(grill_client, ziel_temperatur, toleranz=1):
    while True:
        aktuelle_temperatur = grill_client.get_temperatur()
        temperatur_diff = ziel_temperatur - aktuelle_temperatur

        # Überprüfe, ob die Temperatur innerhalb der Toleranzgrenzen liegt
        if -toleranz <= temperatur_diff <= toleranz:
            print(f"Zieltemperatur erreicht: {aktuelle_temperatur} °C")
            break

        # Steuere den Grill basierend auf der Temperaturdifferenz
        if temperatur_diff > 0:
            grill_client.ventilator_an()
            grill_client.luftzufuhr_auf()
        else:
            grill_client.ventilator_aus()
            grill_client.luftzufuhr_zu()

        # Warte 5 Sekunden, bevor die nächste Anpassung vorgenommen wird
        time.sleep(5)

def starte_grill_and_regel_temperatur():
    grill_client = GrillClient('http://localhost:5007')
    ziel_temperatur = 250  # Zieltemperatur in °C

    # Zünde den Grill an
    grill_client.anzünden()
    # time.sleep(20)

    # Regel die Temperatur des Grills
    regle_temperatur(grill_client, ziel_temperatur)


if __name__ == "__main__":
    starte_grill_and_regel_temperatur()
