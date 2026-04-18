class Solution:
    def isValid(self, s: str) -> bool:
        match = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in match:
                if stack and stack[-1] == match[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return stack == []
