

#----------------#
#Questão 5
#----------------#

entrada = input("Digite uma string para inverter: ")

string_invertida = ""

for i in range(len(entrada) - 1, -1, -1):
    string_invertida += entrada[i]

print("String invertida:", string_invertida)
