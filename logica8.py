comida = 'Macarrão'
ano = 1981
div = 1981 / 42
res = 'Minha comida preferida e %s, eu nasci no ano de %i, %i' %(comida, ano, div)
print(res)

comida = 'Macarrão'
ano = 1981
div = 1981 / 42
res = 'Minha comida preferida e {}, eu nasci no ano de {}, {:.2f}.'.format(comida, ano, div)
print(res)
