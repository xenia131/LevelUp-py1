import json

a1 = input("answer the question 1: ")
a2 = input("answer the question 2: ")
a3 = input("answer the question 3: ")

dct = {
    "data": '21.10.2022',
    "answer_1": a1,
    "answer_2": a2,
    "answer_3": a3
} 



with open("quiz-json.json", 'w') as json_f:
    answs = json.dump(dct, json_f, indent=4)

