#Desafio Dev

usr_input = input("Qual o Codigo De Usuario ? ")

if usr_input == '1234' :
    while True :
        senha_input = int(input('Digite a Senha Do Usuario:  '))
        if senha_input == 9999:
            print('Acesso permitido')
            exit()
        else:
            print('Senha Incorreta ! ')
            print('\n1 - Tentar Novamente \n\n0 - Encerrar Sistema\n')
            Tentar_nov = int(input('Digite uma Opção: '))

            if Tentar_nov == 0:
                    exit()

            if Tentar_nov > 1:
                print('Opção Invalida ! ')
                print('Encerrando...')
                exit()

else:
    print('Usuario Invalido !')
    exit()

#Desafio Completo :)
