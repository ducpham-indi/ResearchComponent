from __future__ import annotations
from gameobject import *
import typing


class Component:

    go: GameObject

    def __init__(self, go: GameObject, *args):
        self.go = go
        self.init(*args)

    def init(self, *args):
        raise NotImplementedError
