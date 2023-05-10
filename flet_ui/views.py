from flet import border
from data import *


def CopyContent(e):
    e.page.set_clipboard(e.control.data)


def NavSelection(e):
    global RouteDictionary
    for key in RouteDictionary:
        if e.control.text == key:
            RouteDictionary[key].controls[0].visible = True
            RouteDictionary[key].controls[0].update()
        if e.control.text != key:
            RouteDictionary[key].controls[0].visible = False
            RouteDictionary[key].controls[0].update()


def _hover_animation(e):
    if e.data == "true":
        if e.control.content.data == True:
            pass
        else:
            e.control.border = border.only(left=border.BorderSide(1, "#f8fafc"))
            e.control.update()
            e.control.content.color = "#f8fafc"
            e.control.content.update()
    else:
        if e.control.content.data == True:
            pass
        else:
            e.control.border = border.only(left=border.BorderSide(1, "#64748b"))
            e.control.update()
            e.control.content.color = "#64748b"
            e.control.content.update()

    return _hover_animation
