import time
filmes = [] # matriz onde serão adicionados os filmes e suas informações
cont = 0
temp = 0 #variavel temporaria que ira percorrer a matriz atras do codigo
temp2= 0 #varialvel temporaria que ira encontrar a linha do ano desejado
temp3= 0
temp4=0
while True:    #o programa irá rodar enquanto o usuario não pedir para sair
    n = input("""\033[7;36mO que gostaria de fazer ?

[3]--------------------------------- Adicionar um filme
[1]--------------------------------- Modificar uma Informação do filme
[2]--------------------------------- Buscar filmes por ano
[4]--------------------------------- Buscar filmes por categoria
[5]--------------------------------- Comprar um filme
[0]--------------------------------- Sair

\033[m""") #menu de opções

    while not n.isnumeric():
        n = input("""\033[7;36mO que gostaria de fazer ?

        [3]--------------------------------- Adicionar um filme
        [1]--------------------------------- Modificar uma Informação do filme
        [2]--------------------------------- Buscar filmes por ano
        [4]--------------------------------- Buscar filmes por categoria
        [5]--------------------------------- Comprar um filme
        [0]--------------------------------- Sair

        \033[m""")


    if n == "0": # se for 0 irá sair do programa e irá exibir o catalogo de filmes
        break

    if n == "1": #se digitar 1, irá abrir para colocar o codigo do filme que se quer alterar
        time.sleep(1) # da um segundo antes das infromações aparecerem para nao ficarem meio que explodindo na tela
        cod = int(input("\033[1;31mDigite o codigo do filme que deseja altera: \033[m"))

        for i in range(0,cont): #os codigos estao na posiçao [i][0]
            if filmes[i][8] == cod:    #varre toda a matriz e descobre qual o codigo correspondente
                temp = i

        time.sleep(1)  # da um segundo antes das infromações aparecerem para nao ficarem meio que explodindo na tela

        info = int(input("""\033[7;37mQual informação voce deseja alterar?:
[0]---------------------------------Nome
[1]---------------------------------Categoria
[2]---------------------------------Classificação
[3]---------------------------------Ano De lançamento 
[4]---------------------------------Preço
[5]---------------------------------Quantidade
[6]---------------------------------Quantidade de Filmes Vendidos
[7]---------------------------------Montante Arrecadado\033[m
"""))
        if info == 0:
            new_nome = input("\033[1;31mDigite um novo nome: \033[m")
            filmes[temp][0] = new_nome  # o temp me da em que linha ta o filme, como eu quero mudar o nome eu pego a linha temp e mudo a coluna de nome que é a 0


        if info == 1:
            new_categoria = input("\033[1;31mDigite uma nova categoria: \033[m") # a categoria agora foi mudada
            filmes[temp][1] = new_categoria


        if info == 2:
            new_classe = input("\033[1;31mDigite uma nova classificação: \033[m") # a classificação foi mudade, ela fica na coluna 2, no caso as listas e matrizes começam suas cotnagens com 0
            filmes[temp][2] = new_classe


        if info == 3:
            new_age = input("\033[1;31mDigite um novo ano de lançamento: \033[m")
            filmes[temp][3] = new_age #ano do lançamento do filme é mudado


        if info == 4:
            new_preco = input("\033[1;31mDigite um novo preço: \033[m")
            filmes[temp][4] = new_preco # agora o preço foi alterado


        if info == 5:
            new_quantidade = input("\033[1;31mDigite uma nova quantidade: \033[m")
            filmes[temp][5] = new_quantidade


        if info == 6:
            new_quant_vend = input("\033[1;31mDigite uma nova quantidade de filmes vendidos: \033[m")
            filmes[temp][6] = new_quant_vend


        if info == 7:
            new_mont = input("\033[1;31mDigite um novo montante arrecadado: \033[m")
            filmes[temp][7] = new_mont



    if n == "3": #se o numero digitado for 3 iremos começar a adicionar os valores
        time.sleep(1)  # da um segundo antes das infromações aparecerem para nao ficarem meio que explodindo na tela
        while True:
            menu2 = input("\033[1;31mBOM DIA! Vamos adicionar seu filme. Ainda Deseja Continuar?(S/N) \033[m").lower() # o que foi digitado fica no diminutivo

            while not menu2.isalpha():

                menu2 = input(
                    "\033[1;31mBOM DIA! Vamos adicionar seu filme. Ainda Deseja Continuar?(S/N) \033[m").lower()

            if menu2 == "n":
                break
            for i in range(0,1):
                dados = []
                for j in range(0,1):
                    codigo = input("\033[1;31mDigite um codigo para seu filme: \033[m")

                    while not codigo.isnumeric():
                        codigo = input("\033[1;31mDigite um codigo para seu filme: \033[m")

                    nome = input("\033[1;31mNome do  filme: \033[m")
                    categoria = input("\033[1;31mCategoria: \033[m")
                    classificacao = input("\033[1;31mClassificação indicativa: \033[m")


                    ano = input("\033[1;31mAno do filme: \033[m")
                    while not ano.isnumeric():
                        ano = input("\033[1;31mAno do filme: \033[m")

                    preco = float(input("\033[1;31mValor do filme:R$ \033[m"))
                    quantidade = int(input("\033[1;31mQuantidade: \033[m"))
                    quantidade_vendidos = int(input("\033[1;31mQuantos foram vendidos? \033[m"))
                    montante = preco*quantidade_vendidos #float(input("\033[1;31mQual a arrecadação? \033[m"))
                    print(montante)
                    dados.append(nome)
                    dados.append(categoria)
                    dados.append(classificacao)
                    dados.append(ano)
                    dados.append(preco)
                    dados.append(quantidade)
                    dados.append(quantidade_vendidos)
                    dados.append(montante)
                    dados.append(codigo)
                filmes.append(dados)
                cont += 1 # conta quantos filmes foram adicionados

    if n == "2":
        time.sleep(1)  # da um segundo antes das infromações aparecerem para nao ficarem meio que explodindo na tela
        intervalo=input("\033[1;31mDigite qual o ano do filme desejado: \033[m")
        while not intervalo.isnumeric():
            intervalo =input("\033[1;31mDigite qual o ano do filme desejado: \033[m")


        for i in range(0,cont): #os codigos estao na posiçao [i][3], nesse caso os anos do filme
            if filmes[i][3] == intervalo:    #varre toda a matriz e descobre qual o ano do filmes
                temp2 = i

            print(filmes[temp2][0])                 #imprime o nome dos filmes do ano desejado

    if n == "4":
        time.sleep(1)  # da um segundo antes das infromações aparecerem para nao ficarem meio que explodindo na tela
        procurar_categoria=input("\033[1;31mQual categoria de filmes deseja? \033[m")
        for i in range(0,cont): #os codigos estao na posiçao [i][0]
            if filmes[i][1] == procurar_categoria:    #varre toda a matriz e descobre qual o codigo correspondente
                temp3 = i

                print(filmes[temp3][0]) #imprime o titulo do filme que tem a categoria escolhida pelo usuario

    if n == "5":
        co2=int(input("Digite o codigo do filme que voce deseja comprar: "))
        for i in range(0, cont):  # os codigos estao na posiçao [i][0]
            if filmes[i][8] == co2:  # varre toda a matriz e descobre qual o codigo correspondente
                temp4 = i

        if filmes[temp4][6] == 0: #se a quantidadade em estoque for zero ele madna essa mensagem
            time.sleep(1)
            print("\033[1;32mDesculpe, mas não temos este filme no estoque no momento\033[m")
        else:
            time.sleep(1)
            quantidade_comprar=int(input("Quantos filmes deseja comprar ?: "))
            print(f"Sua compra irá custar {filmes[temp4][5]*quantidade_comprar}")

print(filmes)