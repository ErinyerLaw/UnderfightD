from main import *
import pytest
import builtins
import pygame


def test_fpsset():
    for x in range(2):
        for y in range(2):
            assert fpsset(x, y) == 10 or fpsset(
                x, y) == 60 or fpsset(x, y) == 80


def test_fpsset_wrong():
    for x in range(2, 100):
        for y in range(2, 100):
            assert fpsset(x, y) == 'Wrong input'


def test_attackm():
    m = attackm(100)
    for i in range(len(m)):
        assert (m[i][0] == 0 and m[i][1] != 0) or (
            m[i][1] == 0 and m[i][0] != 0)


def test_hp_decor():
    for i in range(1, 100):
        assert hp_decor(i) == abs(hp_decor(i))
    for i in range(0, -100, -1):
        assert hp_decor(i) == 0

