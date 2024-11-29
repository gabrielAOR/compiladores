import sys
from antlr4 import *
from DesenharLexer import DesenharLexer
from DesenharParser import DesenharParser 
from DesenharVisitor import DesenharVisitor
import turtle

class TurtleInterpreter(DesenharVisitor):
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        self.screen.mainloop()

    def visitMove(self, ctx):
        distance = int(ctx.INT().getText())
        self.turtle.forward(distance)

    def visitTurn(self, ctx):
        angle = int(ctx.INT().getText())
        self.turtle.right(angle)

    def visitPen(self, ctx):
        if ctx.getText() == 'PENUP;':
            self.turtle.penup()
        else:
            self.turtle.pendown()

    def visitColor(self, ctx):
        color = ctx.COLOR().getText().lower()
        self.turtle.color(color)

    def visitRepeat(self, ctx):
        times = int(ctx.INT().getText())
        for _ in range(times):
            for stmt in ctx.statement():
                self.visit(stmt)

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = DesenharLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DesenharParser(stream)
    tree = parser.program()
    interpreter = TurtleInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main()
