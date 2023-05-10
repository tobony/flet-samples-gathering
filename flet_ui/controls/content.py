""" Main Content Class """
from flet import (
    Container,
    UserControl,
    Row,
    padding,
    Column,
    alignment,
    border,
    Text,
)
from controls.colorPage import Color
from controls.gradientPage import GradientPage
from controls.buttonPage import AnimatedButtons
from views import _hover_animation
from data import *


class MainContent(UserControl):
    def __init__(self):
        super().__init__()

    def PageRouting(self, e):
        for row in self._side_navigation_column.controls[:]:
            if row.data != "title":
                (
                    row.controls[0].border,
                    row.controls[0].content.color,
                    row.controls[0].content.data,
                ) = (
                    border.only(left=border.BorderSide(1, "#64748b")),
                    "#64748b",
                    False,
                )

                row.controls[0].update()
                row.controls[0].content.update()

            if e.control.content.data != True:
                e.control.content.color, e.control.content.data = "white", True
                e.control.content.update()
                e.control.border = border.only(left=border.BorderSide(1, "white"))
                e.control.update()

        global RouteDictionary
        for key in RouteDictionary:
            if e.control.content.value == key:
                RouteDictionary[key].controls[0].visible = True
                RouteDictionary[key].controls[0].update()
            if e.control.content.value != key:
                RouteDictionary[key].controls[0].visible = False
                RouteDictionary[key].controls[0].update()

    def SideNavigation(self):
        side_nav_list = SideNavigationDictionary()

        self._side_navigation_column = Column(spacing=1)

        for _title in side_nav_list:
            _row = Row(
                data="title",
                controls=[
                    Container(
                        padding=padding.only(bottom=10),
                        content=Text(f"{_title}"),
                    )
                ],
            )
            self._side_navigation_column.controls.append(_row)

            for _sub_title in side_nav_list[_title].values():
                _row = Row(
                    data="subtitle",
                    controls=[
                        Container(
                            height=30,
                            alignment=alignment.center,
                            padding=padding.only(left=20),
                            on_click=lambda e: self.PageRouting(e),
                            on_hover=lambda e: _hover_animation(e),
                            border=border.only(left=border.BorderSide(1, "white")),
                            content=Text(
                                f"{_sub_title}",
                                color="white",
                                data=True,
                            ),
                        )
                    ],
                )

                self._side_navigation_column.controls.append(_row)

        for _ in self._side_navigation_column.controls[2:]:
            _.controls[0].content.color = "#64748b"
            _.controls[0].content.data = False
            _.controls[0].border = border.only(left=border.BorderSide(1, "#64748b"))

        return self._side_navigation_column

    def build(self):
        # COLOR LIST: renders the colors available in Flet library
        Colors = Color(True)

        # GRADIENT LIST: renders randomly generated linear gradeints
        Gradients = GradientPage(False)

        # ANIMATED BUTTONS: renders animated buttons from the fletton directory
        Animations = AnimatedButtons(False)

        # MAIN CONTENT: contains all the page routes, the side navigation, and some padding to the right side
        self._main_content_area = Row(
            alignment="center",
            vertical_alignment="start",
            controls=[
                Container(padding=padding.only(left=20)),
                Container(
                    height=500,
                    expand=1,
                    content=Column(
                        scroll="auto",
                        horizontal_alignment="center",
                        controls=[
                            Container(
                                content=self.SideNavigation(),
                            ),
                        ],
                    ),
                ),
                Container(
                    expand=6,
                    content=Column(
                        controls=[
                            Colors,
                            Gradients,
                            Animations,
                        ],
                    ),
                ),
                Container(expand=1),
                Container(padding=padding.only(left=20)),
            ],
        )

        global RouteDictionary
        RouteDictionary["Colors"] = Colors
        RouteDictionary["Animations"] = Animations
        RouteDictionary["Gradients"] = Gradients

        return self._main_content_area
