
def P_F(i, N):
    return 1 / ((1 + i) ** N)


def P_A(i, N):
    return (1 - P_F(i, N)) / i

def A_P(i, N):
    return 1 / P_A(i, N)

PF_15_4 = P_F(0.15, 4)
print("PF_15_4 = ", PF_15_4)
PF_15_8 = P_F(0.15, 8)
print("PF_15_8 = ", PF_15_8)
PA_15_8 = P_A(0.15, 8)
print("PA_15_8 = ", PA_15_8)

AP_15_8 = A_P(0.15, 8)
print("AP_15_8 = ", AP_15_8)

PW_MX = - 200000 - (200000 * PF_15_4) + (5000 * PF_15_4) + (5000 * PF_15_8) - (10000 * PA_15_8) - (200000 * 2 * PA_15_8)
print("PW_MX = ", PW_MX)

PW_MKJ = -350000 - (20000 * PA_15_8) - (1.5 * 200000 * PA_15_8) + (20000 * PF_15_8)
print("PW_MKJ = ", PW_MKJ)

AW_MX = PW_MX * A_P(0.15, 8)
print("AW_MX = ", AW_MX)

AW_MKJ = PW_MKJ * A_P(0.15, 8)
print("AW_MKJ = ", AW_MKJ)

AW_MX_4 = PW_MX * A_P(0.15, 4)
print("AW_MX_4 = ", AW_MX_4)