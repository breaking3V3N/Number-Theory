def times_table(q:int,n: int)->list:
    table = []
    for x in range (0,n):
        table.append((x+1)*q)
    return  table

print(times_table(19,5))

def multiplication(q:int,n:int)->int:
    if n == 1:
        return q
    else:
        return q+multiplication(q,n-1)

a= [255]
b = times_table(1463,100)
print(b)
for idx in range(0,100):
    a.append(255 + b[idx])
print(a)

