# Descrição
# A computação em nuvem, ou cloud computing, é a entrega de recursos de TI 
# sob demanda por meio da internet, com definição de preço conforme o uso. 
# Neste desafio, você irá associar os conceitos fundamentais da computação 
# em nuvem com suas respectivas descrições.


# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "IaaS":
        return "Infraestrutura como Serviço"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
    elif conceito == "Computação em Nuvem":
        return "Entrega de serviços de computação pela internet"

    elif conceito == "SaaS":
        return "Software como Serviço"

    elif conceito == "PaaS":
        return "Plataforma como Serviço"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".
print(descrever_conceito(entrada))