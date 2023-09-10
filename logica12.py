#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e 
#um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do 
#desconto e o preço final do produto. 

preco = float(input('Qual o preço do protuto? '))
desconto = float(input('Qual a porcentagem do desconto? '))
des = preco *(desconto / 100)
total = preco - des
print('Desconto e de R${:.2f}, o total a se pagar e R${:.2f}'.format(des, total))