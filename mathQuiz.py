import random
import operator as op
while True:
    num1 = int(random.random() * 10) * int(random.random() * 10)
    num2 = int(random.random() * 10) * int(random.random() * 10)
    operators = {"+":op.add,"-":op.sub,"x":op.mul,"÷":op.truediv}
    sybole ,operator = random.choice(list(operators.items()))
    currectAnswer = (operator(num1, num2))
    
    print(f'Quiz: {num1} {sybole} {num2}')
    humanAnswer = int(input("Whats your anwser?: "))
    if humanAnswer == currectAnswer:
        print('That is Currect!')
        input("Press a Key to Rematch...")
    else:
        print(f'That is incurrect :)\nCurrect answer is {currectAnswer}')
        input("Press a Key to Rematch...")
