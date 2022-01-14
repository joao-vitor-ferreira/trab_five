class rotas:

    def __init__(self,option,origem,destino,valor):
        self.__option = option
        self.__origem = origem
        self.__destino = destino
        self.__valor = valor

    def set_origem(self,origem):
        self.__origem = origem

    def set_destino(self,destino):
        self.__destino = destino

    def set_valor(self,valor):
        self.__valor = valor

    def set_option(self,option):
        self.__option = option

    @property
    def option(self):
        return self.__option

    @property
    def origem(self):
        return self.__origem

    @property
    def destino(self):
        return self.__destino

    @property
    def valor(self):
        return self.__valor


