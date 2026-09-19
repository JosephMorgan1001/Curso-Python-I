from os import system
system('cls')

while True:
    try:
        #Calculadora de IMC
        peso = float(input('Digite seu peso (kg): ').replace(',', '.'))
        

        altura = float(input('Digite sua altura: ').replace(',', '.'))
        imc = peso / (altura * altura)
    
        if imc < 18.5:
            print(f'Seu IMC é {imc:.2f} você tá abaixo do peso')
        elif imc >= 18.5 and imc < 24.9:
            print(f'Seu IMC é {imc:.2f} você tá normal')
        elif imc >= 25 and imc < 29.9:
            print(f'Seu IMC é {imc:.2f} você tá com obesidade classe 1')
        elif imc >=30 and imc < 34.9:
            print(f'Seu IMC é {imc:.2f} você tá com obesidade classe 2')
        elif imc >= 35 and imc < 39.9:
            print(f'seu IMC é {imc:.2f} você tá com obesidade classe 3')
        elif imc >= 40:
            print(f'Seu IMC é {imc:.2f} você tá com obesidade classe 4')
        else:
            print('Erro, tente novamente')
        break
    except ValueError:
        print('Digite apenas números, por favor')
