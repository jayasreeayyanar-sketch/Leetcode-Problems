class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}
        def dfs(string):
            if string in memo:
                return memo[string]
            if not string:
                return [""]            
            res = []
            for i in range(1, len(string) + 1):
                prefix = string[:i]                
                if prefix in word_set:
                    suffixes = dfs(string[i:])
                    for suffix in suffixes:
                        if suffix:
                            res.append(prefix + " " + suffix)
                        else:
                            res.append(prefix)            
            memo[string] = res
            return res
        return dfs(s)
