from flet import (
    UserControl,
    Container,
    animation,
    alignment,
    IconButton,
    Text,
    icons,
    Column,
    Row,
    transform,
)
import time


class Button(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):

        self.IconList = [
            icons.FACEBOOK,
            icons.SHARE_SHARP,
            icons.TIKTOK_SHARP,
        ]

        self.IconRow = Row(
            alignment="center",
            vertical_alignment="center",
        )

        for icon_ in self.IconList:
            _icon = IconButton(
                icon=icon_,
                icon_size=22,
                icon_color="white",
                offset=transform.Offset(0, -0.9),
                animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
                animate_opacity=500,
            )
            self.IconRow.controls.append(_icon)

        self.text = Text(
            "BUTTON",
            weight="w900",
            size=18,
            offset=transform.Offset(0, -1),
            animate_offset=animation.Animation(duration=800, curve="elasticOut"),
        )

        self.MainContainer = Container(
            width=300,
            height=300,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=Container(
                width=180,
                height=50,
                bgcolor="blue",
                on_hover=lambda e: self.SocailAnimation(e),
                border_radius=8,
                alignment=alignment.center,
                content=Column(
                    spacing=0,
                    alignment="center",
                    horizontal_alignment="center",
                    controls=[
                        self.IconRow,
                        Row(
                            alignment="center",
                            controls=[
                                self.text,
                            ],
                        ),
                    ],
                ),
            ),
        )

        return self.MainContainer

    def SocailAnimation(self, e):
        if e.data == "false":
            for icon in self.IconRow.controls[:]:
                icon.offset = transform.Offset(0, -0.9)
                icon.update()
                time.sleep(0.1)

            self.text.offset = transform.Offset(0, -1)
            self.text.update()

        else:

            self.text.offset = transform.Offset(0, 0.5)
            self.text.update()

            for icon in self.IconRow.controls[:]:
                icon.offset = transform.Offset(0, 0.15)
                icon.update()
                time.sleep(0.1)
