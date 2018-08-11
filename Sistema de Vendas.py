filmes=[] # matriz onde serão adicionados os filmes e suas informações
while True:
    temp=0
    n=int(input("""O que gostaria de fazer ?

[3]--------------------------------- Adicionar um filme
[1]--------------------------------- Modificar uma Informação do filme
[0]--------------------------------- Sair

""")) #menu de opções

    if n==0:
        break

    if n==1: #se digitar 1, irá abrir para colocar o codigo do filme que se quer alterar
        cod=int(input("Digite o codigo do filme que deseja altera: "))
        info=int(input("""Qual informação voce deseja alterar?:
[0]---------------------------------Nome
[1]---------------------------------Categoria
[2]---------------------------------Classificação
[3]---------------------------------Ano De lançamento 
[4]---------------------------------Preço
[5]---------------------------------Quantidade
[6]---------------------------------Quantidade de Filmes Vendidos
[7]---------------------------------Montante Arrecadado
"""))
        if info==0:
            new_nome=input("Digite um novo nome: ")
            filmes[temp][1]=new_nome


    if n == 0:
        cod = int(input("Digite o Codigo do filmes que deseja alterar: "))
        for i in range(0,2): #os codigos estao na posiçao [i][0]
            if filmes[i][0] == cod:
                temp = i


    if n == 3: #se o numero digitado for 3 iremos começar a adicionar os valores
        while True:
            menu2=input("BOM DIA!! Vamos adicionar seu filme. Ainda Deseja Continuar?(S/N) ").lower()
            if menu2=="n":
                break
            for i in range(0,1):
                dados = []
                for j in range(0,1):
                    codigo = int(input("Digite um codigo para seu filme: "))
                    nome=input("Nome do  filme: ")
                    categoria=input("Categoria: ")
                    classificacao=input("Classificação indicativa:  ")
                    ano=int(input("Ano do filme: "))
                    preco=float(input("Valor do filme: "+ "R$"))
                    quantidade=int(input("Quantidade: "))
                    quantidade_vendidos=int(input("Quantos foram vendidos? "))
                    montante=float(input("Qual a arrecadação? "))
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
