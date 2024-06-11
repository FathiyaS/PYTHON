def listsum(numList):
    
    if numList > 2:
        return numList * listsum(numList - 1)

    return 2

numList = int(input('Masukkan angka: '))
faktorial = listsum(numList)
print(f'{numList}! = {faktorial}')
