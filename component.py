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
    __woke: False

    def __init__(self):
        self.__started = False
        self.__woke = False
        self.coroutines = Coroutines()

    def _awake(self):
        if self.__woke:
            return
        self.__woke = True
        self.awake()
        pass

    def awake(self):
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

    def _kill(self):
        self.kill()
        pass

    def kill(self):
        pass

    def as_new_gameobject(self, name="Noname"):
        go = module_gameobject.GameObject.Create(name)
        go.add_component(self)
        return go
