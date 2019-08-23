# Write your answer here
# When you are done test your solution by running `python3 test.py solution.py`


def d(v_i, v_f, t):
    return (v_i + v_f) * 0.5 * t


def solve(lines, dt=0.01):

    v_x = 0
    v_y = 0
    v_z = 0

    d_x = 0
    d_y = 0
    d_z = 0

    t = 0

    for line in lines:

        t += dt

        a_x = line[0]
        a_y = line[1]
        a_z = line[2]

        v_x_i = v_x
        v_x += a_x * dt
        v_y_i = v_y
        v_y += a_y * dt
        v_z_i = v_z
        v_z += a_z * dt

        d_x += d(v_x_i, v_x, dt)
        d_y += d(v_y_i, v_y, dt)
        d_z += d(v_z_i, v_z, dt)

        # print(f"A - {a_x:>8.3f} {a_y:>8.3f} {a_z:>8.3f}")
        # print(f"V - {v_x_i:>8.3f} {v_y_i:>8.3f} {v_z_i:>8.3f}")
        # print(f"V - {v_x:>8.3f} {v_y:>8.3f} {v_z:>8.3f}")
        # print(f"D - {d_x:>8.3f} {d_y:>8.3f} {d_z:>8.3f}")
        # print(f"---{t}")

    return (d_x, d_y, d_z)


count = int(input())

lines = []
for i in range(count):
    line = input()
    lines.append([float(n) for n in line.split()])

r = solve(lines, 0.1)
# print(r)
print(f"{r[0]:>1.1f} {r[1]:>1.1f} {r[2]:>1.1f}")
