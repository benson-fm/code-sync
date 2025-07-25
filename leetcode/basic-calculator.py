class Solution:
    def calculate(self, s: str) -> int:
        
        # the strategey is that you go throughs and you make it a stack
        # do the case scenario with the + - ( )
        # instead of using isalnum you could also use isdigit
        # for the num in getting the full thing you could just 
            # change it to num = num * 10 + int(char)
            # what this does is that lets say for 780,
            # num = 7
            # num = 7 * 10 + 8
            # num = 78 * 10 + 0
        # for plus 
            # we add to the result * sign
            # num = 0
            # sign = 1
        # for minus
            # add to the result * sign
            # num = 0
            # sign = -1
        # for (
            # push to the stack
        # for )
            # pop from the stack 
            # multiply and stuff

        stack = []
        result = 0
        sign = 1
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += num * sign
                num = 0
                sign = 1
            elif char == '-':
                result += num * sign
                num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                num = 0
            elif char == ')':
                print(result, stack)
                result += sign * num
                result *= stack.pop(-1)
                result += stack.pop(-1)
                sign = 1
                num = 0
        return result + (sign * num)