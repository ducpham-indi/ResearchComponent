from component import Component
import G


class Ground(Component):
    def init(self, a, b, c):
        print(G.px)
        print("INIT GROUND OBJECT HERE")
        print(a)
        print(b)
        print(c)
