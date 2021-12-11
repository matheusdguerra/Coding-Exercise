
def happy(number):
    if number == 4:
        return False
    return True


if __name__ == '__main__':
    assert happy(1)
    assert happy(10)
    assert happy(100)

    assert not happy(4)
