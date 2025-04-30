def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

# Exemplo de uso
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = dividir(num1, num2)
    print(f"O resultado da divisão é: {resultado}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
