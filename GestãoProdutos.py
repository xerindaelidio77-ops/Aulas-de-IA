class Produto:#definicao de classes
    contador_id =1
    def __init__(self,nome,preco,qtd_produtos):
        self.id = Produto.contador_id
        Produto.contador_id+=1
        self.nome = nome
        self.preco = preco
        self.qtd_produtos= qtd_produtos
    def __str__(self):  
        return f"[{self.id}]-${self.nome}:{self.preco:.2f} Mts-{self.qtd_produtos} unid"
        
class Gestao:
    def __init__(self):
        self.produtos=[]
        
    def adicionar(self):
        nome = input("Digite o nome do Produto:").strip()
        preco= float(input("Digite o Preço do produto:"))
        qtd_produtos =int(input("Digite a quantidade de produtos"))
        self.produtos.append(Produto(nome,preco,qtd_produtos))
        print(f"Produto{nome} adicionado com sucesso!!!")
        
    def listar(self):
         if not self.produtos:
             print("Loja Vazia!!!")
             return

         print("====Produtos Cadastrados====")
         total =0.0
         for produto in self.produtos:
             print(produto)
             total+=produto.preco*produto.qtd_produtos
         print(f"Valor total do estoque: ${total:.2f}")
             
    def actualizar(self):        
           self.listar()  
           try:
               id_produto=float(input("Digite ID do produto a actualizar"))
           except ValueError:
               print("ID invalido")
               return
           novo_preco= float(input("Digite novo preço"))
           novo_nome= input("Digite novo nome do produto:")
           qtd_produtos=int(input("Digite nova quantidade de produto"))
           for produto in self.produtos:
               if produto.id==id_produto:
                   produto.nome=novo_nome
                   produto.preco=novo_preco
                   produto.qtd_produtos=qtd_produtos
                   print(f"O preço de:{produto.nome} Actualizado para {novo_preco}Mts em {qtd_produtos} produtos")
                   return
           print("Produto não Encontrado.") 
           
    def remover(self):
         self.listar()
         if not self.produtos:
             print("Loja Vazia!!!")
         try:
            id_produto=float(input("\n Digite o ID do produto que deseja remover:"))
         except ValueError:
             print("ID inválido")
             return
         antes=len(self.produtos)
         self.produtos= [c for c in self.produtos if c.id!=id_produto]
         if len(self.produtos)<antes:
             print(f"Produto com ID{id_produto} removido")
         else:
             print("produto removido com sucesso!!!")
         
        
           

 #--------- Função principal ----------
def main():
    gestao = Gestao()
    
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar  Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("0. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            gestao.adicionar()
        elif opcao == "2":
            gestao.listar()
        elif opcao == "3":
            gestao.atualizar()
        elif opcao == "4":
            gestao.remover()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print(" Opção inválida.")

if __name__ == "__main__":
    main()