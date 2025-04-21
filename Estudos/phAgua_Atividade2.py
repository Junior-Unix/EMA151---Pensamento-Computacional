# 1. Construa um script em que você entre com o valor do PH da solução e o mesmo identifique
#    se a mesma pode ser classificada como PH ácido, básico ou neutro.

print('='*50)
print('Programa para classificar o PH da água.')
print('='*50)



while True:
    phAgua = input('Informe o PH da água ou (s)air: ')
    if phAgua.lower() == 's':
        print('Saindo do programa.')
        break
    phAgua = float(phAgua)
    if phAgua < 0.0 or phAgua > 14.0:
        print(' O PH informado [{}] é inválido. '.format(phAgua))
        break
    if phAgua >= 0.0 and phAgua <= 3.9:
        print(' O PH informado [{}] indica que a água é Ácido forte, pode causar danos imediatos a saúde. '.format(phAgua))
    elif phAgua >= 4.0 and phAgua <= 6.9:
        print(' O PH da água [{}] indica que a água é Acido leve, irritante e pode ser prejudicial a saúde. '.format(phAgua))
    elif phAgua == 7.0:
        print(' O PH da água [{}] indica que a água é NEUTRO, ideal para consumo humano e atividades aquáticas. '.format(phAgua))
    elif phAgua > 7.0 and phAgua <= 10.0:
        print(' O PH da água [{}] indica que a água é Alcalino Leve: geralmente seguro, mas pode afetar a vida aquática. '.format(phAgua))
    elif phAgua >10.0 and phAgua <= 14.0:
        print(' O PH da água [{}] é Alcalino forte: Pode ser corrosivo e perigoso para organismos marinhos, ao consumir pode causar desconforto. '.format(phAgua))
    else:
        print(' O PH informado [{}] é inválido. '.format(phAgua))
