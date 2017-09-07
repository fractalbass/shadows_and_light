# Plot of the Lorenz Attractor based on Edward Lorenz's 1963 "Deterministic
# Nonperiodic Flow" publication.
# http://journals.ametsoc.org/doi/abs/10.1175/1520-0469%281963%29020%3C0130%3ADNF%3E2.0.CO%3B2
#
# Note: Because this is a simple non-linear ODE, it would be more easily
#       done using SciPy's ode solver, but this approach depends only
#       upon NumPy.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Lorenz:

    def lorenz(self,x ,y, z, s=10, r=28, b=2.667):
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot

    def calculate(self, xi, yi, zi):
        dt = 0.01
        stepCnt = 900

        # Need one more for the initial values
        xs = np.empty((stepCnt + 1,))
        ys = np.empty((stepCnt + 1,))
        zs = np.empty((stepCnt + 1,))

        # Setting initial values
        xs[0], ys[0], zs[0] = (xi, yi, zi)

        # Stepping through "time".
        for i in range(stepCnt):
            # Derivatives of the X, Y, Z state
            x_dot, y_dot, z_dot = self.lorenz(xs[i], ys[i], zs[i])
            xs[i + 1] = xs[i] + (x_dot * dt)
            ys[i + 1] = ys[i] + (y_dot * dt)
            zs[i + 1] = zs[i] + (z_dot * dt)

        print("Last location: {0}, {1}, {2}".format(xs[-1], ys[-1], zs[-1]))
        return (xs, ys, zs)

    def plot(self, attractors):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for attractor in attractors:
            ax.plot(attractor["xs"], attractor["ys"], attractor["zs"], lw=0.5, color=attractor["c"])
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Y Axis")
            ax.set_zlabel("Z Axis")
            ax.set_title("Lorenz Attractor")

        plt.show()

if __name__ == "__main__":
    print("got to here.")
    lorenz = Lorenz()
    attractors = list()

    xs, ys, zs = lorenz.calculate(0., 1., 1.05)
    attractor = {"xs": xs, "ys": ys, "zs": zs, "c": "b"}
    attractors.append(attractor)

    xs2, ys2, zs2 = lorenz.calculate(0., 1., 1.051)
    attractor2 = {"xs": xs2, "ys": ys2, "zs": zs2, "c": "r"}
    attractors.append(attractor2)

    lorenz.plot(attractors)