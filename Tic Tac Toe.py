import os 
a, b, c = ['-', '-', '-', ], ['-', '-', '-'], ['-', '-', '-'] 

def insert(a, b, c, turn, pos): 
    if 1 <= pos <= 3: 
        a[pos - 1] = turn 
    elif 4 <= pos <= 6: 
        b[pos - 4] = turn 
    elif 7 <= pos <= 9: 
        c[pos - 7] = turn 
    return a, b, c 

def check_win(a, b, c, turn): 
# rows 
    if a[0] == turn and a[1] == turn and a[2] == turn: 
        return True 
    elif b[0] == turn and b[1] == turn and b[2] == turn: 
        return True 
    elif c[0] == turn and c[1] == turn and c[2] == turn: 
        return True 
# columns 
    elif a[0] == turn and b[0] == turn and c[0] == turn: 
        return True 
    elif a[1] == turn and b[1] == turn and c[1] == turn: 
        return True 
    elif a[2] == turn and b[2] == turn and c[2] == turn: 
        return True 
# diagonal 
    elif a[0] == turn and b[1] == turn and c[2] == turn: 
        return True 
    elif a[2] == turn and b[1] == turn and c[0] == turn: 
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

def print_board(a, b, c):
    row_a = make_row(a) 
    row_b = make_row(b) 
    row_c = make_row(c) 
    table = ('_' * 13) + '\n' + row_a + '\n' + row_b + '\n' + row_c +  '\n' +  ('¯' * 13)
    print(table) 


ended = False 

while not is_finished(a, b, c, ended): 
    print_board(a, b, c) 
    command = input("enter your sign and number: ") 
    params = command.split() 
    turn = params[0] 
    pos = int(params[1])
    a, b, c = insert(a, b, c, turn, pos) 

    if check_win(a, b, c, turn): 
        print_board(a, b, c) 
        print(turn + ' is the winner!') 
        ended = True 
        
if not ended: 
    print_board(a, b, c) 
    print('draw')



# print_board(a, b, c)
# pos = int(input("Enter the pos (1-9): "))
# a, b, c = insert(a, b, c, turn, pos)

# if check_win(a, b, c, turn):
#     print_board(a, b, c)
#     print(turn + ' is the winner!')
#     ended = True
# else:
#     turn = 'O' if turn == 'X' else 'X' 🐱‍💻