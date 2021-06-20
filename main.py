from encrypt import szyfrowanie, deszyfrowanie
import sys


class main:
    def menu():
        off = 1
        while off != 0:
            opr = input("Wybierz: (szyfrowanie, deszyfrowanie, wyjscie): ")
            if opr == "szyfrowanie":
                napis = input("Podaj napis do operacji: ")
                print("Zaszyfrowany napis: " + szyfrowanie(napis))
                break
            elif opr == "deszyfrowanie":
                napis = input("Podaj napis do operacji: ")
                print("Odszyfrowany napis: " + deszyfrowanie(napis))
                break
            elif opr == "wyjscie":
                sys.exit("")
            else:
                print("Bledna operacja!")

    menu()
