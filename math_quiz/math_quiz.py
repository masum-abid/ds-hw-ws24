import random


def rand_num(min, max):
    """
    function to create random integer number between min and max.
    """

    return random.randint(min, max)

def rand_choice():
    ''' function for randome operator selection'''

    return random.choice(['+', '-', '*'])


def math_ops(num1, num2, operation):
      ''' function to do math operation '''

    problem = f"{num1} {operation} {num2}" #represent the generated problem
    if operation == '+':
        answer = num1 + num2 #error resolved from '-' to '+'
    elif operation == '-':
        answer = num1 - num2 #error resolved from '+' to '-'
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
     '''
    function to create questions and take user input as answer
    '''

    sum = 0
    time_quiz = int(3.14159265359) #floating number converted to integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for num in range(time_quiz):
        num1 = rand_num(1, 10); num2 = rand_num(1, 5.5); operation = rand_choice()

        PROBLEM, ANSWER = math_ops(num1, num2, operation)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Error: Please enter a valid integer.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            sum += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {sum}/{time_quiz}")

if __name__ == "__main__":
    math_quiz()
