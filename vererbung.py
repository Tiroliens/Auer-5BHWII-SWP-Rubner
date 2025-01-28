class Schule:
    def __init__(self, name, adresse):
        # a) Neuer Fehler und behebbare Fehler
        if not isinstance(name, str):
            print("Fehler: Name der Schule muss ein String sein. Standardwert 'Unbekannt' wird verwendet.")
            name = "Unbekannt"  # Behebung des Fehlers
        if not isinstance(adresse, str):
            raise ValueError("Adresse muss ein String sein.")  # Fehler, der nicht behebbar ist
        self.name = name
        self.adresse = adresse

    def beschreibung(self):
        return f"Die Schule {self.name} befindet sich in der {self.adresse}."


class Wirtschaft(Schule):
    def __init__(self, name, adresse, projekte):
        super().__init__(name, adresse)
        # a) Neuer-Fehler, aber behebbar
        if not isinstance(projekte, list):  # Hier wird überprüft, ob projekte eine Liste ist.
            print("Fehler: Projekte müssen als Liste übergeben werden. Ein Standardprojekt wird hinzugefügt.")
            projekte = ["Kein Projekt"]  # Behebung des Fehlers
        self.projekte = projekte
        # b) Hochblubber-Fehler, behebbar
        if not isinstance(name, str):
            print("Fehler: Name der Schule muss ein String sein. Standardwert 'Unbekannt' wird verwendet.")
            name = "Unbekannt"  # Behebung des Fehlers

    def zeige_projekte(self):
        return f"In der Abteilung Wirtschaft werden folgende Projekte durchgeführt: {', '.join(self.projekte)}."


class Elektronik(Schule):
    def __init__(self, name, adresse, labors):
        super().__init__(name, adresse)
        # c) Neuer Fehler, nicht behebbar
        if not isinstance(labors, int) or labors < 0:
            raise ValueError("Labors muss eine positive Ganzzahl sein.")  # Schwerwiegender Fehler, nicht behebbar
        self.labors = labors

    def labor_info(self):
        return f"Die Abteilung Elektronik hat {self.labors} spezialisierte Labors."


class Maschinenbau(Schule):
    def __init__(self, name, adresse, werkstätten):
        super().__init__(name, adresse)
        # d) Hochblubber-Fehler, nicht behebbar
        if not isinstance(werkstätten, int) or werkstätten < 0:
            raise ValueError("Werkstätten muss eine positive Ganzzahl sein.")  # Fehler blubbert nach oben
        self.werkstätten = werkstätten

    def werkstatt_info(self):
        return f"Die Abteilung Maschinenbau hat {self.werkstätten} Werkstätten für praktische Übungen."


# Testzeilen mit Fehlerbehandlung
if __name__ == "__main__":
    try:
        # Gültige Objekte erstellen
        htl = Schule("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck")
        wirtschaft = Wirtschaft("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck", ["Marketing", "Unternehmensführung"])
        elektronik = Elektronik("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck", 5)
        maschinenbau = Maschinenbau("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck", 3)

        # Gültige Methodenaufrufe
        print(htl.beschreibung())
        print(wirtschaft.zeige_projekte())
        print(elektronik.labor_info())
        print(maschinenbau.werkstatt_info())

        # Fehlerhafte Objekte testen
        print("\nTest: Fehler bei der Initialisierung von Wirtschaft")
        fehlerhafte_wirtschaft = Wirtschaft("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck", "Kein Projekt")  # Sollte Fehler erzeugen

    except ValueError as e:
        print(f"Fehler: {e}")

    try:
        print("\nTest: Fehler bei der Initialisierung von Elektronik")
        fehlerhafte_elektronik = Elektronik("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck", -1)  # Sollte ValueError werfen

    except ValueError as e:
        print(f"Fehler: {e}")

    try:
        print("\nTest: Fehler bei der Initialisierung von Maschinenbau")
        fehlerhafte_maschinenbau = Maschinenbau("HTL Anichstraße", "Anichstraße 26, 6020 Innsbruck", "Drei")  # Sollte ValueError werfen

    except ValueError as e:
        print(f"Fehler: {e}")

    try:
        print("\nTest: Fehler bei der Initialisierung von Schule")
        fehlerhafte_schule = Schule(123, "Anichstraße 26, 6020 Innsbruck")  # Sollte ValueError werfen

    except ValueError as e:
        print(f"Fehler: {e}")
