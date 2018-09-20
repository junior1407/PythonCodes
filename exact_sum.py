
def bin_search(books, start, end, dinheiro, livro):

    saldo = dinheiro- livro
    global solutions
    if (start> end):
        return
    if (saldo<=0):
        return
    mid = (start+end)//2
    if (books[mid] == saldo):
        solutions.append((livro,books[mid]))
    elif (books[mid] < saldo):
        bin_search(books, mid+1, end, dinheiro, livro)
    elif (books[mid] > saldo):
        bin_search(books, start, mid-1, dinheiro, livro)


while(True):
    try:
        solutions = []
        n_livros = int(input())
        books= input().split()
        dinheiro = int(input())
        for i in range(len(books)):
            books[i] = int(books[i])
        books.sort()
        for i in range(len(books)):
            bin_search(books,i+1,len(books)-1, dinheiro, books[i])
        melhor =0
        for i in range(len(solutions)):
            if abs(solutions[i][0] - solutions[i][1]) < abs(solutions[melhor][0] - solutions[melhor][1]):
                melhor =i
        print("Peter should buy books whose prices are ",solutions[melhor][0]," and ",solutions[melhor][1],".",sep="")
        print()
        input()

    except EOFError or ValueError:
        break


