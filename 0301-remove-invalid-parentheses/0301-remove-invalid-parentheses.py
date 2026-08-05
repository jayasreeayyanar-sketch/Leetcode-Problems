class Solution(object):
    def removeInvalidParentheses(self, s):
        left_remove = 0
        right_remove = 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove == 0:
                    right_remove += 1
                else:
                    left_remove -= 1
        result = set()
        def dfs(index, left_count, right_count, left_remove, right_remove, path):
            if index == len(s):
                if left_remove == 0 and right_remove == 0:
                    result.add(path)
                return
            ch = s[index]
            if ch == '(' and left_remove > 0:
                dfs(index + 1, left_count, right_count,
                    left_remove - 1, right_remove, path)
            if ch == ')' and right_remove > 0:
                dfs(index + 1, left_count, right_count,
                    left_remove, right_remove - 1, path)
            if ch != '(' and ch != ')':
                dfs(index + 1, left_count, right_count,
                    left_remove, right_remove, path + ch)
            elif ch == '(':
                dfs(index + 1, left_count + 1, right_count,
                    left_remove, right_remove, path + ch)
            elif ch == ')' and left_count > right_count:
                dfs(index + 1, left_count, right_count + 1,
                    left_remove, right_remove, path + ch)
        dfs(0, 0, 0, left_remove, right_remove, "")
        return list(result)