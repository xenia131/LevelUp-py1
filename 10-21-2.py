student_ids, student_names, student_grades = list(input().split()), list(input().split()), list(input().split())
dct, result = {}, {}

for k, v, m in zip(student_ids, student_names, student_grades):
    result[k] = {v: int(m)}
print(result)

