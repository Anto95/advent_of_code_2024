def ex_03_0():
    SUM=0
    with open('test/03_0.txt') as f:
        for line in f.readlines():
            for mul_candidate in line.split("mul("):
                mul_candidate = mul_candidate.split(")")[0]
                multipliers = mul_candidate.split(",")
                if len(multipliers) != 2:
                    continue
                a,b = multipliers
                try:
                    if str(int(a)) == a and str(int(b)) == b:
                        SUM += int(a) * int(b)
                except:
                    continue
    return SUM


def ex_03_1():
    def grep_do_dont(mul_candidate, DO):
        print("MUL  CANDIDATES", DO, mul_candidate)
        do_candidate = mul_candidate.split("do()")
        if len(do_candidate) > 1:
            DO = True
        print("DO   CANDIDATES", DO, do_candidate)
        dont_candidate = do_candidate[-1].split("don't()")
        if len(dont_candidate) > 1:
            DO = False
        print("DONT CANDIDATES", DO, dont_candidate)
        print()
        return DO

    SUM=0
    DO = True
    with open('test/03_1.txt') as f:
        for line in f.readlines():
            for mul_candidate in line.split("mul("):
                multipliers_candidate = mul_candidate.split(")")[0]
                multipliers = multipliers_candidate.split(",")
                if len(multipliers) != 2:
                    DO = grep_do_dont(mul_candidate, DO)
                    continue
                a,b = multipliers
                try:
                    if str(int(a)) == a and str(int(b)) == b and DO:
                        SUM += int(a) * int(b)
                    DO = grep_do_dont(mul_candidate, DO)
                except:
                    DO = grep_do_dont(mul_candidate, DO)
                    continue
                DO = grep_do_dont(mul_candidate, DO)
    return SUM

print(ex_03_0())
print(ex_03_1())