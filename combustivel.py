gasolina = float(input('Digite o preço da gasolina \n'))

alcool = float(input('Digite o preço do alcool \n'))

resultado= alcool/ gasolina *(70/100)*100

print(resultado)

if resultado <70:
    print('Compensa a gasolina')
    
elif  resultado >70:
    print('Compensa o alcool')
    
elif  resultado == 70:
    print('Tanto faz')

consultar = input ('Deseja fazer uma nova consulta ?')


