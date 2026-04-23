class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            for i in range(start, min(start + 3, len(s))):
                part = s[start:i + 1]
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue
                path.append(part)
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result