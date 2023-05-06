# Instrukcja laboratoryjna

## Lista narzędzi niezbędnych do realizacji zadania

- `numpy`
- `matplitlib.pyplot`
- funkcja `rectangle` z modułu `skimage.draw`
- funkcja `rotate` z modułu `skimage.transform`
- funkcje `convolve2d` i `medfilt` z modułu `scipy.signal`

## Problem

Zadaniem zawartym w dzisiejszej instrukcji będzie przygotowanie narzędzia, które z wykorzystaniem operacji konwolucji za pomocą operatorów Sobel S1 i S3 pozwalają na wyrównanie do osi obrazu ilustracji składającej się z prostych figur geometrycznych.

## Ścieżka przetwarzania

W ramach laboratorium proszę przygotować skrypt, który realizuje następującą ścieżkę przetwarzania:

### Przygotowanie danych

- Wygeneruj obraz cyfrowy `entry_img` pomijający kwantyzację, składający się z wartości zmiennoprzecinkowych, o wymiarach `(256, 256)` pikseli. Przypominam, że w zmiennoprzecinkowej reprezentacji obrazu, wartości jego intensywności powinny zawierać się w przedziale `(0., 1.)`.
- Wykorzystując funkcję `rectangle()` wyrysuj w nim trzy prostokąty:
	- Rozciągający się od punktu `(32,32)` do `(92,92)`.
	- Rozciągający się od punktu `(92,92)` do `(128,128)`.
	- Rozciągający się od punktu `(128,128)` do `(144,144)`.
- Wynikowo otrzymasz poniższy obraz.

![figure_1](https://user-images.githubusercontent.com/904399/142221598-aee3e445-eb35-4d47-8c73-872fe765ca8a.png)


- Z rozkładu jednostajnego wylosuj kąt obrotu ilustracji, mieszczący się w przedziale `(-20, 20)`.
- Za pomocą funkcji `rotate` obróć obraz o wylosowany kąt.
- Wynikowo otrzymasz obraz `rot_img` zbliżony do poniższego.

![figure_2](https://user-images.githubusercontent.com/904399/142221631-b4ce2129-5d02-4a5c-ae38-50cdc3cda66e.png)


### Definicja parametrów przetwarzania

- W zmiennych zdefiniuj jądra konwolucji S1 i S3 [operatora Sobel](https://pl.wikipedia.org/wiki/Sobel). Służą one do detekcji krawędzi pionowych i poziomych obrazu, działając w sposób zbliżony do efektu pasm Macha.
- Jako przestrzeń liniową zainicjalizuj wektor przeszukiwanych kątów obrotu `angles` w 50 kwantach z zakresu od -30 do 30 stopni. Pamiętaj, że funkcja `rotate` do obrotu przyjmuje właśnie stopnie, a więc przeliczenie jednostek kąta nie będzie potrzebne.
- Przygotuj dwa inicjalizowane zerami wektory na pomiary (`abssums_s1` i `abssums_s2`), dla każdego z przekształceń, również o 50 elementach.

### Pętla przetwarzania

W każdej iteracji pętli przetwarzania wyrysuj wizualizację zbliżoną do poniższej, aby na bieżąco zweryfikować poprawność obliczeń. Znajdują się na nim.

- obraz oryginalny [0,0]
- obraz po losowej rotacji początkowej [0,1]
- obraz po aktualnej rotacji kompensującej [1,0]
- obraz [1,0] po konwolucji S1 [1,1]
- wykres wartości pomiarów [2,0]
- obraz [1,0] po konwolucji S3 [2,1]

![foo](https://user-images.githubusercontent.com/904399/142221667-0ad1b71e-8e81-4b4a-8701-092a6b214d10.png)


Procedurę przetwarzania zrealizuj w pętli for dla każdego kąta ze zmiennej `angles`.

- Do zmiennej `out_img` zapisz obraz `rot_img` obrócony o zadany powtórzeniem pętli kąt.
- Funkcją `convolve2d` dokonaj równoległej konwolucji obrazu `out_img` jądrem S1 i S3, wyniki zapisując do osobnych zmiennych.
- Dla obu obrazów po konwolucji dokonaj pomiaru będącego sumą wartości bezwzględnych ich intensywności, zapisując wyniki na odpowiednich pozycjach wektorów `abssums_s1` i `abssums_s2`.

### Identyfikacja optymalnego kąta obrotu

- Dla każdego z wektorów `abssums` odnajdź indeks minimalnej wartości i wyznacz lokalny `best_angle` jako koresponującą z nim wartość wektora `angles`.
- Wyznacz globalny `best_angle` jako średnią z obu lokalnych. To właśnie zidentyfikowany, optymalny kąt obrotu.
- Wyznacz obraz końcowy `final_img`, obracając obraz `rot_img` o kąt `best_angle`.
- Za pomocą funkcji `imsave` zapisz:
	- jako obraz `baz.png` - obraz finalny `final_img`
	- jako obraz `bar.png` - obraz barwny, którego kanałami będą kolejno:
		- czerwonym - obraz wejściowy `entry_img`,
		- zielonym - obraz końcowy `final_img`,
		- niebieskim - obraz zniekształcony `rot_img`.

Wynikowo otrzymasz obrazy zbliżone do poniższych. Na ich podstawie wyjaśnij, co na obrazie oznacza:
- kolor biały,
- kolor niebieski,
- kolor żółty,
- kolory czerwony i zielony.

![baz](https://user-images.githubusercontent.com/904399/142221695-0b12d302-d858-4cb1-8204-b4b3f758de84.png)
![bar](https://user-images.githubusercontent.com/904399/142221711-a69a605e-32fe-482d-aee8-e439f5832cee.png)
