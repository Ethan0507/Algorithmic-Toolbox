# python3
import random

def max_naive(numbers):
    max_curr = -1
    for i in range(len(numbers)):
        for j in range(i + 1 ,len(numbers)):
            if numbers[i] * numbers[j] > max_curr:
                max_curr = numbers[i] * numbers[j]
    return max_curr

def max_pairwise_product(numbers):
    n = len(numbers)
    max1 = 0
    max2 = n - 1
    j = n - 1
    for i in range(n):
        if numbers[i] > numbers[max1] and i != max2:
            max1 = i
        if numbers[j] > numbers[max2] and max1 != j:
            max2 = j
        j -= 1
    # for i in range(n):
    #     if max1 == -1 or numbers[i] > numbers[max1]:
    #         max1 = i
    # for j in range(n):
    #     if max2 == -1 and j != max1 or numbers[j] > numbers[max2]  and j != max1:
    #         max2 = j
    return numbers[max1] * numbers[max2]


if __name__ == '__main__':
    while(1) :
        rand_n = random.randrange(2,100)
        print(rand_n)
        l1 = []
        for i in range(rand_n):
            l1.append(random.randint(0,100000))
        print(l1)
        x1 = max_naive(l1)
        x2 = max_pairwise_product(l1)
        if (x1 != x2):
            print("Wrong!"+str(x1)+" "+str(x2))
            break
        else:
            print("Ok")

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
