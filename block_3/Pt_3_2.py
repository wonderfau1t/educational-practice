fibonacci = lambda lim, n1, n2, sp: [sp.append(n1 + n2), fibonacci(lim, n2, n1 + n2, sp) if (n1 + n2) < (lim - n2) else sp.insert(1, 1)]

fib_numbers = [0]
fibonacci(int(input("Enter number: ")), 0, 1, fib_numbers)

print(f'Fibonacci numbers before: {fib_numbers}')
