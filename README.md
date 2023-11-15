# PROJETO FINAL - PROGRAMAÇÃO PARA ENGENHARIA

## - Sistema para padaria :bread:

Para o projeto final da disciplina de Programação, deverá ser desenvolvido um sistema para uma padaria.

O programa deverá ser desenvolvido na linguagem de programação **Python** e cumprir seguintes tarefas:

### Menu Principal

1. [Cadastrar Produto](#cadastrar-produto)
2. [Alterar Produto](#alterar-produto)
3. [Realizar Venda](#realizar-venda)
4. [Relatórios](#relatorios)
5. Sair

#### 1. Cadastrar Produto <a name="cadastrar-produto"></a>

Nessa tela o usuário terá a opção de cadastrar um produto para venda na padaria.

As informações para cadastro são:

- Identificador do produto (gerar automaticamente, o usuário não pode mexer nesse campo).
- Nome do produto.
- Tipo de produto (Pão, Bolo, Salgado, Bebida, etc.).
- Preço de venda.
- Estoque inicial.

Os campos considerados obrigatórios são:

- Nome do produto.
- Tipo de produto.
- Preço de venda.
- Estoque inicial.

Caso algum dos campos considerados obrigatórios não forem fornecidos, o sistema deverá apresentar uma mensagem de aviso e reiniciar o cadastro.

O sistema deverá apresentar a mensagem de realização de cadastro com sucesso, ex: ‘_Cadastro Realizado com sucesso!_’.

### 2. Alterar Produto <a name="realizar-venda"></a>

Para isso, o usuário deverá realizar a busca de produto pelo nome ou pelo 
identificador.

Caso o produto seja encontrado, o sistema deverá permitir a alteração dos 
seguintes campos:

- Nome do produto.
- Tipo de produto.
- Preço de venda.
- Estoque.

Ao inserir os novos dados sobre o produto, o sistema deverá apresentar uma mensagem de confirmação de alteração.

### 3. Realizar Venda <a name="alterar-produto"></a>

Nessa tela o usuário terá a opção de registrar uma venda de produto na padaria.
Para isso, o usuário deverá:

1. Selecionar o produto.
2. Informar a quantidade desejada.

O sistema deverá verificar se a quantidade solicitada está disponível no estoque.
Caso contrário: deverá apresentar uma mensagem informando que não há estoque suficiente.

Se houver estoque suficiente, o sistema deverá:

1. Registrar a venda.
2. Atualizar o estoque.
3. Apresentar a mensagem de realização. Ex: "Venda realizada com sucesso!".

### 4. Relatórios <a name="relatorios"></a>

Todas os relatórios devem conter um cabeçalho e ser apresentado de forma tabular.
Nessa tela, o sistema deverá apresentar as seguintes opções:

1. Relatório de todos os produtos.
2. Relatório de vendas realizadas.