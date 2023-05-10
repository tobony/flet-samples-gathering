""" Navigation Class """
from flet import (
    UserControl,
    Row,
    PopupMenuItem,
    PopupMenuButton,
)

from views import NavSelection


class Navigation(UserControl):
    def __init__(self, visibility):
        self.visibility = visibility
        super().__init__()

    def build(self):
        # NAVIGATION: visbility if FALSE until size reaches a min. WIDTH
        self._navigation = Row(
            visible=self.visibility,
            alignment="start",
            controls=[
                PopupMenuButton(
                    items=[
                        PopupMenuItem(
                            text="Colors",
                            on_click=lambda e: NavSelection(e),
                        ),
                        PopupMenuItem(
                            text="Animations",
                            on_click=lambda e: NavSelection(e),
                        ),
                        PopupMenuItem(
                            text="Gradients",
                            on_click=lambda e: NavSelection(e),
                        ),
                    ]
                )
            ],
        )

        return self._navigation
