from utils.PrintPretty import PrintPretty

print_pretty = PrintPretty()

def origin_view():
    print("\n" + "Selecione uma das opções abaixo:")
    print("1. Usuário")
    print("2. Grupo")
    print("5. Presentes")
    print("6. Cartas")
    print("3. Gerenciar usuarios de um grupo")
    print("4. Gerenciar lista de desejos de um grupo")
    print("0. Encerrar programa")

def user_view():
    print("\n" +"Selecione uma das opções abaixo:")
    print("1. Criar Usuário")
    print("2. Deletar Usuário pelo nome")
    print("3. Mostrar todos os Usuário")
    print("4. Pesquisar por id")
    print("5. Atualizar Usuário por id")
    print("0. Voltar")

def group_view():
    print("\n" +"Selecione uma das opções abaixo:")
    print("1. Criar Grupo")
    print("2. Deletar Grupo")
    print("3. Mostrar todos os Grupos")
    print("4. Atualizar Grupo")
    print("0. Voltar")

def user_group_view():
    print("\n" +"Selecione uma das opções abaixo:")
    print("1. Adicionar participante a um grupo")
    print("2. Remover participante a um grupo")
    print("3. Mostrar todos os usuarios atrelados a um grupo")
    print("4. Sortear remetentes de um grupo")
    print("0. Voltar")

def wish_list_view():
    print("\n" +"Selecione uma das opções abaixo:")
    print("1. Adicionar um presente a lista de desejo")
    print("2. Remover um presente da lista de desejo")
    print("3. Mostrar todos os presentes de um participante")
    print("0. Voltar")

def gift_view():
    print("\n" + "Selecione uma das opções abaixo:")
    print("1. Adicionar um presente ao banco")
    print("2. Mostrar todos os presentes cadastrados")
    print("0. Voltar")

def letter_view():
    print("\n" +"Selecione uma das opções abaixo:")
    print("1. Adicionar carta")
    print("2. Mostrar todas as cartas")
    print("0. Voltar")

def invalid_option():
    print_pretty.red("Opção invalida, por favor, tente novamente!")

def exit_program():
    print("\n" + "Aplicativo finalizado")