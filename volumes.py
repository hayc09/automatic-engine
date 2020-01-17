#!/usr/bin/env python3

from math import pi, isclose


def cylinder_volume(r, h):
    """ cylinder function, takes radius and height, makes sure they are positive values,
    then returns the volume """
    if r < 0 or h < 0:
        return ValueError
    else:
        vol = pi * (r ** 2) * h
        return vol


def torus_volume(inner_r, outer_r):
    """ torus function, takes inner radius and outer radius, makes sure they are positive values,
    converts to minor and major radius, then returns the volume """
    if inner_r < 0 or outer_r < 0:
        return ValueError
    else:
        minor_r = (outer_r - inner_r) / 2
        major_r = inner_r + minor_r
        vol_tor = (pi * minor_r ** 2) * (2 * pi * major_r)
        return vol_tor


if __name__ == "__main__":
    x = (cylinder_volume(2, 5))
    y = (pi * 2**2 * 5)
    print("Is the volume function returning an acceptable value: " + str(isclose(x, y)))

    z = cylinder_volume(2, -5)
    print(z)

    a = torus_volume(3, 4)
    b = (pi * 0.5**2)*(2*pi*3.5)
    print("Is the torus function returning an acceptable value: " + str(isclose(a, b)))

    g = torus_volume(5, -1)
    print(g)
