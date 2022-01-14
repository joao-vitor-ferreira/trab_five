from sistema import sistema

def menu_autenticado(user):
    print("*********************************")
    print("*******LINHAS AEREAS FINXI*******")
    print("*********************************")

    print("(1) Fazer reserva de passagem (2) Cancelar reserva (3) Deslogar")

    option = int(input("Qual opção: "))

    if (option == 1):
        sistema.reserva_passagem(sistema,user)
        menu_autenticado(user)
    elif (option == 2):
        sistema.cancela_reserva(sistema,user)
        menu_autenticado(user)
    elif (option == 3):
        login()
    else:
        print("opção invalida")
        menu_autenticado(user)

def login():
    print("*********************************")
    print("*******LINHAS AEREAS FINXI*******")
    print("*********************************")

    print("(1) Login (2) Cadastrar Usuário (3) Sair")

    option = int(input("Qual opção: "))

    if (option == 1):
        login_cpf = input("Informe o cpf: ")
        autenticado = False
        usuario_autenticado = None

        for user in sistema.usuarios:
            if (user.cpf == login_cpf):
                usuario_autenticado = user
                autenticado = True

        if autenticado :
            menu_autenticado(usuario_autenticado)
        else:
            print("Usuário não incontrado")
            login()
    elif (option == 2):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        passagens.cadastra_usuario(nome,cpf)
        login()
    elif (option == 3):
        exit()
    else:
        print("opção invalida")
        login()

passagens = sistema()
login()

