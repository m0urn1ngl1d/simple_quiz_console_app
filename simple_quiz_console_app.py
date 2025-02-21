
import random

# use math operators
def solve_and_check(num1, num2, operator, given_answer):
    if operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    if float(result) != given_answer:
        return "WRONG", float(result)
    return "CORRECT"

# check answer if answer is string - ask for number
def check_input(given_answer=None):
    if given_answer is None:
        given_answer = input("Type answer: ")
    if given_answer != "q":
        try:
            float(given_answer)
            return given_answer
        except ValueError:
            print("INPUT A NUMBER!!!") 
            return check_input(input("Type answer: ")) 
           
    return given_answer

# increased rate to get division
def make_div_great_again():
    num1 = random.randrange(0, 100)
    num2 = random.randrange(1, 100)
    operator = "/"
    if operator == "/" and num1 % num2 != 0:
        return make_div_great_again()
    return num1, num2, operator

# use random
def make_random(func):
    math_operators = ["/", "*", "-", "+"]
    num1 = random.randrange(0, 100)
    num2 = random.randrange(1, 100)
    operator = random.choice(math_operators)
    if operator == "/" and num1 % num2 != 0:
        return func
    elif operator == "-" and num2 > num1:
        return make_random()
    return num1, num2, operator


# declare dictionary for statistics output
statistic_dictionary = {"CORRECT": 0, "WRONG": 0} 

# use make_random func to make random numbers
num_1, num_2, operator = make_random(make_div_great_again())

# print task for user to solve
print("=" * 100)
print(num_1, operator, num_2)

# input answer
given_answer = check_input()
first_input = True
# I won't explain it...
# Ok... Nah

while given_answer != "q":
    count = 0                                                                        
    result = solve_and_check(num_1, num_2, operator, float(given_answer))           
    print("YOUR ANSWER IS:", *(result if type(result) == tuple else (result,))) 
    print("=" * 100)
    if result == "CORRECT":
        statistic_dictionary["CORRECT"] = statistic_dictionary.get("CORRECT", 0) + 1 
    elif result[0] == "WRONG":
        statistic_dictionary["WRONG"] = statistic_dictionary.get("WRONG", 0) + 1    
    num_1, num_2, operator = make_random(make_div_great_again())
    print(num_1, operator, num_2)
    given_answer = check_input()
    first_input = False

# count OUTPUPUT
if statistic_dictionary["WRONG"] > 0:
    output = statistic_dictionary["CORRECT"] / (statistic_dictionary["WRONG"] + statistic_dictionary["CORRECT"]) * 100
elif first_input:
    output = 0.0
else:
    output = 100.0

# print OUTPUT
print("=" * 100)
print(f"You have: {round(output, 1)}% correct answers")