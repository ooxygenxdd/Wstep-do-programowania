# Zad. 6B - to samo co 6A, ale z f-stringami
import random

droga = random.randint(50, 1000)
print(f"Wylosowana droga: {droga} km")

spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa (zł/l): "))

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena_paliwa

print(f"Przewidywane zużycie paliwa: {zuzycie:.2f} l")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")
