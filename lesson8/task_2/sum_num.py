def sum_num(num: str) -> int:
    return sum(map(int, filter(lambda i: i.isdigit(), str(num))))