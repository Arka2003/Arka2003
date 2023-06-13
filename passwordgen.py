import string, random

def combination():
    s = list()
    s.extend(list(string.ascii_letters))
    s.extend(list(string.digits))
    s.extend(list(string.punctuation))
    return s


def generator(value):
    s = combination()
    pasw = list()
    random.shuffle(s)

    for x in range(int(value)):
        pasw.append(random.choice(s))
    return "".join(pasw)


if __name__ == '__main__':
    value = input()
    print(generator(value))