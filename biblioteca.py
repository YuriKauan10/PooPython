import time

class Pessoa():
    def __init__(self,nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.estado = "Acordado"


    def falar(self):
        if self.estado == "Comendo":
            self.estado = "Falando"
            print(f"Tengo(tenho) {self.idade} afos(anos) e meu nome é {self.nome}, foi mal, é que to comenfo(comendo)")
        elif self.estado == "Dormindo":
            print("ZzZzZz.. dormindo...")
        elif self.estado == "Falando":
            print("Você já está falando.")
        else:
            print(f"Tenho {self.idade} anos e meu nome é {self.nome} eu estudo no...")
            self.estado = "Falando"


    def pararFalar(self):
        if self.estado == "Acordado":
            print("Estou sem fazer nada.")
        else:
            print("Acabei de falar.")
            self.estado = "Acordado"

    def dormir(self):
        if self.estado == "Dormindo":
            print("Você já está dormindo.")
        else:
            print("Vou dormir.")
            self.estado = "Dormindo"


    def acordar(self):
        if self.estado == "Acordado":
            print("Já estou acordado.")
        else:
            print("Acordei painho")
            self.estado = "Acordado"

    def comer(self, comida):
        if comida and self.estado == "Acordado":
            print(f"{self.nome} está comendo {comida}")
            self.estado = "Comendo"
        elif self.estado == "Comendo":
            print("Você não pode comer, pois já está comendo.")
        elif self.estado == "Acordado":
            print(f"{self.nome} está comendo...")
            self.estado = "Comendo"
        elif self.estado == "Dormindo":
            print("Você nao pode comer pois está dormindo.")
        elif self.estado == "Falando":
            print("Quando eu acabar de falar eu como.")
