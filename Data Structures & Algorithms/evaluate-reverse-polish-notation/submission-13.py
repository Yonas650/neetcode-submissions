import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+': operator.add, '-': operator.sub,'*': operator.mul}
        stack=[]
        for token in tokens:
            if token in operators:
                num1=stack.pop()
                num2=stack.pop()    
                res=operators[token](num2,num1)
                stack.append(res)
            elif token=='/':
                num1=stack.pop()
                num2=stack.pop()    
                res=int(num2/num1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]