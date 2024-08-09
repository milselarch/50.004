class Solution:
    def get_palindrome(self, s: str, start=0, end=0, cache=None):
        cache = {} if cache is None else cache
        cache_key = (start, end)
        print('CACHE', cache_key)

        if cache_key in cache:
            return cache[cache_key]

        if start == end:
            return s[start]
        elif min(start, end) < 0:
            return ''
        elif max(start, end) > len(s) - 1:
            return ''
        elif start > end:
            return ''
        elif end - start == 1:
            if s[start] == s[end]:
                return s[start] + s[end]
            else:
                return ''

        sub_palindrome = self.get_palindrome(
            s=s, start=start + 1, end=end - 1, cache=cache
        )

        if (sub_palindrome != '') and (s[start] == s[end]):
            result = s[start] + sub_palindrome + s[end]
            cache[cache_key] = result
        else:
            cache[cache_key] = ''

        return cache[cache_key]

    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        cache = {}
        end = 0

        while end < len(s):
            start = end

            while True:
                p1 = self.get_palindrome(
                    s=s, start=start-1, end=end+1, cache=cache
                )
                p2 = self.get_palindrome(
                    s=s, start=start-1, end=end, cache=cache
                )

                if len(p1) > len(p2):
                    palindrome = p1
                    start -= 1
                    end += 1
                else:
                    palindrome = p2
                    start -= 1

                if len(palindrome) > len(longest):
                    longest = palindrome
                if len(palindrome) == 0:
                    break

        return longest


if __name__ == '__main__':
    solution = Solution()
    test = 'ccc'
    ans = solution.longestPalindrome(test)
    print('ANS', ans)
