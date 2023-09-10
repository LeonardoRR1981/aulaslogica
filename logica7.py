s1 = ('Linguagem de programação:' '\nPython ' + '-' * 5 + ' C ' + '-' * 5 + '-' + ' Java ' + '-' * 5 + ' PHP ' ) 
print(s1)

nota = 9.3
materia = 'Algoritimo'
media = 'Sua media e %.2f na materia %s' % (nota, materia)
print(media)

nota = 9.3
materia = 'Algoritimo'
media = 'Sua media e {} na materia {}'.format(nota, materia)
print(media)
