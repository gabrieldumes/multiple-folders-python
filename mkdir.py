import os

pastas = input("Pastas: ")
lista = pastas.split(",")

os.mkdir("itens")
os.chdir("./itens")

for i in range(0, len(lista)):
    os.mkdir(lista[i])
    os.chdir("./" + str(lista[i]))
    arquivo = open(str(lista[i]) + ".txt", "w+")
    arquivo.write("")
    arquivo.close()
    os.chdir("../")

input("Pressione enter para encerrar o programa... ")
exit()
