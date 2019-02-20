from bs4 import BeautifulSoup

# A variável seguidores e seguindo deve 
# conter o bloco da tag <ul class="jSC57  _6xe7A">...</ul>

seguidores = ''
seguindo = ''

soup_seguindo = BeautifulSoup(seguindo, 'html.parser')
soup_seguidores = BeautifulSoup(seguidores, 'html.parser')

lista_seguindo_suja = soup_seguindo.find_all('div', class_='wFPL8 ')
lista_seguidores_suja = soup_seguidores.find_all('div', class_='wFPL8 ')

lista_seguindo = set([nome.get_text() for nome in lista_seguindo_suja])
lista_seguidores = set([nome.get_text() for nome in lista_seguidores_suja])

diferenca = lista_seguindo - lista_seguidores

print('-- Diferença de ' + str(len(diferenca)) + ' perfis. --')

for i in diferenca:
  print(i)