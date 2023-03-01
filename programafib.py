def programafib():
    num = eval(input("Digite um número: "))
    fib_ant = 0
    fib_atual = 1
    while fib_atual < num:
        fib_prox = fib_ant + fib_atual
        fib_ant = fib_atual
        fib_atual = fib_prox

    if fib_atual == num:
        print(f"{num}, pertece à sequência de Fibonacci.")

    else:
        print(f"{num}, não pertence à sequencia de Fibonacci.")

programafib()
a = input("Deseja continuar? Sim/Não ").upper()

while a == 'SIM':
        programafib()
        a = input("Deseja continuar? Sim/Não ").upper()

print('Obrigado!')


"""""
Me desculpa me empolguei 
"""