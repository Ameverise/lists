def create_phone_number(lst: list) -> str:
    """Решение для Задачи 1"""
    return f"({lst[0]}{lst[1]}{lst[2]}) {lst[3]}{lst[4]}{lst[5]}-{lst[6]}{lst[7]}{lst[8]}{lst[9]}"


def duplicate_encode(text: str) -> str:
    """Решение для Задачи 2"""
    text_lower = text.lower()
    result = ""

    for char in text_lower:
        if text_lower.count(char) == 1:
            result += "("
        else:
            result += ")"

    return result


def is_valid_walk(walk: list) -> bool:
    """Решение для Задачи 3"""
    if len(walk) != 10:
        return False

    x = 0
    y = 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1

    return x == 0 and y == 0


def move_zeros(lst: list) -> list:
    """Решение для Задачи 4"""
    non_zeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    return non_zeros + zeros


def find_uniq(lst: list):
    """Решение для Задачи 5"""
    for num in lst:
        if lst.count(num) == 1:
            return num