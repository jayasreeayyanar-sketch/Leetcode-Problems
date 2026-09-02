class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        words.sort(key=len)
        word_set = set()
        result = []        
        def can_form(word, memo):
            if not word:
                return True
            if word in memo:
                return memo[word]
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in word_set and can_form(word[i:], memo):
                    memo[word] = True
                    return True
                    
            memo[word] = False
            return False
        for word in words:
            if not word:
                continue
            if can_form(word, {}):
                result.append(word)              
            
            word_set.add(word)            
        return result
