import requests

class GrillClient:
    def __init__(self, base_url):
        """
        Erstellt ein GrillClient-Objekt, um mit der Flask-Applikation zu interagieren und den Grill zu steuern.

        :param base_url: Die Basis-URL der Flask-Applikation (z.B. 'http://localhost:5007')
        """
        self.base_url = base_url

    def anzünden(self):
        """Zündet den Grill an."""
        requests.post(f'{self.base_url}/api/anzünden')

    def ventilator_an(self):
        """Schaltet den Ventilator an."""
        requests.post(f'{self.base_url}/api/ventilator_an')

    def ventilator_aus(self):
        """Schaltet den Ventilator aus."""
        requests.post(f'{self.base_url}/api/ventilator_aus')

    def luftzufuhr_zu(self):
        """Schließt die Luftzufuhr."""
        requests.post(f'{self.base_url}/api/luftzufuhr_zu')

    def luftzufuhr_auf(self):
        """Öffnet die Luftzufuhr."""
        requests.post(f'{self.base_url}/api/luftzufuhr_auf')

    @property
    def temperatur(self):
        """Gibt die aktuelle Temperatur des Grills zurück."""
        return self.get_temperatur()

    @property
    def grill_status(self):
        """Gibt den aktuellen Status des Grills zurück."""
        return self.get_grill_status()

    def get_temperatur(self):
        """Gibt die aktuelle Temperatur des Grills zurück (klassische Getter-Methode)."""
        response = requests.get(f'{self.base_url}/api/grill_status')
        return response.json()['temperatur']

    def get_grill_status(self):
        """Gibt den aktuellen Status des Grills zurück (klassische Getter-Methode)."""
        response = requests.get(f'{self.base_url}/api/grill_status')
        return response.json()
