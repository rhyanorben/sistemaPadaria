import pandas

#Funções

def buscaProduto(info):
    """
    Realiza a busca do produto pelo nome ou código.
    Necessário: Nome ou Código do produto.
    Retorna: índice e informações do produto no dicionário.
    """
    if info.isdigit():
        info = int(info)
    else:
        info = str(info.lower())
    for indice, produto in produtos.items():
        if indice == info or produto[0].lower() == info:
            return indice, produto
    return None, None


def alterarProduto(indice):
    """
    Faz a alteração do produto no dicionário.
    Necessário: Indice do produto no dicionário.
    Solicita o que o usuário quer modificar e depois realiza a modificação mediante confirmação.
    """
    opcao = -1
    while opcao != 0:
        opcao = input("O que você deseja alterar?\n1. Nome do produto\n2. Tipo do produto\n3. Valor de venda\n4. Estoque\n5. Todas informações\n0. Cancelar alteração\nOpcão: ")
        if opcao.lower() in ['1', 'nome', 'nome do produto', 'nome produto']:
            novaInfo = input("Novo nome do produto: ")
            print("Novo nome do produto é: {}".format(novaInfo))
            while True:
                confirmacao = input("Você confirma a alteração? (S/N): ")
                if confirmacao.lower() in ['sim', 's']:
                    produtos[indice] = (novaInfo, produtos[indice][1], produtos[indice][2], produtos[indice][3])
                    print("Alteração realizada com sucesso!")
                    break
                elif confirmacao.lower() in ['nao', 'n', 'não']:
                    print("Alteração cancelada!")
                    break
                else:
                    print("Alternativa incorreta, digite Sim ou Não!")
            break
            
        elif opcao.lower() in ['2', 'tipo', 'tipo do produto', 'tipo produto']:
            novaInfo = input("Novo tipo do produto: ")
            print("Novo tipo do produto é: {}".format(novaInfo))
            while True:
                confirmacao = input("Você confirma a alteração? (S/N): ")
                if confirmacao.lower() in ['sim', 's']:
                    produtos[indice] = (produtos[indice][0], novaInfo, produtos[indice][2], produtos[indice][3])
                    print("Alteração realizada com sucesso!")
                    break
                elif confirmacao.lower() in ['nao', 'n', 'não']:
                    print("Alteração cancelada!")
                    break
                else:
                    print("Alternativa incorreta, digite Sim ou Não!")
            break
            
        elif opcao.lower() in ['3','valor', 'valor de venda', 'valor venda']:
            while True:
                novaInfo = input("Novo valor de venda: ")
                try:
                    novaInfo = float(novaInfo)
                    break
                except ValueError:
                    print("Valor incorreto, tente novamente!")
            print("Novo valor de venda é: {}".format(novaInfo))
            while True:
                confirmacao = input("Você confirma a alteração? (S/N): ")
                if confirmacao.lower() in ['sim', 's']:
                    produtos[indice] = (produtos[indice][0], produtos[indice][1], novaInfo, produtos[indice][3])
                    print("Alteração realizada com sucesso!")
                    break
                elif confirmacao.lower() in ['nao', 'n', 'não']:
                    print("Alteração cancelada!")
                    break
                else:
                    print("Alternativa incorreta, digite Sim ou Não!")
            break

        elif opcao.lower() in ['4', 'estoque']:
            while True:
                novaInfo = input("Novo estoque: ")
                try:
                    novaInfo = float(novaInfo)
                    break
                except ValueError:
                    print("Valor incorreto, tente novamente!")
                print("Novo estoque do produto é: {}".format(novaInfo))
            while True:
                confirmacao = input("Você confirma a alteração? (S/N): ")
                if confirmacao.lower() in ['sim', 's']:
                    produtos[indice] = (produtos[indice][0], produtos[indice][1], produtos[indice][2], novaInfo)
                    print("Alteração realizada com sucesso!")
                    break
                elif confirmacao.lower() in ['nao', 'n', 'não']:
                    print("Alteração cancelada!")
                    break
                else:
                    print("Alternativa incorreta, digite Sim ou Não!")
            break

        elif opcao.lower() in ['5', 'todas informações', 'todas informacoes', 'todas', 'todos', 'todas as informações', 'todas as informacoes', 'todos informacoes']:
            novoNome = input("Novo nome do produto: ")
            novoTipo = input("Novo tipo do produto: ")
            while True:
                novoValorVenda = input("Novo valor de venda: ")
                try:
                    novoValorVenda = float(novoValorVenda)
                    break
                except ValueError:
                    print("Valor incorreto, tente novamente!")
            while True:
                novoEstoque = input("Novo estoque: ")
                try:
                    novoEstoque = float(novoEstoque)
                    break
                except ValueError:
                    print("Valor incorreto, tente novamente!")
            print("Nome: {}".format(novoNome))
            print("Tipo: {}".format(novoTipo))
            print("Valor Venda: {}".format(novoValorVenda))
            print("Estoque: {}".format(novoEstoque))
            while True:
                confirmacao = input("Você confirma a alteração? (S/N): ")
                if confirmacao.lower() in ['sim', 's']:
                    produtos[indice] = (novoNome, novoTipo, novoValorVenda, novoEstoque)
                    print("Alteração realizada com sucesso!")
                    break
                elif confirmacao.lower() in ['nao', 'n', 'não']:
                    print("Alteração cancelada!")
                    break
                else:
                    print("Alternativa incorreta, digite Sim ou Não!")
            break
        elif opcao == 0:
            print("Alteração cancelada!")
            break
        else:
            print("Opcão Inválida! Tente novamente.")


def realizarVenda(indice, quantidade):
    idVendas = len(vendas) + 1
    if produtos[indice][3] >= quantidade:
        vendas[idVendas] = (indice, produtos[indice][0], produtos[indice][2], quantidade, produtos[indice][2] * quantidade)
        estoqueAtualizado = produtos[indice][3] - quantidade
        produtos[indice] = (produtos[indice][0], produtos[indice][1], produtos[indice][2], estoqueAtualizado)
        print("Venda realizada com sucesso!")
    else:
        print("Produto não tem estoque suficiente.")
        print("Estoque: {}".format(produtos[indice][3]))


#Dicionários

#Dicionário Produtos. Código: (Nome Produto, Tipo Produto, Valor Venda, Estoque)
produtos = {
    1: ('Pão de Forma', 'Salgado', 250, 10),
    2: ('Bolo de Chocolate', 'Doce', 180, 3),
    3: ('Pão de Queijo', 'Salgado', 1000, 100)
}

#Dicionário Vendas. Código: (Código Produto, Nome Produto, Valor Unitário, Quantidade, Valor Total)
vendas = {}

#Defininindo Váriaveis

menuPrincipal = 0
idProduto = 0
nomeProduto = ''
tipoProduto = ''
valorVenda = 0
estoqueInicial = 0


#Menu Principal Sistema

while menuPrincipal != 5:
    while True:
        menuPrincipal = input("1. Cadastrar Produto\n2. Alterar Produto\n3. Realizar Venda\n4. Relatórios\n5. Sair\nOpção: ")
        try:
            menuPrincipal = int(menuPrincipal)
            break
        except ValueError:
            print("{} não é uma das opções, tente novamente.".format(menuPrincipal))


#1. Cadastrar Produto


    if menuPrincipal == 1:


        idProduto = len(produtos) + 1


        while True:
            nomeProduto = input("Produto: ")
            if nomeProduto == '':
                print("Produto não definido. Você precisa informar um nome de produto válido!")
            else:
                break


        while True:
            tipoProduto = input("Tipo Produto: ")
            if tipoProduto == '':
                print("Tipo de produto não definido. Você precisa informar um tipo de produto válido!")
            else:
                break


        while True:
            valorVenda = input("Valor Venda: ")
            try:
                valorVenda = float(valorVenda)
                break
            except ValueError:
                if valorVenda == 0:
                    print("valorVenda não foi definido. Você precisa informar um valor de venda!")
                else:
                    print("Valor incorreto, você precisa informar um valor válido.")


        while True:
            estoqueInicial = input("Estoque inicial: ")
            try:
                estoqueInicial = float(estoqueInicial)
                break
            except ValueError:
                if estoqueInicial == 0:
                    print("Estoque inicial não foi definido. Você precisa informar um estoque inicial válido!")
                else:
                    print("Valor incorreto, você precisa informar um estoque inicial válido.")


        #Adicionando produto cadastrado no dicionário


        produtos[idProduto] = nomeProduto, tipoProduto, valorVenda, estoqueInicial
        print("Cadastro realizado com sucesso!")


#2. Alterar Produto

    if menuPrincipal == 2:
        while True:
            produto = input("Digite o nome ou código do produto que você quer alterar: ")
            indiceEncontrado, produtoEncontrado = buscaProduto(produto)
            if indiceEncontrado is not None:
                alterarProduto(indiceEncontrado)
                break
            else:
                print("Produto não encontrado! Tente novamente.")


#3. Realizar Venda

    if menuPrincipal == 3:
        print("TELA DE VENDA")
        print("")
        while True:
            produto = input("Código ou Nome Produto: ")
            indiceEncontrado, produtoEncontrado = buscaProduto(produto)
            if indiceEncontrado is not None:
                break
            else:
                print("Produto não encontrado! Tente novamente.")
        while True:
            quantidade = input("Quantidade: ")
            try:
                quantidade = float(quantidade)
                break
            except ValueError:
                print("Quantidade Inválida! Tente novamente.") 
        realizarVenda(indiceEncontrado, quantidade)

#4. Relatórios

    if menuPrincipal == 4:
        while True:
            opcaoRelatorio = input("1. Relatório dos produtos\n2. Relatório de vendas\nOpção: ")
            if opcaoRelatorio.lower() in ['1', 'relatorio dos produtos', 'relatório dos produtos', 'produtos', 'relatório produtos', 'relatorio produtos']:
                print("               RELATÓRIO DE PRODUTOS")
                print("")
                relatorio = pandas.DataFrame.from_dict(produtos, orient='index', columns=['Nome', 'Tipo Produto', 'Valor Venda', 'Estoque'])
                relatorio.index.name = 'Cód Produto'
                print(relatorio)
                break

            elif opcaoRelatorio.lower() in ['2', 'relatorio de vendas', 'relatorio vendas', 'relatório de vendas', 'relatório vendas', 'relatório venda', 'relatorio venda', 'vendas', 'vendas']:
                print("                            RELATÓRIO DE VENDAS")
                print("")
                relatorio = pandas.DataFrame.from_dict(vendas, orient='index', columns=['Cód Produto', 'Produto', 'Valor Unit.', 'Quantidade', 'Valor Total'])
                relatorio.index.name = 'Cód Venda'
                print(relatorio)
                break

            else:
                print("Opção Inválida, tente novamente!")