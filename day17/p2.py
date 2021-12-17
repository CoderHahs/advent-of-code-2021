from operator import ne
from numpy.lib.nanfunctions import nanargmax
import tools as t
import re

with open("day17/input.txt", encoding="utf-8") as f_d:
  x_1, x_2, y_1, y_2 = list(map(int, re.findall(r"-?\d+", f_d.read())))

def get_pos(vx0, vy0, current_time):
    current_y = vy0 * current_time - (current_time - 1) * (current_time) // 2

    # ignore -ve x as the input is to the right
    current_x = (
        (2 * vx0 - current_time + 1) * (current_time) // 2
        if current_time < vx0
        else vx0 * (vx0 + 1) // 2
    )

    return current_x, current_y

def will_intersect(current_v, upper_bound, lower_bound):
    tmin = t.math.floor(
        current_v[1] + t.math.sqrt(current_v[1] * current_v[1] - 2 * upper_bound[1])
    )
    tmax = t.math.floor(
        current_v[1] + t.math.sqrt(current_v[1] * current_v[1] - 2 * lower_bound[1])
    )

    for current_t in range(tmin, tmax + 2):
        current_x, current_y = get_pos(current_v[0], current_v[1], current_t)
        if (
            upper_bound[0] <= current_x <= lower_bound[0]
            and lower_bound[1] <= current_y <= upper_bound[1]
        ):
            return True
    return False

vy_min = y_1
vx_max = x_2

vy_max = -y_1
vx_min = t.math.floor(t.math.sqrt(2 * x_1) - 1)

upper_bound = (x_1, y_2)
lower_bound = (x_2, y_1)

tmp = sum(
    [
        will_intersect((vx, vy), upper_bound, lower_bound)
        for vx in range(vx_min, vx_max + 1)
        for vy in range(vy_min, vy_max + 1)
    ]
)

print(tmp)