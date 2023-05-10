""" Landing Page Class """
from flet import UserControl, ResponsiveRow, Container, alignment, Text, padding, Column


class Landing(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self._title = ResponsiveRow(
            alignment="center",
            controls=[
                Container(
                    alignment=alignment.top_center,
                    col={"xs": 12, "sm": 12, "md": 10, "lg": 10, "xl": 12},
                    padding=30,
                    content=Text(
                        "Open Source UI Designs Programmed In Flet",
                        size=44,
                        weight="w700",
                        text_align="center",
                    ),
                )
            ],
        )

        self._sub_title = ResponsiveRow(
            alignment="center",
            controls=[
                Container(
                    col={"xs": 10, "sm": 10, "md": 10, "lg": 8, "xl": 6},
                    alignment=alignment.center,
                    padding=padding.only(bottom=30),
                    content=Text(
                        "A collection of Flet's color palette, animations, and linear gradients that you can use as content in any part of your website. Simply click a single color item or gradient and paste the Python code inside your application or project!.",
                        size=16,
                        weight="w300",
                        text_align="center",
                        color="#64748b",
                    ),
                )
            ],
        )

        return Column(controls=[self._title, self._sub_title])
