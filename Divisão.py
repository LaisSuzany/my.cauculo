def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

# Exemplo de uso
num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador: "))

resultado = dividir(num1, num2)
print("Resultado:", resultado)
