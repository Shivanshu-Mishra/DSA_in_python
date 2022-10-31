import argparse

def arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("expression", help="Enter prefix/postfix expression to evaluate")
    parser.add_argument("--type", help="Enter supplied expression type pre or post")
    return parser.parse_args()

class InfixEvaluator:
    operators=("+","-","/","*","^")
    def __init__(self,expression):
        self.expression=expression
        self.stack=[]
    def evaluate(self):
        for element in self.expression:
            if element in InfixEvaluator.operators:
                self.operand2=int(self.stack.pop())
                self.operand1=int(self.stack.pop())
                result=self.performOperation(element)
                self.stack.append(result)
            elif str.isalnum(element):
                self.stack.append(element)
            else:
                raise Exception("Operation not permitted");
        return self.stack.pop()


    def performOperation(self,operator):
        if operator=="+":
            return self.operand1+self.operand2
        elif operator=="-":
            return self.operand1-self.operand2
        elif operator=="*":
            return self.operand1*self.operand2
        elif operator=="/":
            return self.operand1/self.operand2
        elif operator=="^":
            return pow(self.operand1,self.operand2)



if __name__=="__main__":
    args=arguments()
    infix=InfixEvaluator(args.expression)
    print(infix.evaluate())