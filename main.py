import pytest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Выяисляет является ли числа полиндромом
        :param x:
        :return:
        '''
        c = 1
        c += 1
        print(c)
        return str(x) == str(x)[::1]

@pytest.mark.parametrize("input_value, expected", [(123, False),
                                                   (111, True),
                                                   (222, True)])
def test_palindrome(input_value, expected):
    sol = Solution()
    assert sol.isPalindrome(input_value) is expected

