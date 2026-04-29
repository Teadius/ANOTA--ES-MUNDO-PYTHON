times = ('-', 'CORINTHIAS', 'PALMEIRAS', 'SANTOS', 'GRÊMIO', 'CRUZEIRO', 'FLAMENGO', 
        'VASCO DA GAMA', 'CHAPECOENSE', 'ATLÉTICO', 'BOTAFOGO', 'ATLÉTICO-PR', 
        'BAHIA', 'SÃO PAULO', 'FLUMINENSE', 'SPORT RECIFE', 'EC VITORIA', 'CORITIBA', 
        'AVAI', 'PONTE PRETA', 'ATLÉTICO-GO')
print(f'top 20\n{times}')
print(f'top 5 {times[1:6]}')
print(f'os ultimos 4 {times[-4:]}')
print(f'top 20 em ordem alfabetica:\n{sorted(times)}')
print(f'O time chapecoense se encontra na posicao {times.index('CHAPECOENSE')}')
