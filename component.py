from __future__ import annotations
import gameobject as module_gameobject
import typing
from coroutines import Coroutines
import G

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transform import Transform


class Component:

    go: module_gameobject.GameObject
    coroutines: Coroutines
    transform: Transform
    __started: False

    def __init__(self, go: module_gameobject.GameObject, *args):
        self.__started = False
        self.go = go
        self.transform = self.go.transform
        self.coroutines = Coroutines()
        self.init(*args)

    def init(self, *args):
        pass

    def _start(self):
        if self.__started:
            return
        self.__started = True
        self.start()
        pass

    def _update(self):
        self.coroutines.update(G.ELAPSED_TIME)
        self.update()
        pass

    def start(self):
        pass

    def update(self):
        pass
