# Desvios condicionais

numero = int(input("Digite um numero:"))

# if significa "se" ou seja ele excuta o bloco dentro da identacao 
# caso ele cumpra condições, elif fica entre o if e else e significa 
# "se nao se", o else significa "se nao" caso nenhumas das condicoes 
# anteriores se comprirem ele executa.
if numero == 0:
    print("O numero e zero")
elif numero > 0:
    print("O numero e positivo")
else:
    print("O numero e negativo")

# condicao simplificada
print('o numero e zero' if numero == 0 else 'o numero e positivo' 
if numero > 0 else 'o numero e negativo')