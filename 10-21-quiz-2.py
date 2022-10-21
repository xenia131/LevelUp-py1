import json

with open("quiz-json.json", 'rb') as json_f:
    answers = json.load(json_f)

score = 0
if answers['answer_1'] in ['Hi', 'Hello', 'Hola']:
    score +=1
if answers['answer_2'] in ['Hi', 'Hello', 'Hola']:
    score +=1
if answers['answer_3'] in ['Hi', 'Hello', 'Hola']:
    score +=1

print(score)