from flet import (
    UserControl,
    Container,
    animation,
    alignment,
    IconButton,
    Text,
    icons,
    Stack,
)


class Button(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):
        self.MovingContainer = Container(
            border_radius=100,
            width=45,
            height=45,
            bgcolor="black",
            animate=animation.Animation(600, "ease"),
            alignment=alignment.center_left,
            content=IconButton(
                icon=icons.KEYBOARD_ARROW_RIGHT_ROUNDED,
                icon_size=16,
                icon_color="white",
            ),
        )
        self.text = Text(
            "LEARN MORE",
            size=12,
            weight="w800",
            right=40,
            top=15,
            color="black",
        )

        self.MainContainer = Container(
            width=300,
            height=300,
            # aspect_ratio=1,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=Container(
                width=180,
                height=45,
                on_hover=lambda e: self.SlideAnimation(e),
                content=(
                    Stack(
                        controls=[
                            self.MovingContainer,
                            self.text,
                        ]
                    )
                ),
            ),
        )
        return self.MainContainer

    def SlideAnimation(self, e):
        if e.data == "true":
            self.MovingContainer.width = 180
            self.MovingContainer.update()

            self.text.color = "white"
            self.text.update()

        else:
            self.MovingContainer.width = 45
            self.MovingContainer.update()
            self.text.color = "black"
            self.text.update()
