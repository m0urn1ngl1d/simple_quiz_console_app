
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
    if float(result) == given_answer:
        return "CORRECT"
    return "WRONG"

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

# declare dictionary for statistics output

statistic_dictionary = {"CORRECT": 0, "WRONG": 0} 

# base math operators

math_operators = {0: "/", 1: "*", 2: "-", 3: "+"}

# use random

num_1 = random.randrange(0, 100) 
num_2 = random.randrange(1, 100)
operator = random.choice(math_operators)

# print task for user to solve
print("=" * 100)
print(num_1, operator, num_2)

# input answer
given_answer = check_input()
first_input = True
# I won't explain it...
# Ok... Nah

while given_answer != "q":
    count = 0                                                                        # to count "CORRECT" and "WRONG"
    result = solve_and_check(num_1, num_2, operator, float(given_answer))           # solve task to check user
    print("YOUR ANSWER IS:", result)                                                                    # print CORRECT" or "WRONG"
    print("=" * 100)
    if result == "CORRECT":
        statistic_dictionary["CORRECT"] = statistic_dictionary.get("CORRECT", 0) + 1 # count amount of "CORRECT". ADD VALUE to dictionary
    elif result == "WRONG":
        statistic_dictionary["WRONG"] = statistic_dictionary.get("WRONG", 0) + 1     # count amount of "WRONG". ADD VALUE to dictionary
    num_1 = random.randrange(0, 100)    
    num_2 = random.randrange(1, 100)
    operator = random.choice(math_operators)
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