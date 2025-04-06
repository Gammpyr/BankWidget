from functools import wraps
from typing import Any


def log(filename: str = "") -> Any:
    """Регистрирует детали выполнения функций (время вызова, имя функции, передаваемые аргументы,
    результат выполнения и информация об ошибках"""

    def wrapper(function: Any) -> Any:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            func_name = function.__name__

            try:
                result = function(*args, **kwargs)

            except Exception as err:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func_name} error: {err}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func_name} error: {err}. Inputs: {args}, {kwargs}")
            else:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func_name} ok")
                else:
                    print(f"{func_name} ok")
                return result

        return inner

    return wrapper
