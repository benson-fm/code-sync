class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for item in s:
            if item in mapping:
                if len(stack) > 0 and stack[-1] == mapping[item]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(item)


        return not stack