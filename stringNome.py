nome = str(input('Nome: '))
try:
    for c in nome:
        if c.isdigit():
            raise RuntimeError('Nome não pode conter números.')
except RuntimeError as e:
    print(f'Erro: {e}')
else:
    print(f'Nome válido: {nome}')
finally:
    print('Fim do programa.')