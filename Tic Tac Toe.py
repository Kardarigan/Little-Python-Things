import random
import os 
a, b, c = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'] 

def insert(a, b, c, sign, pos): 
    if 1 <= pos <= 3: 
        a[pos - 1] = sign 
    elif 4 <= pos <= 6: 
        b[pos - 4] = sign 
    elif 7 <= pos <= 9: 
        c[pos - 7] = sign 
    return a, b, c 

def validation(pos):
    if 1 <= pos <= 3:
        if a[pos - 1] != '-':
            return False
    elif 4 <= pos <= 6: 
        if b[pos - 4] != '-':
            return False
    elif 7 <= pos <= 9: 
        if c[pos - 7] != '-':
            return False
    return True

def check_win(a, b, c, sign): 
# rows 
    if a[0] == sign and a[1] == sign and a[2] == sign: 
        return True 
    elif b[0] == sign and b[1] == sign and b[2] == sign: 
        return True 
    elif c[0] == sign and c[1] == sign and c[2] == sign: 
        return True 
# columns 
    elif a[0] == sign and b[0] == sign and c[0] == sign: 
        return True 
    elif a[1] == sign and b[1] == sign and c[1] == sign: 
        return True 
    elif a[2] == sign and b[2] == sign and c[2] == sign: 
        return True 
# diagonal 
    elif a[0] == sign and b[1] == sign and c[2] == sign: 
        return True 
    elif a[2] == sign and b[1] == sign and c[0] == sign: 
        return True 
    return False

def is_finished(a, b, c, result): 
    if result: 
        return True
        
    elif b[0] != '-' and b[1] != '-' and b[2] != '-' and a[0] != '-' and a[1] != '-' and a[2] != '-' and c[0] != '-' and c[1] != '-' and c[2] != '-': 
        return True
    
    return False 

def make_row(r): 
    row = '| ' + r[0] + ' | ' + r[1] + ' | ' + r[2] + ' |'
    return row 

def make_table(a, b, c):
    row_a = make_row(a) 
    row_b = make_row(b) 
    row_c = make_row(c) 
    table = ('_' * 13) + '\n' + row_a + '\n' + row_b + '\n' + row_c +  '\n' +  ('¯' * 13)
    print(table) 


ended = False 

while not is_finished(a, b, c, ended): 
    make_table(a, b, c) 
    command = input("enter your sign and number: ") 
    params = command.split() 
    sign = params[0] 
    pos = int(params[1])
    a, b, c = insert(a, b, c, sign, pos) 
    cpos = random.randint(1, 9)
    while not validation(cpos):
        cpos = random.randint(1, 9)
    a, b, c = insert(a, b, c, 'x', cpos)
      
    
    if check_win(a, b, c, sign): 
        make_table(a, b, c) 
        print(sign + ' is our winner!') 
        ended = True 
        
if not ended: 
    make_table(a, b, c) 
    print('draw')



# make_table(a, b, c)
# pos = int(input("Enter the pos (1-9): "))
# a, b, c = insert(a, b, c, sign, pos)

# if check_win(a, b, c, sign):
#     make_table(a, b, c)
#     print(sign + ' is the winner!')
#     ended = True
# else:
#     sign = 'O' if sign == 'X' else 'X' 🐱‍💻