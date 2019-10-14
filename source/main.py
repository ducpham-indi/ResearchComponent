from component import Component
import G
import components


class Main(Component):

    cam = None  # components.Camera

    def start(self):
        pass

    def setup(self, cam: components.Camera):
        self.cam = cam

        cam.targetShowcaseIndex = 0
        pass

    def update(self):
        pass
