file = open("2023/day1/day1-input.txt")


def part_one():
    sum = 0

    for line in file:
        num = ""
        first = None
        last = None
        for char in line:
            if char.isdigit() and first == None:
                first = char
            elif char.isdigit() and first != None:
                last = char

        if last:
            num = str(first) + str(last)
        else:
            num = str(first) * 2

        sum = sum + int(num)

    return sum


mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def part_two():
    with open("2023/day1/day1-input.txt") as f:
        data = f.read()
        for name, value in mapping.items():
            data = data.replace(name, value)

        lines = data.splitlines()

    res = 0

    for line in lines:
        num = ""
        for char in line:
            if char.isdigit():
                num += char
                break

        for char in line[::-1]:
            if char.isdigit():
                num += char
                break

        res += int(num)

    return res


print(part_one())
print(part_two())
