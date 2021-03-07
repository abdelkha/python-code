def fizz_buzz():
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


if __name__ == '__main__':
    fizz_buzz()
