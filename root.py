import time, os, os.path
import G
import gameloader
import components
import source.main
import source.autorot


def run_dev():
    # run as a dev environment.
    # this run setting will load the file source/main.py and expect class Main(Component)
    # as a default component

    G.window(True, 480, 640)
    clear_camera = G.camera("clear")
    clear_showcase = G.showcase("clear")
    for i in range(0, 8):
        G.SHOWCASES.append(G.showcase("3dcase"))
    G.SCENE = G.Scene("Main scene")

    # TODO: CHANGE MAIN HERE, WE NOT USING IT AT ALL
    from source.main import Main

    G.GameObject.Create("Main gameplay object").add_component(Main())
    # init main component

    while True:

        G.DT = G.ELAPSED_TIME = G.getElapsedTime()

        # moveVector = G.vec3(0.0, 0.0, 0.0)

        # touch = G.singleTouch()
        # if touch is not None:
        #     if touch["is_pressed"]:
        #         print("ASDASDSD")
        #     moveVector = G.vec3(
        #         touch["cur_x"] - touch["org_x"], 0, -(touch["cur_y"] - touch["org_y"])
        #     )
        #     moveVector = G.vec3(cam.camera.viewInverseMatrix * moveVector)

        for go in G.SCENE.gameobjects:
            go.awake()  # awake inactivated components

        for go in G.SCENE.gameobjects:
            go.start()  # start inactivated components

        for go in G.SCENE.gameobjects:
            go.update()  # update the components

        clear_camera.shoot(clear_showcase, clearColor=True)

        for go in G.SCENE.gameobjects:
            go.try_render_camera()  # render the camera components

        G.swap()
        G.SCENE.update_collections()


def run_scene():
    # todo: later
    pass


def run_lib():
    # todo: export this as a lib to be used later
    pass


if __name__ == "__main__":
    run_dev()
