from pydantic import BaseModel, ValidationError

# Definindo um modelo com Pydantic
class SomaInput(BaseModel):
    valor1: int
    valor2: int

# Função que faz a soma
def soma(valores: SomaInput) -> int:
    return valores.valor1 + valores.valor2

# Exemplo de uso
try:
    # Tentando criar um modelo com valores válidos
    dados = SomaInput(valor1=5, valor2=10)
    resultado = soma(dados)
    print(f"A soma é: {resultado}")
except ValidationError as e:
    print("Erro de validação:", e)

try:
    # Tentando criar um modelo com valores inválidos
    dados = SomaInput(valor1=5, valor2="dez")  # Aqui vai falhar
    resultado = soma(dados)
    print(f"A soma é: {resultado}")
except ValidationError as e:
    print("Erro de validação:", e)