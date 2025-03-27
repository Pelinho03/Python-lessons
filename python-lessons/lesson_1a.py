# Elaborar um algoritmo em python que faça a gestão de stocks de produtos. 
# - O algoritmo deve permitir adicionar produtos; 
# - Atualizar a quantidade de um produto específico; 
# - Remover um produto; 
# 
# Cada produto tem: 
# - Um nome,
# - Um preço por unidade 
# - Uma quantidade em stock

class produto:  # Define uma classe chamada 'produto' para representar um produto no stock
    def __init__(self, nome, preçoUnidade, quantidade):  # Método construtor para inicializar os atributos do produto
        self.nome = nome  # Atributo que armazena o nome do produto
        self.preçoUnidade = preçoUnidade  # Atributo que armazena o preço por unidade do produto
        self.quantidade = quantidade  # Atributo que armazena a quantidade em stock do produto

    def atualizar_quantidade(self, quantidade):  # Método para atualizar a quantidade do produto
        self.quantidade += quantidade  # Incrementa a quantidade atual com o valor fornecido

    def __str__(self):  # Método especial para retornar uma representação em string do objeto
        return f'{self.nome}: {self.quantidade} unidades, Preço por unidade: {self.preçoUnidade:.2f}€'  
        # Retorna uma string formatada com o nome, quantidade e preço por unidade do produto


class stock:  # Define uma classe chamada 'stock' para gerenciar o estoque de produtos
    def __init__(self):  # Método construtor para inicializar os atributos da classe
        self.produtos = {}  # Dicionário para armazenar os produtos, onde a chave é o nome do produto

    def adicionar_produto(self, nome, preçoUnidade, quantidade):  # Método para adicionar um produto ao estoque
        if nome in self.produtos:  # Verifica se o produto já existe no estoque
            self.produtos[nome].atualizar_quantidade(quantidade)  # Atualiza a quantidade do produto existente
        else:  # Caso o produto não exista no estoque
            self.produtos[nome] = produto(nome, preçoUnidade, quantidade)  # Adiciona um novo produto ao estoque

    def remover_produto(self, nome):  # Método para remover um produto do estoque
        if nome in self.produtos:  # Verifica se o produto existe no estoque
            del self.produtos[nome]  # Remove o produto do dicionário
        else:  # Caso o produto não exista no estoque
            print(f'O produto {nome} não existe no stock')  # Exibe uma mensagem informando que o produto não foi encontrado

    def mostrar_stock(self):  # Método para exibir todos os produtos no estoque
        if not self.produtos:  # Verifica se não há produtos no estoque
            print('O stock está vazio.')  # Exibe uma mensagem se o estoque estiver vazio
        for produto in self.produtos.values():  # Itera sobre os valores (objetos 'produto') no dicionário
            print(produto)  # Exibe a representação em string de cada produto

# Cria uma instância da classe 'stock' para gerenciar o estoque de produtos
stock = stock()  

# Adiciona produtos ao estoque com nome, preço por unidade e quantidade inicial
stock.adicionar_produto('Banana', 0.50, 100)  # Adiciona 100 unidades de Banana ao estoque com preço de 0.50€ por unidade
stock.adicionar_produto('Maçã', 0.30, 50)  # Adiciona 50 unidades de Maçã ao estoque com preço de 0.30€ por unidade
stock.adicionar_produto('Laranja', 0.40, 75)  # Adiciona 75 unidades de Laranja ao estoque com preço de 0.40€ por unidade

# Exibe o título do resumo do estoque
print('Resumo do stock: ')  
# Chama o método para exibir todos os produtos no estoque
stock.mostrar_stock()  

# Remove um produto do estoque
stock.remover_produto('Banana')  # Remove o produto 'Banana' do estoque

# Exibe o título do resumo após a remoção
print('\nResumo após remover Banana:')  
# Chama o método para exibir o estoque atualizado
stock.mostrar_stock()
