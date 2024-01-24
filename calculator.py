import tkinter as tk 

white = "#fff"
black = "#070504"
primeColor = "#000"
secondColor = "yellow"

smallFont = ("Arial", 16)
middleFont = ("Arial", 24)
middleBoldFont = ("Arial", 24, "bold")
largFont = ("Arial", 40, "bold")


class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("250x300")
        self.window.resizable(False, False)
        self.window.title("Calculator")

        self.totalExpression = ''
        self.currentExpression = ''
        
        
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} 

        self.displayFrame = self.createDisplayFrame()
        self.buttonFrame = self.createButtonFrame()
        self.totalLabel, self.currentLabel = self.createDisplayLabels()
        
        self.buttonFrame.rowconfigure(0, weight=1)
        for z in range(1,5):
            self.buttonFrame.rowconfigure(z, weight=1)
            self.buttonFrame.columnconfigure(z, weight=1)
        self.createButtons()
        self.displayFrame = self.createDisplayFrame()
        self.digitButton = self.createDigit()
        self.bindKeyboard()

    def createButtons(self):
        self.createOperator()
        self.createClear()
        self.createEquals()
        self.createSquare()
        self.createSquareRoot()
        
    def createDisplayLabels(self):
        totalLabel = tk.Label(self.displayFrame, text=self.totalExpression, anchor= tk.E, bg=primeColor,fg=white,
                              padx=24, font=smallFont)
        totalLabel.pack(expand=True,fill="both")
        
        currentLabel = tk.Label(self.displayFrame, text=self.currentExpression, anchor= tk.E, bg=primeColor,fg=white,
                              padx=24, font=largFont)
        currentLabel.pack(expand=True,fill="both")

        return totalLabel, currentLabel

    def createDisplayFrame(self):
        frame = tk.Frame(self.window, height=221, bg=primeColor)
        frame.pack(expand=True, fill="both")
        return frame
    
    def createButtonFrame(self):
        frame = tk.Frame(self.window, bg=primeColor)
        frame.pack(expand=True, fill="both")
        return frame

    def updateTotalLabel(self):
        expression = self.totalExpression
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.totalLabel.config(text=expression)
    
    def updateCurrentLabel(self):
        self.currentLabel.config(text=self.currentExpression[:7])
            
    def addToExpression(self, value):
        self.currentExpression += str(value)
        self.updateCurrentLabel()
    
    def appendOperator(self, operator):
        self.currentExpression += operator
        self.totalExpression += self.currentExpression
        self.currentExpression = ""
        self.updateCurrentLabel()
        self.updateTotalLabel()
    
    def clear(self):
        self.currentExpression = ''
        self.totalExpression = ''
        self.updateCurrentLabel()
        self.updateTotalLabel()
    
    def square(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**2"))
        self.updateCurrentLabel()
        
    def squareRoot(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
        self.updateCurrentLabel()
    
    def createDigit(self):
        for digit, gridPos in self.digits.items():
            button = tk.Button(self.buttonFrame, text=str(digit), bg=black, fg=white, font=middleBoldFont, borderwidth=0, command=lambda z=digit: self.addToExpression(z))
            button.grid(row=gridPos[0], column=gridPos[1], sticky=tk.NSEW)

    def createOperator(self):
        rowNum = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttonFrame, text=symbol, bg=secondColor, fg=primeColor, font=middleFont, borderwidth=0, command=lambda z=operator: self.appendOperator(z))
            button.grid(row= rowNum, column=4, sticky=tk.NSEW)
            rowNum+=1
        
    def createClear(self):
        button = tk.Button(self.buttonFrame, text="C", bg=secondColor, fg=primeColor, font=middleFont, borderwidth=0, command= self.clear)
        button.grid(row= 0, column=1, sticky=tk.NSEW)
    
    def createEquals(self):
        button = tk.Button(self.buttonFrame, text="=", bg=secondColor, fg=primeColor, font=middleFont, borderwidth=0, command=self.evaluation)
        button.grid(row= 4, column=3, columnspan=2, sticky=tk.NSEW)
    
    def createSquare(self):
        button = tk.Button(self.buttonFrame, text="x\u00b2", bg=secondColor, fg=primeColor, font=middleFont, borderwidth=0, command=self.square)
        button.grid(row= 0, column=2, sticky=tk.NSEW)
            
    def createSquareRoot(self):
        button = tk.Button(self.buttonFrame, text="\u221ax", bg=secondColor, fg=primeColor, font=middleFont, borderwidth=0, command=self.squareRoot)
        button.grid(row= 0, column=3, sticky=tk.NSEW)
        
    def evaluation(self):
        try:
            self.totalExpression += self.currentExpression
            self.currentExpression = str(eval(self.totalExpression))
            if self.currentExpression != self.totalExpression:
                self.totalExpression = ""
        except Exception as e:
            self.currentExpression = "Error"
        finally:
            self.updateTotalLabel()
            self.updateCurrentLabel()
            
    def bindKeyboard(self):
        self.window.bind("<Return>", lambda event: self.evaluation())
        for key in self.digits:
            self.window.bind(str(key), lambda event, z=key: self.addToExpression(z))
        for key in self.operators:
            self.window.bind(key, lambda event, z=key: self.appendOperator(z))
           
    def run(self):
        self.window.mainloop()

calculator

if __name__=='__main__':
    calc = calculator()
    calc.run()