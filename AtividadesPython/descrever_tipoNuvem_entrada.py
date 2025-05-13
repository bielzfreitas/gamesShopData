# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um tipo de nuvem e retornar sua respectiva descrição.
def descrever_tipo_nuvem(tipo):
    if tipo == "Nuvem Pública":
        return "Serviços oferecidos pela internet por terceiros"
        
    # COMPLETE AQUI: Preencha corretamente cada tipo de nuvem, considerando as descrições abaixo:
    elif tipo == "Multicloud":
        return "Uso de múltiplos provedores de nuvem"

    elif tipo == "Nuvem Híbrida":
        return "Combinação de nuvem pública e privada"

    elif tipo == "Nuvem Privada":
        return "Infraestrutura dedicada exclusivamente a uma organização"
        
# Imprime a descrição do tipo de nuvem recebida na "entrada" através da função "descrever_tipo_nuvem".
print(descrever_tipo_nuvem(entrada))