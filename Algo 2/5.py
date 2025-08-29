class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def no_of_magical_numbers(mid):
            return (mid//a + mid//b - (mid*gcd(a, b))//(a*b))

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        l = min(a, b)
        r = n * (l)
        ans = 0
        while l <= r:
            m = l + (r-l)//2
            no = no_of_magical_numbers(m)

            if no < n:
                l = m + 1
            else:
                ans = m
                r = m - 1

        return ans % (10**9 + 7)            



