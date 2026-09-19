def calculadora():
    print('1 - adição')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    esc = input('Digite uma opção acima: ')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if esc == '1':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif esc == '2':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif esc == '3':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif esc == '4':
        print(f'{num1} / {num2} = {num1 / num2}')
calculadora()