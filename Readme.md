Anna Matyjewicz i projekt zaliczeniowy nr 1

Pliki dostępne w repozytorium na GitHub pod adresem: https://github.com/Astghik1319/python1

Opis programu:
Moduł encrypt.py zawiera dwie funckje:
funkcja szyfrowanie, która przyjmuje zadany tekst, zamienia go na małe litery i zamienia według słownika szyfr_dict a następnie zwraca zaszyfrowany napis
funkcja deszyfrowanie, która przyjmuje zadany tekst, zamienia go na małe litery i zamienia według słownika deszyfr_dict a następnie zwraca zaszyfrowany napis

Program main.py:
Po uruchomieniu programu rozpoczyna się pętla while i wyświetla się komunikat z prośbą o wybranie typu operacji.
Wybranie operacji szyfrowanie wyświetla komunikat, aby podać tekst do zaszyfrowania, szyfruje go za pomocą funckji szyfrowanie znajdujacej się w pliku encrypt.py, wyświetla zaszyfrowany napis i przerywa pętlę.
Wybranie operacji deszyfrowanie prosi wyświetla komunikat, aby podać tekst do zaszyfrowania, szyfruje go za pomocą funckji deszyfrowanie znajdujacej się w pliku encrypt.py, wyświetla rozszyfrowany napis i przerywa pętlę.
Wybranie operacji wyjscie kończy działanie programu.
Podanie błędnej operacji sprawi, że na ekranie pojawi się komunikat "Bledna operacja!" i pętla wykona się jeszcze raz. Przy podawaniu błędnych operacji pętla działa w nieskończoność. 

Kod źródłowy został sprawdzony na zgodność z dokumentacją PEP8 przy pomocy programu flake8