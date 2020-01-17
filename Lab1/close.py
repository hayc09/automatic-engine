#!/usr/bin/env python3


def close(x, y, z):
    dif = abs(x-y)
    if dif < z:
        return True
    else:
        return False


if __name__ == "__main__":
    a = close(1, 2, 0.5)
    print(a)
    b = close(1, 2, 3)
    print(b)



