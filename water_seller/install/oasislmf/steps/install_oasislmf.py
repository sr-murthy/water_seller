import os

from gerund.commands.terminal_command import TerminalCommand
from distutils import util


class InstallOasisLmf:

    def __init__(self, root_path: str, ktools_path: str) -> None:
        self.root_path: str = root_path
        self.ktools_path: str = ktools_path
        self.platform: str = util.get_platform().replace("-", "_").replace(".", "_")

    def install(self) -> None:
        TerminalCommand("pip install pip-tools").wait()

        env_vars = {
            "KTOOLS_TAR_FILE_DIR": self.ktools_path
        }
        TerminalCommand(
            f"cd {self.root_path} && python setup.py install bdist_wheel --plat-name {self.platform}",
            environment_variables=env_vars
        ).wait()
