from flet import (
    UserControl,
    Container,
    animation,
    alignment,
    Text,
    transform,
    Stack,
    colors,
)


class Button(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):

        self.StackContainer = Stack()

        self.RedList = ["red100", "red200", "red300", "red400", "red"]

        for i in self.RedList:
            x = Container(
                width=130,
                height=55,
                bgcolor=i,
                border_radius=12,
                offset=transform.Offset(0, 0),
                animate_offset=animation.Animation(duration=700, curve="ease"),
            )
            if i == "red":
                x.content, x.alignment = (
                    Text("BUTTON!", color="white", weight="w700"),
                    alignment.center,
                )

            self.StackContainer.controls.append(x)

        self.MainContainer = Container(
            width=300,
            height=300,
            alignment=alignment.center,
            bgcolor="white",
            border_radius=10,
            content=Container(
                width=130,
                height=55,
                bgcolor=colors.RED_50,
                border_radius=15,
                content=self.StackContainer,
                on_hover=lambda e: self.ColorShadeAnimation(e),
            ),
        )

        return self.MainContainer

    def ColorShadeAnimation(self, e):
        if e.data == "true":
            x, y = -0.05, -0.05
            for shade in self.StackContainer.controls[:]:
                shade.offset = transform.Offset(x, y)
                shade.update()
                x -= 0.05
                y -= 0.08

        else:
            for shade in self.StackContainer.controls[:]:
                shade.offset = transform.Offset(0, 0)
                shade.update()
