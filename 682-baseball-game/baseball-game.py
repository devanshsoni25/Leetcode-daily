class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for num in operations:
            if num != '+' and num != 'D' and num != 'C' :
                stack.append(int(num))

            elif num == "D":
                if len(stack)!=0:
                    stack.append(stack[-1]*2)

            elif num == "+":
                if len(stack)>=2:
                    stack.append(stack[-1]+stack[-2])

            elif num == "C":
                stack.pop()

        return sum(stack)