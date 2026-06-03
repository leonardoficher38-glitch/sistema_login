SENHA_CORRETA = "python123"
TENTATIVAS_MAX = 3

tentativas = 0

while tentativas < TENTATIVAS_MAX:
    senha = input("Digite a senha: ")

    if senha == SENHA_CORRETA:
        print("Acesso permitido! Bem-vindo.")
        break
    else:
        tentativas += 1
        restantes = TENTATIVAS_MAX - tentativas

        if restantes > 0:
            print(f"Senha errada! {restantes} tentativa(s) restante(s).")
        else:
            print("Acesso bloqueado! Tente mais tarde.")