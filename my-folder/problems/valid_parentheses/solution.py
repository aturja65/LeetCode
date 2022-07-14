class Solution:
    def __init__(self):
        self.left_list=['(','{','[']
        self.right_list=[')','}',']']
    def isValid(self, s: str) -> bool:
        stack=[]
        for value in s:
            if value in self.left_list:
                stack.append(value)
            if value in self.right_list:
                if len(stack)==0:
                    return False
                top=stack.pop(-1)
                if not self.checkBracket(top,value):
                    return False
        if stack ==[]:
            return True
        else:
            return False
    def checkBracket(self,left,right):
        return self.left_list.index(left)==self.right_list.index(right)