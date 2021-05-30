# https://www.algoexpert.io/questions/Run-Length%20Encoding

def run_length_encoding(string: str) -> str:
    running_char = string[0]
    running_count = 1
    encoded_char_list = []

    for i in range(1, len(string)):
        char = string[i]
        if char != running_char or running_count == 9:
                encoded_char_list += [str(running_count), running_char]
                running_char = char
                running_count = 1
        else:
            running_count += 1

    encoded_char_list += [str(running_count), running_char]
    return "".join(encoded_char_list)


def test_0():
    assert run_length_encoding("AAAB122233") == "3A1B113223"


def test_1():
    assert run_length_encoding("aA") == "1a1A"


def test_2():
    assert run_length_encoding("AAAAAAAAAAAAABBCCCCDD") == "9A4A2B4C2D"
