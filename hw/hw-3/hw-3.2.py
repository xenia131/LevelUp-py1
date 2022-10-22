from hw_3_module_2 import reading, calcs

expr = calcs()
res = {
        expr[1] == '+': int(expr[0]) + int(expr[2]),
        expr[1] == '-': int(expr[0]) - int(expr[2]),
        expr[1] == '*': int(expr[0]) * int(expr[2]),
        expr[1] == '/' and expr[2] != '0': int(expr[0]) / int(expr[2]) if expr[2] != '0' else 'error',
        expr[1] not in ['+', '-', '*', '/']: 'error'
    }
       
print(res[True])
