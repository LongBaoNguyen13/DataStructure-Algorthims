def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number_fast(n):
    fib_list = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_fast(input_n))
