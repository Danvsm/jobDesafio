string = input("Escreva uma palavra: ")
invertida = []

for i in range(len(string)-1, -1, -1):
    invertida.append(string[i])


invertida_string = "".join(invertida)


print("String original:", string)
print("String invertida:", invertida_string)
