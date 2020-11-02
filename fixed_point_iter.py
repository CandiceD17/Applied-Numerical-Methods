import math
import numpy as np
import random
import matplotlib.pyplot as plt


def g(x):
    return math.pi + 0.5 * math.sin(x/2)


def fixed_point_iter(p0, max_iters, abs_tol):
    p_cur = p0
    ps = [p0]  # an array to store the past results
    for i in range(1, max_iters+1):
        p_next = g(p_cur)
        func_error = abs(p_next - g(p_next))
        step_error = abs(p_next - p_cur)
        if func_error < abs_tol or step_error <abs_tol:
            break
        ps.append(p_next)
        p_cur = p_next
    return ps, p_next


def graph(p, ps):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    y1 = [abs(v - p) for v in ps]  # calculate |p_n - p| for every n
    y2 = []
    y3 = [abs(g(v) - v) for v in ps]  # calculate |g(p_n) - p_n| for every n
    for i in range(len(ps) - 1):
        y2.append(abs(ps[i + 1] - ps[i]))  # calculate |p_n - p_n-1| for every n
    x1 = np.arange(1, len(ps) + 1)  # create an array from 1 to # of iterations + 1
    x2 = np.arange(1, len(ps))
    ax3.plot(x1, y1)
    ax3.set(xlabel='iterations', title='|p_n - p|')
    ax2.plot(x2, y2)
    ax2.set(xlabel='iterations', title='|p_n - p_n-1|')
    ax1.plot(x1, y3)
    ax1.set(xlabel='iterations', title='|g(p_n) - p_n')
    plt.show()


def main():
    p0 = random.uniform(0, 2 * math.pi) # generate a random number in [0, 2pi] as p0
    ps, root = fixed_point_iter(p0, 20, pow(10, -4))
    graph(root, ps)
    print(root)


if __name__ == '__main__':
    main()
