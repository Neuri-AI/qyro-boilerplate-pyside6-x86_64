import sys
from ppg_runtime.application_context.${python_bindings} import ApplicationContext
from ppg_runtime.application_context import PPGLifeCycle, init_lifecycle
from ppg_runtime.application_context.devtools.reloader import hot_reloading
from ppg_runtime.application_context.utils import app_is_frozen
from ${python_bindings}.QtWidgets import QMainWindow, QLabel

@init_lifecycle
@hot_reloading
class ${app_name}(QMainWindow, PPGLifeCycle):

    def render_(self):
       QLabel('Hello World!', parent=self)

    def responsive_UI(self):
        self.setMinimumSize(640, 480)


if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = ${app_name}()
    if not app_is_frozen():
        window._init_hot_reload_system(__file__)
    window.show()
    exec_func = getattr(appctxt.app, 'exec', appctxt.app.exec_)
    sys.exit(exec_func())