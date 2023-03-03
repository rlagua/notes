import pytest


class TestYu:
    def test_1(self):
        print("111111")
        assert 1 == 2


if __name__ == '__main__':
    pytest.main([__file__])
