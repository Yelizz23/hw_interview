import stack
import pytest


class Test:
    def set_up(self):
        print('Method setUp')

    @pytest.mark.parametrize('string_, expected_result', [
        ('({{[(())]}})', 'Сбалансировано'),
        ('(({{{(([[[]]]))}}}))', 'Сбалансировано'),
        ('[[[{{({})}}]]]', 'Сбалансировано'),
        ('([{}])', 'Сбалансировано'),
        ('({{}])', 'Несбалансировано'),
        ('{{((({[[]})))}}', 'Несбалансировано'),
        ('{]()}', 'Несбалансировано'),
        ('(({{}}[({])]', 'Несбалансировано')
    ])
    def test_check_balance(self, string_, expected_result):
        assert main.check_balance(string_) == expected_result
