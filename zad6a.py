# Zad. 6A - droga losowa, cena paliwa podawana przez użytkownika
import random

droga = random.randint(50, 1000)  # losowa liczba całkowita (km)
print("Wylosowana droga:", droga, "km")

spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa (zł/l): "))

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena_paliwa

print("Przewidywane zużycie paliwa:", round(zuzycie, 2), "l")
print("Szacowany koszt podróży:", round(koszt, 2), "zł")
