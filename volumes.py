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


def torus_volume(major_r, inner_r):
    """ torus function, takes major radius and minor radius, makes sure they are positive values,
    then returns the volume """
    if major_r < 0 or inner_r < 0:
        return ValueError
    else:
        vol_tor = (pi * inner_r ** 2) * (2 * pi * major_r)
        return vol_tor


if __name__ == "__main__":
    x = (cylinder_volume(2, 5))
    y = (pi * 2**2 * 5)
    print("Is the volume function returning an acceptable value: " + str(isclose(x, y)))

    z = cylinder_volume(2, -5)
    print(z)

    a = torus_volume(5, 1)
    b = (pi * 1**2)*(2*pi*5)
    print("Is the torus function returning an acceptable value: " + str(isclose(a, b)))

    g = torus_volume(5, -1)
    print(g)
