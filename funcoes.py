from os import system
system('cls')

continuar = ''

try:
    while continuar.upper() != 'X':

        def soma(a,b):
            try:
                print(f'A soma entre os números é de: {a+b}')
            except:
                print('erro, sei lá.')
        def subtracao(a,b):
            try:
                print(f'A subtração entre os números é de: {a-b}')
            except:
                print('erro, sei lá.')
        def divisao(a,b):
            try:
                print(f'A divisão entre os números é de: {a / b}')
            except ZeroDivisionError as erro:
                print('Deu erro. Tentou divir por 0 né?')

        def multiplicacao(a,b):
            try:
                print(f'A divisão entre os números é de: {a * b}')
            except:
                print('erro, sei lá.')

        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('Informe o segundo número: '))

        opcao = int(input('''
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        Escolha uma opção acima: 
        '''))

        if opcao == 1:
            soma(num1, num2)
        elif opcao ==2:
            subtracao(num1, num2)
        elif opcao == 3:
            multiplicacao(num1, num2)
        elif opcao == 4:
            divisao(num1, num2)
        else:
            print('Opção invalida')

        continuar = input('Tecle qualquer tecla para continuar ou X para sair').upper()
except ValueError:
    print('Rapaz, algo deu errado ai, eu só não sei o que foi. Verificou se colocou números? (pode ter dado espaço sem querer também)')

    