"""
calculadora com while
"""

while True:
    numero1 = input('digite o primeiro número: ')
    operador = input('qual o tipo de operador: ')
    numero2 = input('digite o segundo número: ')

    numeros_validos = None

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
     numeros_validos = None

    if numeros_validos is None:
        print('um ou ambos os numeros são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador inválido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    print('realizando o cálculo')   

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}', num_1_float * num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}', num_1_float / num_2_float)
    else:
        print('isso nunca deveria chegar aqui')


    sair = input('quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break