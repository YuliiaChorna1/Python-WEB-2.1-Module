from typing import TypeVar, Any


T = TypeVar("T", int, str, float)

# Generics

def calculator(x: T, y: T) -> T:
    return x + y

print(calculator(3, 5))
print(calculator("Hello", " world!"))
print(calculator(3.5, 1.4))

# Any

def calculator2(x: Any, y: Any) -> T:
    return x * y
