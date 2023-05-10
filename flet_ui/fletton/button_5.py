from flet import UserControl, Container, animation, alignment, Text, transform, border


class Button(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):

        self.outer = Container(
            width=120,
            height=50,
            border_radius=8,
            bgcolor="white",
            border=border.all(1.5, "black"),
            offset=transform.Offset(0, -0.1),  # position
            animate_offset=animation.Animation(duration=700, curve="ease"),
            alignment=alignment.center,
            content=Text("BUTTON", size=15, color="black", weight="w900"),
        )

        self.button = Container(
            width=300,
            height=300,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=Container(
                width=120,
                height=50,
                bgcolor="black",
                border_radius=10,
                # padding=padding.only(bottom=5),
                on_hover=lambda e: self.StretchButton(e),
                content=self.outer,
            ),
        )

        return self.button

    def StretchButton(self, e):
        if e.data == "true":
            self.outer.offset = transform.Offset(0, -0.16)
            self.outer.update()
        else:
            self.outer.offset = transform.Offset(0, -0.1)
            self.outer.update()
