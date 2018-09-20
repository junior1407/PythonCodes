from random import randint

c = randint(4,10)
entrada = randint(1, c)
saida = randint(1,c)

v =randint(4,2*c - 1)
print(c,entrada,saida,v)
lista_in = [0] * (c+1)
lista_out = [0] * (c+1)
for i in range(v):
    while(True):
        a = randint(1,c)
        b = randint(1,c)
        if (a!=b and lista_in[a]!=2 and lista_out[b]!=2):
            lista_in[a]=+1
            lista_out[b]+=1
            print(  a,b,randint(0,1))
            break

print("end")




