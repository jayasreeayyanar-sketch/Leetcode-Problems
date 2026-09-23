class Solution(object):
    def outerTrees(self, trees):
        def cross_product(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        trees.sort()

        if len(trees) <= 3:
            return trees
            
        lower = []
        for p in trees:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
            
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
            
        unique_points = set(tuple(p) for p in lower + upper)        
        return [list(p) for p in unique_points]
