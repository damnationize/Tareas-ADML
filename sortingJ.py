numbers = input("Ingrese los números separados por una coma: ")
numbers = [int(n) for n in numbers.split(',')]

end = len(numbers) - 1

while end != 0:

    for i in range(end):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    end = end - 1

    
print(numbers)