""" Button Page Class """
from flet import UserControl, ResponsiveRow, Container
import importlib, os, importlib.util


# MODULE IMPORTS: necessary to iterate with the following logic for scaling purposes
_moduleList = []
# LOOP ONE: iterate over the tuple of the root folder
for root, dirs, __ in os.walk(r"./"):
    # LOOP TWO: iterate over the second element of the tuple => fodlers
    for dir in dirs:
        # IF ONE: if the directory matches the folder name, continue
        if dir == "fletton":
            # LOOP THREE: iterate over the filenames under sorted method
            for filename in sorted(os.listdir(dir)):
                # crate the path for each file name
                _file = os.path.join(dir, filename)
                # IF TWO: check to see if the file is a file and not a folder
                if os.path.isfile(_file):
                    # strip the extension from the filename
                    filename = filename.strip(".py")
                    # finally append the modules to a list so we can call them when we create the UI
                    _moduleList.append(
                        importlib.util.spec_from_file_location(filename, _file)
                    )


class AnimatedButtons(UserControl):
    def __init__(self, visibility):
        self.visibility = visibility
        super().__init__()

    def build(self):
        self._animation_row = ResponsiveRow(
            run_spacing=10,
            alignment="center",
        )
        for _module in _moduleList:
            _gradient = Container(
                bgcolor="white",
                padding=30,
                border_radius=12,
                aspect_ratio=1,
                col={"xs": 12, "sm": 6, "md": 6, "lg": 4, "xl": 3},
                content=_module.loader.load_module().Button(),
            )

            self._animation_row.controls.append(_gradient)

        return self._animation_row
