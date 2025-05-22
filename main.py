
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produtos(self, *produtos):
        self.produtos.append(produtos)
        print("Produto inserido ao carrinho com sucesso!")
    
    @property
    def listar_produtos(self):
        print("Seu carrinho:")
        for item in self.produtos:
            for produto in item:
                print(f"Nome: {produto.nome}")
                print(f"Nome: {produto.quantidade}")
                print("-" * 30)


class Produto:
    def __init__(self):
        self._nome = "undefined"
        self._quantidade = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade


meu_carrinho = CarrinhoDeCompras()

while True:
    
    print("""
[1] Adicionar novo produto ao carrinho
[2] Listar produtos do carrinho
    """)
    
    opcao = input("Digite aqui >>> ").strip()
    
    if opcao == "1":
        nome_produto = input("Nome do produto >>> ")
        
        while True:
            quantidade_produto = input("Quantidade do produto >>> ")
            
            try:
                quantidade_produto = int(quantidade_produto)
                break
            
            except Exception as e:
                print("Digite apenas números.")
        
        produto = Produto()
        produto.nome = nome_produto
        produto.quantidade = quantidade_produto
        
        meu_carrinho.inserir_produtos(produto)

    elif opcao == "2":
        meu_carrinho.listar_produtos
    
    else:
        print("Digite apenas 1 ou 2.")
