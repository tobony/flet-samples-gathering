from flet import (
    UserControl,
    Container,
    animation,
    alignment,
    IconButton,
    Text,
    icons,
    padding,
    Row,
    transform,
    colors,
)


class Button(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):

        self.text = Text(
            "DELETE",
            size=11,
            weight="w600",
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(duration=900, curve="ease"),
            animate_opacity=200,
        )

        self.icon = IconButton(
            icon=icons.DELETE_ROUNDED,
            icon_size=23,
            icon_color="white",
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(duration=900, curve="ease"),
        )

        self.IconContainer = Container(
            alignment=alignment.center_right,
            padding=padding.only(top=5, bottom=5),
            animate=animation.Animation(1000, "ease"),
            content=Row(
                alignment="end",
                vertical_alignment="end",
                spacing=0,
                controls=[
                    self.icon,
                ],
            ),
        )

        self.MainContainer = Container(
            width=300,
            height=300,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=Container(
                width=140,
                height=50,
                bgcolor=colors.RED_700,
                border_radius=8,
                padding=padding.only(left=30, right=5),
                on_hover=lambda e: self.DeleteAnimation(e),
                content=Row(
                    alignment="spaceBetween",
                    spacing=0,
                    controls=[
                        self.text,
                        self.IconContainer,
                    ],
                ),
            ),
        )
        return self.MainContainer

    def DeleteAnimation(self, e):
        if e.data == "true":
            self.text.offset = transform.Offset(-1, 0)
            self.text.opacity = 0
            self.text.update()

            self.icon.offset = transform.Offset(-1.1, 0)
            self.icon.update()

        else:
            self.text.offset = transform.Offset(0, 0)
            self.text.opacity = 100
            self.text.update()

            self.icon.offset = transform.Offset(0, 0)
            self.icon.update()
