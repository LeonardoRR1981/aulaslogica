#Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, 
#de horas, de minutos e de segundos. Calcule o total de segundos resultante e 
#imprima na tela para o usuário.


dias = int(input('Escolha uma quantidade de dias: '))
horas = int(input('Escolha as horas: '))
minu = int(input('Escolha os minutos: '))
seg = int(input('Escolha os segundos: '))
# 1 dia = 24 horas , 1 hora = 60 minutos , 1 minuto = 60 segundos 
total = seg + (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minu * 60)
print('O total de segundos e: {}'.format(total))