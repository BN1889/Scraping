	
import requests
from bs4 import BeautifulSoup
llamada = requests.get('https://www.starz.com/ar/es/movies')
print("El codigo de la llamada es ", llamada.status_code) 
from pandas import pandas as pd 

datos_soup = BeautifulSoup(llamada.text, 'html.parser')

titulos = datos_soup.find_all("p",class_="title")
	
lanzamiento = datos_soup.find_all("p",class_="text-body")

sinopsis = datos_soup.find_all("p",class_="is-truncated")

	
# Declaramos listas vacias
lista_titulos = []
lista_lanzamiento = []
lista_sinopsis = []
 
# Guardamos los titulos en lista_titulos
for dato in titulos:
    lista_titulos.append(dato.find('a').get_text())
 
# Guardamos el año de lanzamiento en lista_lanzamiento
for dato in lanzamiento:
    lista_lanzamiento.append(dato.get_text())
 
# Guardamos la sinopsis en lista_sinopsis
for dato in sinopsis:
    lista_sinopsis.append(dato.get_text())
    
	

 
df = pd.DataFrame({"titulos": lista_titulos, "lanzamiento": lista_lanzamiento,
                   "sinopsis": lista_sinopsis})
 
# removemos las /n del texto
df = df.replace('\n','', regex=True)
 
# removemos espacios multiples del texto
df = df.replace('\s+', ' ', regex=True)
 
# removemos espacios que esten al final o al principio del texto
df = df.apply(lambda x: x.str.strip())
 
#Imprimimos las primeras 5 lineas
print(df.head(5))


# link_accion = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/acci%C3%B3n"> Acción </a>'
# link_comedia = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/comedias"> Comedias </a>'
# link_crimenes = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/cr%C3%ADmenes-reales"> Crímenes Reales </a>'
# link_terror = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/de-terror"> De terror </a>'
# link_drama = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/dramas"> Dramas </a>'
# link_epoca = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/dramas-de-%C3%A9poca"> Dramas de época </a>'
# link_nuevos = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/nuevos-lanzamientos"> Nuevos lanzamientos </a>'
# link_romanticos = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/rom%C3%A1nticas"> Románticas </a>'
# link_dramatico = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/series-dram%C3%A1ticas-de-relaciones"> Series dramáticas de relaciones </a>'
# link_policiales = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/series-policiales"> Series policiales </a>'
# link_great = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/si-te-gusta-the-great"> Si te gusta The Great </a>'
# link_thriller = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/thriller"> Thriller </a>'
# link_ultima = '<a class="browse-menu-link d-block" href="/ar/es/browse/genre/%C3%BAltima-oportunidad"> Última oportunidad </a>'





datos_soup = BeautifulSoup(llamada.text, 'html.parser')

titulos = datos_soup.find_all("p",class_="title")
	
episodios = datos_soup.find_all("div",class_="links flexgrid")

temporadas = datos_soup.find_all("div",class_="season-selector d-flex")

	
# Declaramos listas vacias
lista_titulos = []
lista_episodios = []
lista_temporadas= []
 
# Guardamos los titulos en lista_titulos
for dato in titulos:
    lista_titulos.append(dato.find('a').get_text())
 
# Guardamos los episodios en lista_episodios 
for dato in episodios:
    lista_episodios.append(dato.get_text())
 
# Guardamos las temporadas en lista_temporadas
for dato in temporadas:
    lista_sinopsis.append(dato.get_text())
    
	

 
df = pd.DataFrame({"titulos": lista_titulos, "episodios": lista_episodios,
                   "temporadas": lista_temporadas})
 
# removemos las /n del texto
df = df.replace('\n','', regex=True)
 
# removemos espacios multiples del texto
df = df.replace('\s+', ' ', regex=True)
 
# removemos espacios que esten al final o al principio del texto
df = df.apply(lambda x: x.str.strip())
 
#Imprimimos las primeras 5 lineas
print(df.head(5))
