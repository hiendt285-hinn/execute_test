def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Không chia cho 0")
    return a / b


if __name__ == "__main__":
    print(add(2, 3))
    print(divide(10, 2))
