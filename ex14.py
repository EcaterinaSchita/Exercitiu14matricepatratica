n=int(input('Introduceti numarul de linii a matricei:'))
M=[[int(input()) for i in range(n)] for j in range(n)]
print('Matricea este:')
for i in range(len(M)):
    