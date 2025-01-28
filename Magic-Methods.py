class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __len__(self):
        return self.ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition ist nur zwischen Auto-Objekten möglich.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraktion ist nur zwischen Auto-Objekten möglich.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplikation ist nur zwischen Auto-Objekten möglich.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return False

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return False

if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    # __len__
    print(len(a1))  # 50

    # __add__, __sub__, __mul__
    print(a1 + a2)  # 110
    print(a2 - a1)  # 10
    print(a1 * a2)  # 3000

    # Vergleichsoperatoren
    print(a1 == a2)  # False __eq__
    print(a1 < a2)   # True __lt__
    print(a1 > a2)   # False __gt__

    # Fehlerbehandlung
    try:
        print(a1 + 10)  # TypeError
    except TypeError as e:
        print(e)
