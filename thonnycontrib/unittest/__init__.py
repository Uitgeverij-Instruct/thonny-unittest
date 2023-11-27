import os
import subprocess

import thonny.plugins.cells
from thonny import get_workbench

from thonny.codeview import SyntaxText, get_syntax_options_for_tag
from thonny.languages import tr
from thonny.tktextext import TextFrame

from thonny.ui_utils import select_sequence


def cmd_run_unit_tests_enabled():
    return get_workbench().get_editor_notebook().get_current_editor() is not None


def cmd_run_unit_tests():
    dir = get_workbench().get_view("FilesView").get_active_local_dir()
    get_workbench().show_view("TestsView")
    p = thonny.running.create_frontend_python_process(["-u", "-m", "unittest", "discover", "-s", dir],
        stdout=subprocess.PIPE, )
    out, err = p.communicate()
    get_workbench().get_view("TestsView").set_test_results(out)


class TestsView(TextFrame):
    def __init__(self, master):
        super().__init__(master, borderwidth=0, relief="solid", undo=False, read_only=True, text_class=SyntaxText)
        self._show_description()

    def _show_description(self):
        self.text.configure(foreground=get_syntax_options_for_tag("TEXT")["foreground"])
        self.text.direct_insert("end", tr("Test results are displayed here."))

    def set_test_results(self, results):
        self.text.direct_delete("1.0", "end")
        self.text.configure(foreground=get_syntax_options_for_tag("TEXT")["foreground"])
        self.text.direct_insert("end", results)


def load_plugin():
    get_workbench().add_command(command_id="run_unit_tests", menu_name="run", command_label=tr("Run unit tests"),
        caption=tr("Run unit tests"), handler=cmd_run_unit_tests, default_sequence="<F6>",
        extra_sequences=[select_sequence("<Control-Shift-t>", "<Command-Shift-t>")], tester=cmd_run_unit_tests_enabled,
        group=10, image=os.path.join(os.path.dirname(__file__), "res", "tick.png"),
        include_in_toolbar=not (get_workbench().in_simple_mode()), show_extra_sequences=True, )

    get_workbench().add_view(TestsView, "Tests", "s")
