import time

class Pessoa():
    def __init__(self,nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.estado = "Aguardando..."

    def falar(self):
        print("Eae meu mano!")
        self.estado = "Falando..."
        time.sleep(1)
        print(f"Tenho {self.idade} anos e meu nome é {self.nome}")

    def dormir(self):
        print("Vo dormir meu fi")
        self.estado = "Dormindo..."

