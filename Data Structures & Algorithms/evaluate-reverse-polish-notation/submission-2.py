

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)

            elif i == '*':
                stack.append(stack.pop() * stack.pop())

            elif i == '/':
                right, left = stack.pop(), stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(i))
        return stack[0]


            


            

        
