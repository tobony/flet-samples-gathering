import flet
from flet import Page, ElevatedButton, AlertDialog, Text, TextButton


def main(page: Page):
    page.title = "Pop-up Dialog Test"
    page.window_width = 400
    page.window_height = 700

    def close_dialog(e):
        dialog.open = False
        page.update()

    dialog = AlertDialog(
        modal=True,
        title=Text("Hello, world or NOT"),
        content=Text("바꿀겁니까?"),
        actions=[
            TextButton("AAA", on_click=close_dialog),
            TextButton("BBB", on_click=close_dialog)
        ],
        on_dismiss=lambda e: print("딩동댕동")
    )

    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    b1 = ElevatedButton(text="변경", on_click=open_dialog)

    page.controls.append(b1)

    page.update()


# flet.app(target=main)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)
