import math

while(True):
    n = int(input("Please enter the number of menu(1 to 5) : "))
    if n == 1:
        temp = int(input("Enter the F : "))
        print(f'{(temp - 32) * 5 / 9:.4f}')
    elif n == 2:
        temp = int(input("Enter the C : "))
        print(f'{(temp * 9 / 5) + 32:.4f}')
    elif n == 3:
        n = int(input("Enter the number : "))
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(n, "is Not 소수")
                break
        else:
            if (n > 2):
                print(n, "is 소수")
            else:
                print(n, "is Not 소수")
    elif n == 4:
        M, N = map(int, input("Enter the number1 number2 : ").split())
        if M > N:
            tmp = M
            M = N
            N = tmp
        list_prime = [1 for i in range(N + 1)]
        list_prime[0] = 0
        list_prime[1] = 0
        for j in range(2, int(math.sqrt(N)) + 1):
            if list_prime[j] == 1:
                k = 2
                while(j * k <= N):
                    list_prime[j * k] = 0
                    k += 1
        for w in range(M, N + 1):
            if list_prime[w] == 1:
                print(w, end=' ')
        print()
    elif n == 5:
        print("Bye!")
        break
    else:
        print("Please enter the number 1 to 5")