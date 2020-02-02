# new power function


def int_NewPower(x, int_N=2):
    int_S = 1
    while int_N > 0:
        int_S = int_S*x
        int_N = int_N-1
    return int_S

print(int_NewPower(2,10))

