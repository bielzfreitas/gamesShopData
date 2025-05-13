# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_beneficio(beneficio):
    if beneficio == "Escalabilidade":
        return "Capacidade de aumentar ou diminuir recursos conforme a demanda"

    # COMPLETE AQUI: Preencha corretamente cada benefício, considerando as descrições abaixo:
    elif beneficio == "Agilidade":
        return "Implementação rápida e eficiente de soluções"

    elif beneficio == "Elasticidade":
        return "Ajuste rápido de recursos para atender às necessidades"

    elif beneficio == "Economia de custos":
        return "Redução de custos com infraestrutura e manutenção"

# Imprime a descrição do benefício recebido na "entrada" através da função "descrever_benefício".
print(descrever_beneficio(entrada))