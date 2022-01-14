from usuario import usuario
from rotas import rotas
import random
import datetime

class sistema:

    lista_rotas = []
    usuarios = []
    rotas_reservadas = []

    with open("rotas.txt", "r", encoding="utf-8") as file:
        text = file.readlines()

    for line in text:
        split = line.split(" - ")
        option = split[0]
        origem = split[1]
        destino = split[2]
        valor = split[3]

        rota = rotas(option, origem, destino, valor)
        lista_rotas.append(rota)


    def cadastra_usuario(self,nome,cpf):
        user = usuario(nome,cpf)
        self.usuarios.append(user)
        print("Usuario cadastrado")
        ct = str(datetime.datetime.now())
        log = " "+user.nome + " " +user.cpf +" Usuario cadastrado \n"
        self.input_log(ct,log)

    def reserva_passagem(self,user):

        for rota in self.lista_rotas:
            print(rota.option,rota.origem,rota.destino,rota.valor)

        option = int(input("Escolha uma rota: "))
        self.rotas_reservadas.append((user,rota,random.randint(1,1000)))
        print("A reserva foi feita")
        ct = str(datetime.datetime.now())
        log = " "+user.nome+ " "+ user.cpf +" Rota reservada "+self.lista_rotas[option].origem+"X"+self.lista_rotas[option].destino+" R$"+self.lista_rotas[option].valor
        self.input_log(self,ct,log)

    def cancela_reserva(self,user):
        for reservas in self.rotas_reservadas:
            if reservas[0].cpf == user.cpf:
                print(reservas[1].origem, reservas[1].destino, reservas[1].valor + " Codigo:", reservas[2])

        option = int(input("Informe o código da reserva que deseja cancelar: "))
        cont = 0
        achou = False
        for reservas in self.rotas_reservadas:
            if reservas[2] == option:
                achou = True
                del(self.rotas_reservadas[cont])
                ct = str(datetime.datetime.now())
                log = " " + user.nome + " " + user.cpf + " Reserva cancelada " + reservas[1].origem+"X"+reservas[1].destino+"\n"
                self.input_log(self, ct, log)
            cont+=1

        if achou:
            print("Reserva cancelada")
        else:
            print("Reserva não encontrada")

    def get_usuarios(self):
        return self.usuarios

    def get_rotas(self):
        return self.__rotas

    def input_log(self,time_stamp,text):
        log = time_stamp + text
        with open("log.txt","a",encoding="utf-8") as file:
            file.write(log)


