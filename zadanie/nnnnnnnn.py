from pathlib import Path
PLIK = Path("dane.txt")

def www(imie: String, nazwisko: String):
    return (imie, nazwisko)


    while True:
        print("MENU:")
        print("1. Wyświetl Listę Uczniów")
        print("2. Posortuj listę alfabetycznie")
        print("3. Usuń ucznia z listy")
        print("4. Zkończ Program")

        wybor = input("\nWybierz: ")
        if wybor == 1:
            print("\nLisa danych:")
                with open(PLIK, "r", encoding="utf-8") as f:
                for imie, nazwisko in enumerate(f, start=1):
            print(f"{imie}. {nazwisko.strip()}")
        elif wybor == 2:
            x.sorted(PLIK)
            print(x)
        elif wybor == 3:
           x.pop()
           print(x)
        elif wybor == 4:
            break;