from typing import Any

from src.decorators import log


@log()
def divide_element(x: int) -> float:
    return x / x


def test_log_without_filename(capsys: Any) -> Any:
    divide_element(0)
    captured = capsys.readouterr()
    assert captured.out == "divide_element error: division by zero. Inputs: (0,), {}\n"

    divide_element(10)
    captured = capsys.readouterr()
    assert captured.out == "divide_element ok\n"


def test_log_with_filename() -> Any:
    @log("my_file.txt")
    def divide_element_to_write(x: int) -> float:
        return x / x

    assert divide_element_to_write(10) == 1.0
    assert divide_element_to_write(0) is None
