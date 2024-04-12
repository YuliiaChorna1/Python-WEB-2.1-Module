from typing import List
from typing import Dict
from typing import Union

# Псевдонім Списку інтів або флоатів
Data = List[float | int]

def my_mul(data: Data) -> float:
    result = 1
    for num in data:
        result *= result
        return result

my_mul([1, 2, 3])


# Псевдонім Словника
dict_of_users: Dict[int, str] = {1: "Jane", 2: "John"}


# Типи союзів Union
Number = Union[float, int]

def add(x: Number, y: Number) -> Number:
    return x + y


# Союзи після Python 3.10 не потрібні:
def add2(x: float | int, y: float | int) -> float | int:
    return x + y
