
def fill(matrix,x,y,size):
    if x< 0 or x>=size or y<0 or y>=size:
        return
    if matrix[x][y] =='0':
        return
    matrix[x][y] = '0'
    fill(matrix,x-1,y-1,size)
    fill(matrix,x-1, y,size)
    fill(matrix,x-1, y+1,size)
    fill(matrix,x, y-1,size)
    fill(matrix,x, y+1,size)
    fill(matrix,x+1, y-1,size)
    fill(matrix,x+1, y,size)
    fill(matrix,x+1, y+1,size)

def search(matrix, size,t):
    counter = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == '1':
                counter+=1
                fill(matrix,i,j,size)
    print("Image number",t, "contains",counter,"war eagles.")

t=0
while True:
    try:
        size = int(input())
        matrix = []
        for a in range(size):
            matrix.append(list(input()))
        t+=1
        search(matrix, size,t)
    except EOFError:
        break
