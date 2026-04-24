from collections import deque, defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        layer = {beginWord}
        parents = defaultdict(set)        
        while layer and endWord not in parents:
            next_layer = defaultdict(set)
            for word in layer:
                if word in wordSet:
                    wordSet.remove(word)            
            for word in layer:
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        neighbor = word[:i] + char + word[i+1:]
                        if neighbor in wordSet:
                            next_layer[neighbor].add(word)
            for word, p_set in next_layer.items():
                parents[word].update(p_set)
            layer = next_layer.keys()
        def backtrack(word):
            if word == beginWord:
                return [[beginWord]]
            res = []
            for p in parents[word]:
                for path in backtrack(p):
                    res.append(path + [word])
            return res            
        return backtrack(endWord)
