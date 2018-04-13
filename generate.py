import math
import matplotlib.pyplot as plt


def _get_b(b1, b2, t, u,
           ep1: 'Нулевое мат.ожидание'=0,
           ep2: 'Нулевое мат.ожидание'=0):
    if t <= u:
        return b1 * (1 + ep1)
    else:
        return b2 * (1 + ep2)


def get_model(M: 'Число периодов' = 1,
              dt: 'Дискрета времени(временной шаг)' = 0.01,
              A: '[Ap, Aq, Ar, As, Ast, At]' = (0.08, -0.227, 0.72, -0.18, 0, 0.2),
              b1: '[bp, bq, br, bs, bst, bt]' = (0.016, 0.01, 0.01, 0.015, 0.04, 0.05),
              b2: '[bp, bq, br, bs, bst, bt]' = (0.016, 0.01, 0.01, 0.015, 0.04, 0.023),
              u: 'up, uq, ur, us, ust, ut' = (0.18, 0.25, 0.28, 0.315, 0.38, 0.531)):
    y = []
    x = []
    for m in range(M):
        t = 0
        t_end = 1
        while t < t_end:
            summ = 0
            for i in range(6):
                summ += A[i] * math.exp(-((t - u[i]) ** 2) / (2 * (_get_b(b1[i], b2[i], t, u[i]) ** 2)))
            y.append(summ)
            x.append(m + t)
            t += dt
    plt.plot(x, y)
    plt.grid(True)
    plt.show()


get_model(M=2)

