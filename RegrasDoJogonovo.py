from random import shuffle, randint
from time import sleep

listageral = list()
listatemp = list()
listaprimeirojogo = list()
listatimes = list()
while True:
    print("""
\033[1;32m[1] CADASTRAR ATLETAS
[2] STATUS DA PARTIDA
[3] PRIMEIRA PARTIDA
[4] FINALIZAR PELADA\n\033[m""")



    opcao = str(input('\033[1;30mDigite uma opção:\033[m '))

    while opcao not in '1234':
        print('ERRO!!!!')

        opcao = str(input('\033[1;30mDigite uma opção válida:\033[m '))

# OPÇÃO ABAIXO SE REFERE AO MENU PRINCIPAL E ABAIXO SEGUE O CADASTRO DOS ATLETAS E DEFINIÇÃO DOS TIMES

    if opcao == '1':

        while True:

            opscadastro = str(input('\033[1;30mDeseja cadastrar atletas: [S/N]:\033[1;30m ')).strip().upper()[0]

            if opscadastro == 'N':
                break

            nome = str(input('\033[1;30mDigite o nome do atleta:\033[m ')).upper().strip()
            print(f'O jogador \033[1;36m{nome}\033[m foi cadastrado....')

            while opscadastro not in 'SN':
                opscadastro = str(input('\033[1;30mDigite uma opção válida: [S/N]:\033[m ')).strip().upper()[0]

            listageral.append(nome)
            listatemp.append(nome)

            if len(listatemp) == 4:
                listatimes.append(listatemp[:])

            if len(listatemp) == 4:
                listatemp.clear()

# OPÇÃO ABAIXO SE REFERE AO MENU PRINCIPAL E REGE AS REGRAS DA PARTIDA GERANDO UM MENU DE OPÇÕES

    if opcao == '2':
        while True:
            print("""
\033[1;34m[1] EXPULSO
[2] SUSPENSO
[3] EMPATE
[4] RESULTADO
[5] ENCERRAR A PARTIDA\n\033[m""")

            opspartida = str(input('\033[1;30mDigite uma opção:\033[m '))

            if opspartida == '1':

                while True:

                    for p, v in enumerate(listatimes):

                        if p == 0:
                            amarelo = v

                        if p == 1:
                            azul = v

                    if len(listatimes) == 0:
                        print('\033[31mTIMES A SER DEFINIDOS!\033[m')
                    else:
                        print(f"0 - O time amarelo {amarelo}")
                        print(f'1 - O time azul {azul}')

                    definir = str(input('\033[1;30mDeseja sair da partida [S/N]:\033[m ')).strip().upper()[0]

                    while definir not in 'SN':
                        definir = str(input('\033[1;30mDigite uma opção válida [S/N]:\033[m ')).strip().upper()[0]

                    if definir == 'S':
                        break

                    opstime = str(input('\033[1;30mDigite o codigo do time [O-1]:\033[m '))

                    if opstime == '0':

                        for p, v in enumerate(amarelo):
                            print(f"{p+1} - {v}")

                    elif opstime == '1':

                        print(f'{p+1} - {v}')

                    opsjogador = str(input('Digite o código do jogador: [1-2-3-4]: '))

                    while opsjogador not in '1234':

                        opsjogador = str(input('Digite uma opção válida: [1-2-3-4]: '))

                    opsjogador = int(opsjogador)

                    if opstime == '0':

                        del amarelo[opsjogador]
                        del listageral[opsjogador]

                    else:

                        del azul[opsjogador]
                        del listageral[opsjogador]

                    print(listatimes)

            if opspartida == '2':

               while True:

                    for p, v in enumerate(listatimes):

                        if p == 0:
                            amarelo = v

                        if p == 1:
                            azul = v
                    if len(listatimes) == 0:
                        print('\033[31mTIMES A SER DEFINIDOS!\033[m')
                    else:
                        print(f"0 - O time amarelo {amarelo}")
                        print(f'1 - O time azul {azul}')

                    definirtimes = str(input('Deseja sair da partida: [S/N] ')).strip().upper()[0]

                    while definirtimes not in 'SN':

                        definirtimes = str(input('Digite uma opção válida: [S/N]')).strip().upper()[0]

                    if definirtimes == 'S':

                        break

                    opsipose2 = str(input('Digite o codigo do time [O-1]: '))

                    if opsipose2 == '0':

                        for p, v in enumerate(amarelo):

                            print(f"{p} - {v}")

                    elif opsipose2 == '1':

                        print(f'{p} - {v}')

                    opsjogadorsuspenso = int(input('Digite o código do jogador: [O-1-2-3-4]: '))

                    if opsipose2 == '0':

                        for p, v in enumerate(amarelo):

                            if p == opsjogadorsuspenso:

                                print(f'O JOGADOR {v} CUMPRIRÁ 2 MINUTOS FORA!')

                    else:

                        for p, v in enumerate(azul):

                            if p == opsjogadorsuspenso:

                                print(f'O JOGADOR {v} CUMPRIRÁ 2 MINUTOS FORA!')

            if opspartida == '3':
                sorteio = randint(0, 5)

                if sorteio % 2 == 0:
                    print('Amarelo')
                else:
                    print('Azul')

                golamarelo = golazul = int()
                amarelo = listatimes[0]
                azul = listatimes[1]

                while True:


                    opstime = str(input('Digite o código do time batedor [O-1]: '))

                    if opstime == '0':

                        for p, v in enumerate(amarelo):
                            print(f'{p} - {v}')
                        opsjogadoramarelo = int(input('Digite o código do jogador: '))
                        golamarelo = int(input(f'O jogador {amarelo[opsjogadoramarelo]} Converteu: '))

                    else:

                        for p, v in enumerate(amarelo):

                            print(f'{p} - {v}')

                        opsjogadorazul = int(input('Digite o código do jogador: '))
                        golazul = int(input(f'O jogador {azul[opsjogadorazul]} Converteu: '))

                    if golamarelo == 1 and golazul == 0:

                        for p, v in enumerate(amarelo):
                            for j, h in enumerate(listageral):
                                if v == h:
                                    del listageral[j]
                        print('O time amarelo venceu a partida')
                        break

                    elif golamarelo == 0 and golazul == 1:

                        for p, v in enumerate(azul):
                            for j, h in enumerate(listageral):
                                if v == h:
                                    del listageral[j]
                        print('O time azul venceu a partida')
                        break


    # OPÇÃO ABAIXO SE REFERE AO MENU PRINCIPAL E ABAIXO SEGUE A REGRA REFERENTE A PRIMEIRA PARTIDA

    if opcao == '3':

        while True:

            opscadastro = str(input('Deseja cadastrar atletas: [S/N] ')).strip().upper()[0]

            if opscadastro == 'N' or len(listaprimeirojogo) == 8:
                sleep(1)
                print('\033[1;36mTimes definidos............\033[m', end='')

                break

            nome = str(input('Nome dos 08 primeiros: ')).upper().strip()
            print(f'O jogador \033[1;36m{nome}\033[m foi cadastrado....')

            while opscadastro not in 'SN':

                opscadastro = str(input('Digite uma opção válida: [S/N] ')).strip().upper()[0]

            listaprimeirojogo.append(nome)
            listageral.append(nome)

            if len(listaprimeirojogo) == 8:

                shuffle(listaprimeirojogo)
                for p, v in enumerate(listaprimeirojogo):
                    if p < 4:
                        listatemp.append(v)
                listatimes.append(listatemp[:])
                listatemp.clear()

            if len(listaprimeirojogo) == 8:
                shuffle(listaprimeirojogo)
                for p, v in enumerate(listaprimeirojogo):

                    if p > 3 and p <= 8:

                        listatemp.append(v)
                listatimes.append(listatemp[:])
                listatemp.clear()

            print(listaprimeirojogo)

    if opcao == '4':

        pergunta = str(input('\033[1;31mVOCÊ TEM CERTEZA???? [S/N]:\033[m ')).upper().strip()[0]

        while pergunta not in 'SN':

            pergunta = str(input('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA!!! [S/N]:\033[m ')).upper().strip()[0]

        if pergunta == 'S':
            sleep(1)
            print('\033[1;31mFINALIZANDO A PELADA ATÉ A PROXIMA.........\033[m')
            break

