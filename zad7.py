# Zad. 7 - równanie liniowe ax + b = 0
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a != 0:
    x = -b / a
    print(f"Rozwiązanie: x = {x}")
elif b == 0:
    print("Równanie tożsamościowe - nieskończenie wiele rozwiązań.")
else:
    print("Równanie sprzeczne - brak rozwiązań.")
