class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        Osoba.__init__(self, imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        Osoba.__init__(self, imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


class PracujacyStudent(Pracownik, Student):
    def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
        Pracownik.__init__(self, imie, wiek, stawka, liczba_godzin)
        Student.__init__(self, imie, wiek, stypendium)

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin + self.stypendium


class StudentPracujacy(Student, Pracownik):
    def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
        Pracownik.__init__(self, imie, wiek, stawka, liczba_godzin)
        Student.__init__(self, imie, wiek, stypendium)

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin + self.stypendium


class Dupa(PracujacyStudent, StudentPracujacy):
    pass


if __name__ == '__main__':
    dupa = Dupa()
    dupa.pokaz_finanse()
    # os1 = Osoba("Henryk", 54)
    # os2 = Pracownik("Monika1", 24, 9.5, 70)
    # os3 = Student("Monika2", 24, 550)
    # os4 = PracujacyStudent("Monika3", 24, 9.5, 70, 550)
    # # print(os2.pokaz_finanse())
    # # print(os3.pokaz_finanse())
    # print(os4.pokaz_finanse())
    # print(os1)
    # print(os2)
    # print(os3)
    # print(os4)
