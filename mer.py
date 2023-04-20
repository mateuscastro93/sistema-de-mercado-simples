from tkinter import *

class Mercadinho:
    def __init__(self, master):
        self.master = master
        master.title("Mercadinho")
        
        # Criando os widgets
        self.label = Label(master, text="Bem-vindo ao Mercadinho!")
        self.label.pack()

        self.label_nome = Label(master, text="Nome do produto:")
        self.label_nome.pack()

        self.entry_nome = Entry(master)
        self.entry_nome.pack()

        self.label_preco = Label(master, text="Preço:")
        self.label_preco.pack()

        self.entry_preco = Entry(master)
        self.entry_preco.pack()

        self.botao_adicionar = Button(master, text="Adicionar", command=self.adicionar_produto)
        self.botao_adicionar.pack()

        self.botao_listar = Button(master, text="Listar produtos", command=self.listar_produtos)
        self.botao_listar.pack()

        self.botao_sair = Button(master, text="Sair", command=master.quit)
        self.botao_sair.pack()

        self.produtos = []

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()

        self.produtos.append((nome, preco))

        self.entry_nome.delete(0, END)
        self.entry_preco.delete(0, END)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Nome: {produto[0]} | Preço: {produto[1]}")


root = Tk()
mercadinho = Mercadinho(root)
root.mainloop()
