class Solution(object):
    def isNumber(self, s):
        s = s.strip()        
        numSeen = False
        dotSeen = False
        eSeen = False
        numAfterE = True        
        for i in range(len(s)):
            if s[i].isdigit():
                numSeen = True
                numAfterE = True            
            elif s[i] in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False            
            elif s[i] == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True            
            elif s[i] in ['e', 'E']:
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numAfterE = False            
            else:
                return False        
        return numSeen and numAfterE