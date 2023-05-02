import builtins

from pytest_mock import MockerFixture
from main import custom_sum


class TestCustomSum:
    def test_should_sum_two_positive_numbers_correctly(self, mocker: MockerFixture):
        # Arrange
        print_spy = mocker.spy(builtins, "print")

        # Act
        result = custom_sum(1, 1)

        # Assert
        print_spy.assert_called_once_with("Summing 1 and 1")
        assert result == 2
