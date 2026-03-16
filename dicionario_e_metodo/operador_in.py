capitais = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
}

pais = 'Brasil'

if pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')
else:
    print(f'Não há capital registrada pra o país {pais}')