from __future__ import annotations
import G
from component import Component


class Ground(Component):
    def init(self, a, b, c):
        print("INIT GROUND OBJECT HERE")
        print(a)
        print(b)
        print(c)

        self.coroutines.start(self.test())

    def test(self):
        print("START")
        yield from self.coroutines.yield_wait(3)
        print("Stop")
