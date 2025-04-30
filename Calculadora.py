# Calculadora.py

def soma(a, b): return a + b
def subtracao(a, b): return a - b
def multiplicacao(a, b): return a * b
def divisao(a, b): return a / b if b != 0 else "Erro: divisão por zero"

print("Escolha a operação:")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
op = input("Opção: ")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == "1":
    print("Resultado:", soma(a, b))
elif op == "2":
    print("Resultado:", subtracao(a, b))
elif op == "3":
    print("Resultado:", multiplicacao(a, b))
elif op == "4":
    print("Resultado:", divisao(a, b))
else:
    print("Operação inválida.")
