def fibonacci (n):
  if n < 1:
    return [n]

  listSum = fibonacci(n - 1)
  n1 = listSum[-2] if len(listSum) > 2 else 0
  n2 = listSum[-1] if len(listSum) > 2 else 1

  return listSum + [n1 + n2]

panjang = int(input('Masukkan panjang deret : '))
print(fibonacci(panjang - 1))
