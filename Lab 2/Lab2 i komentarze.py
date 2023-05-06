import numpy as np
import matplotlib.pyplot as plt

resolution = 256						#Deklarujemy rozdzielczość obrazu resolution na 256
size = 32
depth = 2							#Deklarujemy 2-bitową głębię bitową obrazu depth
drange = (-1, 1)						#Określamy zakres sensora drange na (-1, 1)
n_iter =  256							#Deklarujemy liczbę iteracji procedury akwizycji n_iter na 256
N = np.power(2, depth) - 1					#Wyliczamy górny limit zakresu dyskretnego N na 2 do potęgi głębi bitowej, pomniejszone o jeden
prober = np.linspace(start=0, stop=8*np.pi, num=resolution)	#Budujemy przestrzeń liniową prober z zakresu od 0 do ośmiu Pi o resolution elementach
sinus = np.sin(prober)						#Próbkujemy tą przestrzenią funkcję sinus, zapisując wynik próbkowania w wektorze prober
perfect_image = sinus[:, np.newaxis] * sinus[np.newaxis:]	#Budujemy macierz perfect_image jako iloczyn dwóch wektorów prober
n_matrix = np.zeros(perfect_image.shape)			#Inicjalizujemy macierze n_matrix i o_matrix, jako struktury dwuwymiarowe o kształcie macierzy perfect_image, składające się z samych zer
o_matrix = np.zeros(perfect_image.shape)

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))

for i in range (n_iter):					#pętla n_iter razy
    noise = np.random.normal(0,1,size=(resolution,resolution))	#Generujemy szum noise z rozkładu normalnego o wartości oczekiwanej funkcji sinus
    n_image = np.add(perfect_image, noise)			#W zmiennej n_image przechowujemy sumę macierzy perfect_image i noise
    o_image = perfect_image					#W zmiennej o_image przechowujemy kopię macierzy perfect_image
    n_dimg = (n_image - drange[0]) / (drange[1] - drange[0])	#Macierze n_image i o_image, niezależnie, poddajemy kwantyzacji do zadanej przez depth głębi bitowej, a wyniki tej operacji zapisujemy w zmiennych n_dimg u o_dimg.
    o_dimg = (o_image - drange[0]) / (drange[1] - drange[0])
    n_dimg = np.clip(n_dimg, 0, 1)
    o_dimg = np.clip(o_dimg, 0, 1)

    n_dimg = np.rint(n_dimg * N)
    o_dimg = np.rint(o_dimg * N)

    n_matrix = n_matrix + n_dimg				#Do macierzy n_matrix dodajemy obraz cyfrowy n_dimg, a do macierzy o_matrix, obraz cyfrowy o_dimg
    o_matrix = o_matrix + o_dimg

    axs[0][0].imshow(perfect_image, cmap='binary')		#pierwszy wiersz - obraz perfect_image
    axs[0][1].imshow(noise, cmap='binary')			#drugi wiersz - obraz szumu

    axs[1][0].imshow(o_dimg, cmap='binary')			#pierwszy wiersz - aktualny obraz cyfrowy o_dimg
    axs[1][1].imshow(n_dimg, cmap='binary')			#drugi wiersz - aktualny obraz cyfrowy n_dimg

    axs[2][0].imshow(o_matrix, cmap='binary')			#pierwszy wiersz - wynikowy dla akwizycji obraz o_matrix
    axs[2][1].imshow(n_matrix, cmap='binary')			#drugi wiersz - wynikowy dla akwizycji obraz n_matrix

plt.tight_layout()
plt.savefig('obraz.png')					#Na koniec każdej pętli itreracji akwizycji zapisujemy do pliku graficznego wizualizację o opisanej niżej charakterystyce
