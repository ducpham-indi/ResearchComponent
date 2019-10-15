from __future__ import annotations
import typing

import gameobject as module_gameobject
import component as module_component
from coroutines import Coroutines
import G


class Scene:

    name: str
    __gameobjects: typing.Set[module_gameobject.GameObject]
    __new_gameobjects: typing.Set[module_gameobject.GameObject]
    __dead_gameobjects: typing.Set[module_gameobject.GameObject]

    def __init__(self, name: str):
        self.name = name
        self.__gameobjects = set()
        self.__new_gameobjects = set()
        self.__dead_gameobjects = set()
        self.__pending_gameobjects = set()

    def add_gameobject(self, gameobject):
        self.__new_gameobjects.add(gameobject)
        pass

    def update_collections(self):
        if len(self.__new_gameobjects) > 0:
            self.__gameobjects.update(self.__new_gameobjects)
            self.__new_gameobjects.clear()

        if len(self.__dead_gameobjects) <= 0:
            return
        self.__gameobjects.difference_update(self.__dead_gameobjects)
        self.__dead_gameobjects.clear()

    @property
    def gameobjects(self) -> typing.Iterable[module_gameobject.GameObject]:
        for go in self.__gameobjects:
            if go.dead:
                self.__dead_gameobjects.add(go)
            else:
                yield go
