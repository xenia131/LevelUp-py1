#import pickle
import json

with open("quiz-json.json", 'rb') as json_f:
    answers = json.load(json_f)
with open("answers.json", 'rb') as json_ans:
    rights = json.load(json_ans)

score = 0
'''if answers['answer_1'] in ['Hi', 'Hello', 'Hola']:
    score +=1
if answers['answer_2'] in ['Hi', 'Hello', 'Hola']:
    score +=1
if answers['answer_3'] in ['Hi', 'Hello', 'Hola']:
    score +=1'''

if answers['answer_1'] == rights['answer_1']:
    score += 1
if answers['answer_2'] == rights['answer_2']:
    score += 1
if answers['answer_3'] == rights['answer_3']:
    score += 1

print(score)