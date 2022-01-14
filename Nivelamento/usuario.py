class usuario:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def set_nome(self,nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf