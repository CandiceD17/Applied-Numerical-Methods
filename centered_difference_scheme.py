import matplotlib.pyplot as plt
import math
import numpy as np

def f(x):
    return 32 * pow(math.pi, 2) * math.sin(2 * math.pi * (2 * x - 1)) + 40

def u_func(x):
    return 2 * math.sin(2 * math.pi * (2 * x - 1)) - 20 * x * (x - 1)


def generate_nodes(num_nodes):
    nodes = [0]
    h = 1/(num_nodes+1)
    for i in range(num_nodes):
        nodes.append(nodes[-1] + h)
    nodes.pop(0)
    return h, nodes


def main():
    ns = [4, 16, 32, 64]
    for n in ns:
        h, nodes = generate_nodes(n)
        fs = np.ones(n)
        for i in range(n):
            fs[i] = pow(h, 2) * f(nodes[i])
        coeffs = np.zeros(shape=[n, n])
        for i in range(n):
            coeffs[i][i] = 2
            if i - 1 >= 0:
                coeffs[i][i-1] = -1
            if i + 1 < n:
                coeffs[i][i+1] = -1
        u = np.linalg.solve(coeffs, fs)
        nodes = np.insert(nodes, 0, 0)
        nodes = np.append(nodes, 1)
        u = np.insert(u, 0, 0)
        u = np.append(u, 0)
        plt.plot(nodes, u, label = "node = %i" %n)

    xs = np.linspace(0, 1, 100)
    true_u = []
    for x in xs:
        true_u.append(u_func(x))
    plt.plot(xs, true_u, "--", label = "u(x)")
    plt.legend(loc = "upper left")
    plt.show()




if __name__ == '__main__':
    main()
