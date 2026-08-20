class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i=0
        temp ="none"
        
        while i<len(s):
            if s[i] in "([{":
                stack.append(s[i])
            
                i +=1
                
            else:
                if not stack:
                    return False
                

                if  (s[i] == "]" and stack[-1] == "[") or (s[i] == "}" and stack[-1] == "{") or (s[i] == ")" and stack[-1] == "("):
                    stack.pop()
                    

                else:
                    return False

                i=i+1

        if len(stack) == 0:
            return True

        return False
