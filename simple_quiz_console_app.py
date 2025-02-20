
import random

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

statistic_dictionary = {"CORRECT": 0, "WRONG": 0}
math_operators = {0: "/", 1: "*", 2: "-", 3: "+"}
num_1 = random.randrange(0, 100)
num_2 = random.randrange(1, 100)
operator = random.choice(math_operators)
print(num_1, operator, num_2)
give_answer = input("Type answer: ")

while give_answer != "q":
    count = 0
    result = solve_and_check(num_1, num_2, operator, float(give_answer))
    print(result)
    if result == "CORRECT":
        statistic_dictionary["CORRECT"] = statistic_dictionary.get("CORRECT", 0) + 1
    elif result == "WRONG":
        statistic_dictionary["WRONG"] = statistic_dictionary.get("WRONG", 0) + 1
    num_1 = random.randrange(0, 100)
    num_2 = random.randrange(1, 100)
    operator = random.choice(math_operators)
    print(num_1, operator, num_2)
    give_answer = input("Type answer: ")
if statistic_dictionary["WRONG"] > 0:
    output = statistic_dictionary["CORRECT"] / statistic_dictionary["WRONG"] * 100
else:
    output = 100.0
print(f"You have: {output}% correct answers")