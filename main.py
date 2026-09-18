import sys
from ${python_bindings}.QtWidgets import QMainWindow, QLabel
from qyro_engine import ApplicationContext
from qyro_engine.ui.component import Component


class ${app_name}(QMainWindow, Component, ApplicationContext):

    def component_will_mount(self):
        self.setMinimumSize(640, 480)

    def render(self):

        label = QLabel(
            f"Hello, World!\n\n\n"
            f"App Title: {self.window_title}\n\n"
            f"Active Icon: {self.app_icon}\n\n"
            f"Platform: {self.platform.value} (Frozen: {self.is_frozen})\n",
            parent=self
        )
        label.move(50, 50)
        label.resize(label.sizeHint())



if __name__ == "__main__":
    window = ${app_name}()
    window.show()
    sys.exit(window.exec())
