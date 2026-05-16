caracteres = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', 
            '8', '9', ' ', '!', '"', '#', '$', '%', '&', "'", 
            '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', 
            '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', 
            '`', '{', '|', '}', '~', 'á', 'à', 'â', 'ã', 'ä', 
            'é', 'è', 'ê', 'ë', 'í', 'ì', 'î', 'ï', 'ó', 'ò', 
            'ô', 'õ', 'ö', 'ú', 'ù', 'û', 'ü', 'ç', 'Á', 'À', 
            'Â', 'Ã', 'Ä', 'É', 'È', 'Ê', 'Ë', 'Í', 'Ì', 'Î', 
            'Ï', 'Ó', 'Ò', 'Ô', 'Õ', 'Ö', 'Ú', 'Ù', 'Û', 'Ü', 
            'Ç', '€', '£', '¥', '¢', '¬', '§', '°', '¹', '²', 
            '³', 'ª', 'º')

senha = str(input('Digite uma senha: ')).strip()
descriptografar = []
i = 0
while True:
    if i == len(senha):
        break
    print(f'O valor numero {i} em analise. ')
    if senha[i] in caracteres:
        descriptografar += senha[i]
        print(f'valor numero {i} identificado com o {senha[i]}. ')
    else:
        print(f'valor {i} não encontrado ')
    i += 1
print(f'Senha identificada como {descriptografar}')
