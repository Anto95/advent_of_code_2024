
def is_safe(numbers):
    small_diff, increasing, decreasing = True, True, True
    for a,b in zip(numbers[:-1], numbers[1:]):
        if abs(b-a) > 3 or b == a:
            small_diff = False
        if b > a:
            decreasing = False
        if a > b:
            increasing = False
    return (decreasing or increasing) and small_diff

def ex_02_0():
    SAFE = 0
    with open('test/02_0.txt') as f:
        for line in f.readlines():
            numbers = [int(x) for x in line.split()]
            SAFE += is_safe(numbers)
    return SAFE

def ex_02_1():
    SAFE = 0
    with open('test/02_0.txt') as f:
        for line in f.readlines():
            numbers = [int(x) for x in line.split()]
            if is_safe(numbers):
                SAFE += 1
                continue
            if is_safe(numbers[1:]):
                SAFE += 1
                continue
            for i in range(1,len(numbers)):
                if is_safe(numbers[:i] + numbers[i + 1:]):
                    SAFE += 1
                    break
    return SAFE

print(ex_02_0())
print(ex_02_1())