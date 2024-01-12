import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[len(numbers) - 1] = numbers[len(numbers) - 1], numbers[index]
    index = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[len(numbers) - 2] = numbers[len(numbers) - 2], numbers[index]
    return numbers[len(numbers) - 1] * numbers[len(numbers) - 2]

def stress_test():
    n, m = map(int, input().split())
    while True:
        n = random.randint(2, n)
        A = [random.randint(0, m) for _ in range(n+1)]

        print(A)

        result1 = max_pairwise_product(A)
        result2 = max_pairwise_product_fast(A)

        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer:", result1, result2)
            return

if __name__ == '__main__':
    stress_test()
