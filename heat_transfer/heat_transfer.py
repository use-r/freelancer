import os
import numpy as np
import matplotlib.pyplot as plt

# parameters
Ca = 753  # J/(kg*K)
Cb = 897  # J/(kg*K)
ma = 100  # kg
mb = 1000  # kg
Ac = 0.0025  # m^2
Lc = 0.1  # m
kc = 205  # W/(m*K)
t_LEO = 100  # min
t_eclipse = 35  # min
t_max = 15 * t_LEO  # min
eps_a = 0.9
eps_b = 0.2
sigma = 5.67e-8  # W/(m^2*K^4)
A_surf_a = 2 * 7.5 * 2  # m^2
A_surf_b = 2 * 2 * 6  # m^2
A_irrad_a = 2 * 7.5  # m^2
A_irrad_b = 2 * 2  # m^2
Irr = 1366.1  # W/m^2

# convert the parameters for linear algebra calcuation
C = np.array([Ca, Cb])
m = np.array([ma, mb])
eps = np.array([eps_a, eps_b])
A_surf = np.array([A_surf_a, A_surf_b])
A_irrad = np.array([A_irrad_a, A_irrad_b])
sign = np.array([-1, 1])


# irradiance funtion
def irrad(t):
    if t - np.floor(t / t_LEO) * t_LEO > t_eclipse:
        return Irr
    else:
        return 0


# function to get the plot for task3
def task3():
    ts = np.arrage(0, t_max)  # time
    irr = [irrad(t) for t in ts]  # irradiance

    # display the result
    plt.figure()
    plt.plot(ts, irr)
    plt.show()


# function to get a right-hand-side of the function
def Tdot(t, T):
    Q_irr = eps * irrad(t) * A_irrad
    Q_rad = -eps * sigma * A_surf * T ** 4
    Q_internal = 3e3
    Q_conduction = sign * kc * Ac * (T[0] - T[1]) / Lc

    return (Q_irr + Q_rad + Q_internal + Q_conduction) / (m * C)


def rk3step(f, t0, y0, h):
    # calculate the next y using Eq. 2
    k1 = h * f(t0, y0)
    k2 = h * f(t0 + h / 2, y0 + k1 / 2)
    k3 = h * f(t0 + h, y0 - k1 + 2 * k2)

    return y0 + (k1 + 4 * k2 + k3) / 6


def main():
    t = [0]  # initial time value. This is a list not integer
    t_max = 15 * t_LEO  # max time value
    T = [np.array([300, 300])]  # initial temperature value
    h = 0.1  # time step

    while t[-1] <= t_max:
        # keep appending until t exceeds t_max
        T.append(rk3step(Tdot, t[-1], T[-1], h))
        t.append(t[-1] + h)

    Ta = [x[0] for x in T]  # temperature for the solar array
    Tb = [x[1] for x in T]  # temperature for the satellite body
    # display the resutl
    plt.figure()
    plt.plot(t, Ta, label='Solar array')
    plt.plot(t, Tb, label='Satellite body')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
    # task3()
