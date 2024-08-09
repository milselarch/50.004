class Solution:
    @staticmethod
    def expand(s, start, end):
        last_start, last_end = None, None

        while (start >= 0) and (end < len(s)) and (s[start] == s[end]):
            last_start, last_end = start, end
            start -= 1
            end += 1

        if last_start is not None:
            # print('STR', (last_start, last_end), s[last_start:last_end+1])
            pass

        return last_start, last_end

    def countSubstrings(self, s: str) -> int:
        num_palindromes = 0

        for k in range(len(s)):
            p1 = self.expand(s, start=k, end=k)  # odd palindromes
            # print('P1', p1)
            p2 = self.expand(s, start=k - 1, end=k)  # even palindromes
            # print('P2', p2)

            if None not in p1:
                start, end = p1
                num_palindromes += 1 + (end - start) // 2
            if None not in p2:
                start, end = p2
                num_palindromes += (1 + end - start) // 2

        return num_palindromes


if __name__ == '__main__':
    solution = Solution()
    test = 'aaa'
    ans = solution.countSubstrings(test)
    print('ANS', ans)