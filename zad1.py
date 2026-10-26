# Zad. 1A - typy wyników działań i znaczenie operatorów
dzialania = [
    ("1 + 2", 1 + 2, "dodawanie (int + int = int)"),
    ("1 + 4.5", 1 + 4.5, "dodawanie (int + float = float)"),
    ("3 / 2", 3 / 2, "dzielenie zmiennoprzecinkowe"),
    ("4 / 2", 4 / 2, "dzielenie zmiennoprzecinkowe "),
    ("3 // 2", 3 // 2, "dzielenie całkowite - odrzuca część ułamkową (zaokrągla w dół)"),
    ("-3 // 2", -3 // 2, "dzielenie całkowite zaokrągla w dół (w stronę -nieskończoności)"),
    ("11 % 2", 11 % 2, "reszta z dzielenia"),
    ("2 ** 10", 2 ** 10, "potęgowanie (int ** int = int)"),
    ("8 ** (1/3)", 8 ** (1 / 3), "potęgowanie ułamkowe = pierwiastek 3. stopnia, wynik float)"),
]

print("=== Zad. 1A ===")
for wyrazenie, wynik, opis in dzialania:
    print(f"{wyrazenie:12} = {wynik!r:20} typ: {type(wynik).__name__:6} -> {opis}")

# Zad. 1B - konwersje typów
konwersje = [
    ("int(3.0)", int(3.0), "float -> int, obcina część ułamkową"),
    ("float(3)", float(3), "int -> float, dodaje część ułamkową"),
    ('float("3")', float("3"), "tekst -> float (tekst musi wyglądać jak liczba)"),
    ("str(12.4)", str(12.4), "liczba -> tekst"),
    ("bool(0)", bool(0), "0 daje False; każda inna liczba daje True"),
]

print("\n=== Zad. 1B ===")
for wyrazenie, wynik, opis in konwersje:
    print(f"{wyrazenie:12} = {wynik!r:8} typ: {type(wynik).__name__:6} -> {opis}")
