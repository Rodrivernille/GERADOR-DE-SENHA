import random
import string

def gerar_senha(tamanho=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("Sua senha gerada é:", gerar_senha(12))
