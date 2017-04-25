import random
import math

NumCasas = 40  # Número de posições no tabuleiro.
DinheiroInicial = 1508  # Dinheiro inicial
NomeJogadores = ""  # Variavel com cada nome de jogador formatados em 50 espaços.
StatusJogadores = ""  # Variavel com status de cada jogador(Livre/Preso por x turnos) 0 = Livre, 1 = Preso por 1 turno, 2 = Preso por 2 turnos, 3 = Preso por 3 turnos, 4 = Falido.
PosicaoJogadores = ""  # Variavel com cada posição de jogador formatada em 2 espaços Ex : 00, 01, 02.
DinheiroJogadores = ""  # Variavel com cada dinheiro de jogador formatada em 5 espaços, possibilitando cada jogador a acumular 99999R$.
NomeCasas = ""  # Variavel com cada nome de casa formatada em 30 espaços.
Terrenos = ""  # Variavel com todos os terrenos, respectivos ids, preços e aluguel formatados em '00(ID)000(Preço)0000(Aluguel)'.
# IDs =  00 = Sem proprietario, 01 ~ 06 reservado a Jogadores, 07 = Ponto Partida, 08 = Imposto , 09 = Sorte Revés, 10 = Vá para prisão, 11 = Prisão, 12 = Lucros ou Dividendos, 13 = Parada Livre
# Devido à companhias em que paga-se o dado * x, se o aluguel for maior que 999, multiplica-se o dado pelos dois números mais significativos. Ex : 4000 = (2 * d6) * 40.
Sorte = ""  # Variavel com todas as frases de sorte formatadas em 82 espaços.
Reves = ""  # Variavel com todas as frases de revés formatadas em 82 espaços.
# Atribuição dos nomes de casa, terrenos, sorte e revés
NomeCasas = ("Ponto de Partida.             Leblon.                       Sorte Revés.                  " +
             "Av. Presidente Vargas.        Av. Nossa S. De Copabacana.   Companhia Ferroviária.        " +
             "Av. Brigadeiro Faria Lima.    Companhia de Viação.          Av. Rebouças.                 " +
             "Av. 9 de Julho.               Prisão.                       Av. Europa.                   " +
             "Sorte Revés.                  Rua Augusta.                  Av.Pacaembú.                  " +
             "Companhia de Táxi.            Sorte Revés.                  Interlagos.                   " +
             "Lucro ou Dividendo.           Morumbi.                      Parada Livre.                 " +
             "Flamengo.                     Sorte Revés.                  Botafogo.                     " +
             "Imposto de Renda.             Companhia de Navegação.       Av. Brasil.                   " +
             "Sorte Revés.                  Av. Paulista.                 Jardim Europa.                " +
             "Vá para a prisão.             Copacabana.                   Companhia de Aviação.         " +
             "Av. Vieira Souto.             Av. Atlântica.                Companhia de Taxi Aéreo.      " +
             "Ipanema.                      Sorte Revés.                  Jardim Paulista.              " +
             "Brooklin.                     ")

Terrenos = ("070000000001000006090000000000600002000600004002005000002400020002005000002200018002200018" +
            "110000000002000016090000000001800014001800014001504000090000000003500035120000000004000060" +
            "130000000001200008090000000001000006080000000001504000001600012090000000001400010001400008" +
            "100000000002600022002005000003200028003000026002005000003000026090000000002800024002600022")

Sorte = ("O serviço do Te Vi No Mackenzie está bombando. E a grana não é virtual!           " +
         "O preço da Mackejada subiu horrores. Mas quem recolhe é você!                     " +
         "O sistema de cola nas provas funciona que é uma maravilha.                        " +
         "Você fez uma pontinha num seriado de TV. Parabéns!                                " +
         "Você jura que não teve nada a ver com o sumiço do professor, mas...               " +
         "O seu período na esportiva expirou, mas esqueceram de cortar o desconto de atleta." +
         "Em sua caminhada para o Mack Fil, você encontrou dinheiro no chão.                ")

Reves = ("De quem foi a incrivel ideia de uniformizar a rapaziada com boné do Mackenzie?    " +
         "Você aproveitou o feriado para visitar um amigo na Região dos Lagos.              " +
         "Chegou o verão e o Mack Fil ta precisando de um novo ar condicionado.             " +
         "A patroa podia pegar mais leve na decoração do apartamento de Moema.              " +
         "A central de TV tá precisando de reparos e a Anatel não vai ajudar.               " +
         "O micreiro que fez os banners da Mackejada caprichou no degradê e no orçamento.   " +
         "O espetinho de lançamento do Maria Antônia ficou uma delícia. Já o preço...       ")

# Fim de atribuição de casas, terrenos, sorte e revés
NumJogadores = 0
while NumJogadores < 3 or NumJogadores > 6:
    print("Digite o número de jogadores.(De 3 à 6 jogadores)")
    NumJogadores = int(input())
for i in range(0, NumJogadores):
    NomeCorreto = False
    Nome = ""
    while not NomeCorreto:
        print("Insira o nome do " + str(i + 1) + "º jogador.")
        Nome = input()
        print("O nome do " + str(
            i + 1) + "º jogador será: " + Nome + ". Este nome está correto?([S] para Sim, [N] para Não")
        if input().lower() == "s":
            NomeCorreto = True
    while len(Nome) < 50:  # Formatando o nome em 50 caracteres.
        Nome += " "
    NomeJogadores += Nome
    StatusJogadores += "0"
    PosicaoJogadores += "00"
    DinheiroJogadores += "0" + str(DinheiroInicial)
    Nome = None
    NomeCorreto = None
FimDeJogo = False
while not FimDeJogo:
    Falidos = 0
    for i in range(0, NumJogadores):
        if StatusJogadores[i] != "4":  # Verificando se o jogador não faliu.
            Nome = NomeJogadores[(i * 50):((i + 1) * 50)].strip()
            Posicao = int(PosicaoJogadores[(i * 2):((i * 2) + 2)])
            Din = int(DinheiroJogadores[(i * 5):((i * 5) + 5)])
            print(Nome + ", é a sua vez.")
            if StatusJogadores[i] == "0":  # Verificando se o jogador está jogando ou está preso.
                Movimento = "."
                while Movimento != "":
                    print("Digite 1 para saber sua posição.")
                    print("Digite 2 para saber sua quantia de dinheiro.")
                    print("Digite 3 para ver suas propriedades.")
                    print("Pressione [ENTER] para jogar os dados.")
                    Movimento = input()
                    if Movimento == "1":
                        print(Nome + ", você encontra-se na " + str(Posicao) + "º posição do tabuleiro.")
                        print()
                    elif Movimento == "2":
                        print(Nome + ", você ainda tem R$" + str(Din))
                        print()
                    elif Movimento == "3":
                        Concatena = ""
                        for i2 in range(0, 360, 9):
                            if Terrenos[i2: i2 + 2] == "0" + str(
                                            i + 1):  # ID Correspondente ao dono do terreno = jogador atual
                                Concatena += NomeCasas[((i2 // 9) * 30): (((i2 // 9) + 1) * 30)] + "\r\n"
                        if Concatena != "":
                            print(Nome + ", você tem estes terrenos:")
                            print(Concatena)
                        else:
                            print(Nome + ", você ainda não tem terrenos.")
                            print()
                d6 = random.randint(1, 6)
                print("Você rodou " + str(d6) + " no primeiro dado.")
                Posicao += d6
                d62 = random.randint(1, 6)
                print("Você rodou " + str(d62) + " no segundo dado.")
                Posicao += d62
                if Posicao > NumCasas - 1:
                    Posicao -= NumCasas  # 39 = ultima casa. se der 41 significa que ele voltou pra casa 0
                    Din += 200
                    print("Você passou pelo ponto de partida e recebeu R$200, totalizando R$" + str(Din))
                TerrenoAtual = NomeCasas[Posicao * 30:(Posicao + 1) * 30]
                print("Você se encontra no terreno: " + TerrenoAtual)
                TerrenoAtual = Terrenos[Posicao * 9: (Posicao + 1) * 9]
                IDTerrenoAtual = TerrenoAtual[0:2]
                if IDTerrenoAtual == "00":  # Não pertence a ninguém.
                    ValorTerreno = int(TerrenoAtual[2:5])
                    print("Este terreno está vago e custa R$" + str(ValorTerreno) + ".")
                    if Din > ValorTerreno:
                        print("Deseja comprar o mesmo?([S] para Sim, [N] para não")
                        if input().upper() == "S":
                            Din -= ValorTerreno
                            print("Parabéns na compra de um novo terreno!")
                            Terrenos = Terrenos[0:Posicao * 9] + "0" + str(i + 1) + Terrenos[(Posicao * 9) + 2:]
                    else:
                        print("Mas infelizmente você não tem dinheiro suficiente para o comprar.")
                elif 0 < int(IDTerrenoAtual) < 7:  # Pertence a alguém.
                    Aluguel = int(TerrenoAtual[5:9])
                    IDTerrenoAtual = int(IDTerrenoAtual) - 1
                    DinDono = int(DinheiroJogadores[(IDTerrenoAtual * 5):((IDTerrenoAtual + 1) * 5)])
                    if Aluguel > 999:
                        Aluguel = (d6 + d62) * Aluguel // 100
                    print("Este terreno já tem dono, e você deve pagar R$" + str(
                        Aluguel) + " de aluguel a(o) " + NomeJogadores[
                                                         (IDTerrenoAtual * 50):((IDTerrenoAtual + 1) * 50)])
                    Din -= Aluguel
                    DinDono += Aluguel
                    DinDono = str(DinDono)
                    while len(DinDono) < 5:
                        DinDono = "0" + DinDono
                    DinheiroJogadores = DinheiroJogadores[0: IDTerrenoAtual * 5] + DinDono + DinheiroJogadores[
                                                                                             (IDTerrenoAtual * 5) + 5:]
                elif IDTerrenoAtual == "08":  # Imposto de renda
                    Din = Din * 0.9
                    print("Como taxa de impostos, você paga 10% do seu dinheiro ao governo, te deixando com R$" + str(
                        Din))
                elif IDTerrenoAtual == "09":  # Sorte ou Revés.
                    Frase = ""
                    if random.randint(1, 2) == 1:
                        print("SORTE")
                        Valor = random.randint(30, 100)
                        print("Você ganhou R$" + str(Valor) + ".")
                        Din += Valor
                        Frase = Sorte
                    else:
                        print("REVÉS:")
                        Valor = random.randint(15, 80)
                        print("Você perdeu R$" + str(Valor) + ".")
                        Din -= Valor
                        Frase = Reves
                    fRand = random.randint(0, 6)
                    print(Frase[fRand * 82:(fRand + 1) * 82])
                elif IDTerrenoAtual == "10":  # Vá para a prisão.
                    print(
                        "Você foi preso. Você ficará preso por até 3 partidas tentando tirar uma dupla nos dados. Se você não conseguir deverá pagar R$50 e será solto na 4ª partida.")
                    StatusJogadores = StatusJogadores[0: i] + "3" + StatusJogadores[i + 1:]
                    Posicao = 10
                elif IDTerrenoAtual == "11":  # Prisão.
                    print("Mas calma, você encontra-se apenas visitando a área.")
                elif IDTerrenoAtual == "12":  # Lucros ou Dividendos
                    Din = math.floor(Din * 1.1)
                    print("Você recebe 10% do seu dinheiro atual, totalizando R$" + str(Din))
            else:  # Jogador Preso
                print(Nome + ", você encontra-se preso por " + StatusJogadores[
                    i] + " turnos.Digite [ENTER] para jogar o primeiro dado.")
                input()
                d6 = str(random.randint(1, 6))
                print("Você tirou " + d6 + " no primeiro dado.")
                d62 = str(random.randint(1, 6))
                print("Você tirou " + d62 + " no segundo dado.")
                sAtual = int(StatusJogadores[i])
                if d6 == d62:
                    sAtual = 0
                    print("Parabéns, você escapou da prisão.")
                elif sAtual == 1:
                    Din -= 30
                    print("Você não conseguiu passar com os dados. Mas pagou R$30 e está livre.")
                    sAtual -= 1
                else:
                    print("Você não conseguiu tirar dados iguais e permanecerá na prisão.")
                    sAtual -= 1
                StatusJogadores = StatusJogadores[0:i] + str(sAtual) + StatusJogadores[(i + 1):]
            if Din < 0:  # Caso o jogador acabe falindo
                print(Nome + " você faliu e está fora do jogo.")
                StatusJogadores = StatusJogadores[0:i] + "4" + StatusJogadores[i + 1:]
                for i2 in range(0, 360, 9):
                    if (Terrenos[i: (i * 2)] == "0" + str(
                                i + 1)):  # ID Correspondente ao dono do terreno = jogador atual
                        Terrenos = Terrenos[0: i2] + "00" + Terrenos[i2 + 2:]
                Din = 0
            Din = str(Din)
            Posicao = str(Posicao)
            if len(Posicao) < 2:
                Posicao = "0" + Posicao
            while len(Din) < 5:
                Din = "0" + Din
            # Colocando as variaveis que mudaram de volta na "array" improvisada
            PosicaoJogadores = PosicaoJogadores[0:i * 2] + Posicao + PosicaoJogadores[(i * 2) + 2:]
            DinheiroJogadores = DinheiroJogadores[0: i * 5] + Din + DinheiroJogadores[(i * 5) + 5:]
            if not FimDeJogo:
                print("Se deseja encerrar o jogo, digite 'ENCERRAR'. Caso contrário aperte [ENTER]")
                if input() == "ENCERRAR":
                    print("Assim que todos tiverem sua última jogada, o jogo será encerrado.")
                    FimDeJogo = True
        if StatusJogadores == NumJogadores * "4":
            FimDeJogo = True
Vitorioso = ""
Din = 0
Plural = False
for i in range(0, NumJogadores):
    DinAtual = int(DinheiroJogadores[i * 5: (i * 5) + 5])
    if DinAtual > Din:
        Din = DinAtual
        Vitorioso = NomeJogadores[i * 50: (i * 50) + 50].strip()
        Plural = False
    elif DinAtual == Din:
        Vitorioso += " e " + NomeJogadores[i * 50: (i * 50) + 50].strip()
        Plural = True
if Plural:
    print(Vitorioso + " foram vitoriosos com R$" + str(Din) + ".")
else:
    print(Vitorioso + " foi vitorioso com R$" + str(Din) + ".")
