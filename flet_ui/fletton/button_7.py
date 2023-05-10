from flet import (
    UserControl,
    Container,
    animation,
    alignment,
    Text,
    transform,
    Stack,
    padding,
)


class Button(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):
        self.AnimatedContainer = Container(
            width=5,
            height=45,
            bgcolor="black",
            animate=animation.Animation(600, "ease"),
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(duration=1000, curve="ease"),
            alignment=alignment.center_left,
        )

        self.text = Text(
            "HOVER ME!",
            size=12,
            weight="w800",
            right=60,
            top=15,
            color="black",
            animate_opacity=600,
        )

        self.inner = Container(
            width=180,
            height=45,
            on_hover=lambda e: self.SideAnimation(e),
            padding=padding.only(left=20),
            content=(
                Stack(
                    controls=[
                        self.AnimatedContainer,
                        self.text,
                    ]
                )
            ),
        )

        self.MainContainer = Container(
            width=300,
            height=300,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=self.inner,
        )

        return self.MainContainer

    def SideAnimation(self, e):
        if e.data == "true":
            self.AnimatedContainer.width = 130
            self.AnimatedContainer.update()

            self.text.color, self.text.opacity = "white", 100
            self.text.update()
        else:
            self.AnimatedContainer.width = 5
            self.AnimatedContainer.update()

            self.text.color, self.text.opacity = "black", 100
            self.text.update()
