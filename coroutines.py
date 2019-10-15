import random
from typing import Set
from collections.abc import Coroutine


class Coroutines:

    __coroutines: Set[Coroutine]
    __completed_coroutines: Set[Coroutine]
    __new_coroutines: Set[Coroutine]
    __updating: bool

    def __init__(self):
        self.__updating = False
        self.__coroutines = set()
        self.__completed_coroutines = set()
        self.__new_coroutines = set()
        pass

    def start(self, coroutine: Coroutine) -> Coroutine:
        coroutine.__next__()
        if self.__updating:
            self.__new_coroutines.add(coroutine)
        else:
            self.__coroutines.add(coroutine)
        return coroutine

    def stop_all(self, func=None):
        if func is None:
            for coroutine in self.__coroutines:
                coroutine.close()
                self.__completed_coroutines.add(coroutine)
        else:
            self.stop_all_with_name(func.__qualname__)

    def stop_all_with_name(self, qualname: str):
        for coroutine in self.__coroutines:
            if coroutine.__qualname__ == qualname:
                self.stop(coroutine)

    def stop(self, coroutine: Coroutine):
        if coroutine not in self.__coroutines:
            return
        coroutine.close()
        self.__completed_coroutines.add(coroutine)

    def update(self, dt: float):
        self.__updating = True
        for co in self.__coroutines:
            try:
                co.send(dt)
            except StopIteration:
                self.__completed_coroutines.add(co)
        self.__updating = False

        if len(self.__completed_coroutines) > 0:
            for co in self.__completed_coroutines:
                self.__coroutines.remove(co)
            self.__completed_coroutines.clear()
        pass

        if len(self.__new_coroutines) > 0:
            for co in self.__new_coroutines:
                self.__coroutines.add(co)
            self.__new_coroutines.clear()

    @staticmethod
    def co_wait(time: float = 0):
        time -= yield
        while time > 0:
            time -= yield

    @staticmethod
    def co_wait_random(min: float, max: float):
        yield from Coroutines.co_wait(random.uniform(min, max))
