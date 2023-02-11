

def P_F(i, N):
    return 1 / ((1 + i) ** N)


def P_A(i, N):
    return (1 - P_F(i, N)) / i

PF_11_5 = P_F(0.11, 5)
print("PF_11_5 = ", PF_11_5)
PF_11_10 = P_F(0.11, 10)
print("PF_11_10 = ", PF_11_10)
PA_11_10 = P_A(0.11, 10)
print("PA_11_10 = ", PA_11_10)

PW_K2 = -125000 - (125000 * PF_11_5) + (20000 * PF_11_5) + (20000 * PF_11_10) + (50000 * PA_11_10)
print("PW_K2 = ", PW_K2)

PW_M7 = -150000 + (30000 * PF_11_10) + (60000 * PA_11_10)
print("PW_M7 = ", PW_M7)
