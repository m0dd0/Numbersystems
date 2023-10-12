from typing import Union


class Value:
    DEFAULT_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(
        self, value: Union[int, str, "Value"], base: int = None, alphabet: str = None
    ) -> None:
        self._validate_base_and_alphabet(base, alphabet)

        if alphabet is None:
            alphabet = self.DEFAULT_ALPHABET[:base]
        self._alphabet = alphabet

        self._int_value = None
        if isinstance(value, int):
            if value < 0:
                raise ValueError("value must be positive")
            self._int_value = value
        elif isinstance(value, str):
            if len(value) == 0:
                raise ValueError("value must not be empty")
            if set(value) - set(self._alphabet):
                raise ValueError("value must only contain characters from alphabet")
            self._int_value = self._str_value_2_int_value(value)
        elif isinstance(value, Value):
            self._int_value = int(value)
        else:
            raise TypeError("value must be int, str or Value")

    def _validate_base_and_alphabet(self, base: int, alphabet: str) -> None:
        if base is None and alphabet is None:
            raise ValueError("base or alphabet must be provided")

        if alphabet is not None:
            if len(alphabet) != len(set(alphabet)):
                raise ValueError("alphabet must not contain duplicate characters")
            if len(alphabet) < 2:
                raise ValueError("alphabet must contain at least 2 characters")
        if base is not None:
            if base < 2:
                raise ValueError("base must be greater than 1")

        if base is not None and alphabet is not None:
            if base != len(alphabet):
                raise ValueError("base and alphabet must be compatible")

        if base is not None and alphabet is None:
            if base > len(self.DEFAULT_ALPHABET):
                raise ValueError("base is too large")

    def _str_value_2_int_value(self, value: str) -> int:
        val = 0
        for i, c in enumerate(value[::-1]):
            val += self._alphabet.index(c) * (len(self._alphabet) ** i)
        return val

    def _int_value_2_str_value(self) -> str:
        if self._int_value == 0:
            return self._alphabet[0]
        val = ""
        v = self._int_value
        while v > 0:
            val = self._alphabet[v % len(self._alphabet)] + val
            v //= len(self._alphabet)
        return val

    def to(self, base: int = None, alphabet: str = None) -> "Value":
        return Value(self._int_value, base, alphabet)

    @property
    def base(self) -> int:
        return len(self._alphabet)

    def __repr__(self):
        return f"value: {self._int_value_2_str_value()}\ndecimal_value: {self._int_value}\nbase: {self.base}\nalphabet: '{self._alphabet}'"

    def __int__(self):
        return self._int_value

    def __eq__(self, other):
        return int(self) == int(other)

    def __ne__(self, other):
        return int(self) != int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __add__(self, other):
        return Value(int(self) + int(other), self.base)

    def __sub__(self, other):
        return Value(int(self) - int(other), self.base)

    def __mul__(self, other):
        return Value(int(self) * int(other), self.base)

    def __floordiv__(self, other):
        return Value(int(self) // int(other), self.base)

    def __mod__(self, other):
        return Value(int(self) % int(other), self.base)

    def __pow__(self, other):
        return Value(int(self) ** int(other), self.base)


if __name__ == "__main__":
    pub_key = Value("751e76e8199196d454941c45d1b3a323f1433bd6", 16)
