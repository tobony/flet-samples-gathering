from flet import (
    UserControl,
    Container,
    animation,
    alignment,
    IconButton,
    Text,
    icons,
    Row,
    transform,
    colors,
)

from flet.transform import Scale
import time


class Button(UserControl):
    global SendCount
    SendCount = True

    def __int__(self):
        super().__int__()

    def build(self):
        self.text = Text(
            "SEND",
            size=15,
            text_align="start",
            weight="w700",
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(duration=900, curve="decelerate"),
            animate_opacity=200,
        )

        self.button = IconButton(
            icon=icons.SEND_SHARP,
            icon_size=16,
            icon_color="white",
            offset=transform.Offset(0, 0),  # position
            animate_offset=animation.Animation(900),  # speed
            rotate=transform.Rotate(11, alignment=alignment.center),
            animate_rotation=animation.Animation(duration=600, curve="decelerate"),
            scale=Scale(scale=1),
            animate_scale=animation.Animation(600, "bounceOut"),
        )

        self.MainContainer = Container(
            width=300,
            height=300,
            # aspect_ratio=1,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=Container(
                width=130,
                height=45,
                bgcolor=colors.BLUE_600,
                border_radius=10,
                on_hover=lambda e: self.SendButtonAnimation(e),
                content=Row(
                    alignment="center",
                    vertical_alignment="center",
                    spacing=0,
                    tight=True,
                    controls=[
                        self.button,
                        self.text,
                    ],
                ),
            ),
        )

        return self.MainContainer

    def SendButtonAnimation(self, e):
        global SendCount
        if e.data == "false":
            SendCount = False

            self.button.rotate.angle -= 1.5
            self.button.offset = transform.Offset(0, 0)
            self.button.scale = transform.Scale(1)
            self.button.update()

            self.text.offset = transform.Offset(0, 0)
            self.text.opacity = 1
            self.text.update()

        else:
            SendCount = True

            self.button.rotate.angle += 1.5
            self.button.offset = transform.Offset(0.5, 0)
            self.button.scale = transform.Scale(1.25)
            self.button.update()

            self.text.offset = transform.Offset(1, 0)
            self.text.opacity = 0
            self.text.update()

        while SendCount == True:
            self.button.offset = transform.Offset(0.5, 0.09)
            self.button.update()
            time.sleep(0.9)
            if SendCount == False:
                self.button.offset = transform.Offset(0, 0)
                self.button.update()
                break
            self.button.offset = transform.Offset(0.5, -0.09)
            self.button.update()
            time.sleep(0.9)
            if SendCount == False:
                self.button.offset = transform.Offset(0, 0)
                self.button.update()
                break
