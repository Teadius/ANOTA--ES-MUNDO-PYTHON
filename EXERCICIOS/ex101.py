from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade >= 16 and idade < 18 or idade > 70:
        return f'Com {idade} anos: Voto opcional'
    elif idade > 18 and idade < 70:
        return f'Com {idade} anos: Voto obrigatório'
    else:
        return f'Com {idade} anos: Não tem idade para votar'


while True:
    try:
        nac = int(input('Em que ano você naceu? '))
        if date.today().year < nac < 1900:
            print('valor incorreto')
        break
    except ValueError:
        print('Por favor, digite um ano válido.')

print(voto(nac))
