import pytest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Выяисляет является ли числа полиндромом
        :param x:
        :return:
        '''
        return str(x) == str(x)[::1]
#какой-то коментарий
# еще один комментарий
# последний комментарий
@pytest.mark.parametrize("input_value, expected", [(123, False),
                                                   (111, True),
                                                   (222, True)])
def test_palindrome(input_value, expected):
    sol = Solution()
    assert sol.isPalindrome(input_value) is expected

