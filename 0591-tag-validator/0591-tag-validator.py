class Solution(object):
    def isValid(self, code):
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            if i > 0 and not stack:
                return False
                
            if code[i:i+9] == "<![CDATA[":
                if not stack:
                    return False
                cdata_end = code.find("]]>", i + 9)
                if cdata_end == -1:
                    return False
                i = cdata_end + 3
                
            # Handle Closing Tags: </TAG_NAME>
            elif code[i:i+2] == "</":
                tag_end = code.find(">", i + 2)
                if tag_end == -1:
                    return False
                tag_name = code[i+2:tag_end]
                
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = tag_end + 1
                
            elif code[i] == "<":
                tag_end = code.find(">", i + 1)
                if tag_end == -1:
                    return False
                tag_name = code[i+1:tag_end]
                if not (1 <= len(tag_name) <= 9) or not tag_name.isalpha() or not tag_name.isupper():
                    return False                    
                stack.append(tag_name)
                i = tag_end + 1
            else:
                i += 1
                
        return len(stack) == 0
