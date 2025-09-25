class ters_cevirme():
    def __init__(self, liste):
        self.liste = liste
        self.index = len(liste) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        deger = self.liste[self.index]
        self.index -= 1
        return deger


ters = ters_cevirme([1, 2, 3, 4])

for i in ters:
    print(i)   # 4, 3, 2, 1
