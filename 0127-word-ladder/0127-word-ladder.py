from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, dist = queue.popleft()            
            if word == endWord:
                return dist
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i+1:]                    
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, dist + 1))        
        return 0
