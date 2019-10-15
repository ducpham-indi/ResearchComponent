import typing
import G


class Sapphi(G.Component):
    def start(self):
        figure = G.components.Figure(
            "Sapphiart/Sapphiart",
            ["Sapphiart@idle", "Sapphiart@walk", "Sapphiart@running"],
        )
        figure.change_anim("Sapphiart@running")

        self.go.add_component(figure)
