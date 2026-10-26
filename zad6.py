# Zad. 6 - zużycie paliwa i koszt podróży
droga = float(input("Podaj przejechaną drogę (km): "))
spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = 6.5  # zł/l

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena_paliwa

print("Przewidywane zużycie paliwa:", round(zuzycie, 2), "l")
print("Szacowany koszt podróży:", round(koszt, 2), "zł")
