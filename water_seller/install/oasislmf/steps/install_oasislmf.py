"""
This file defines the InstallOasisLmf class is used to install the oasislmf package.
"""
from distutils import util
from pathlib import Path

from gerund.commands.terminal_command import TerminalCommand


class InstallOasisLmf:
    """
    The InstallOasisLmf class is used to install the oasislmf package.

    Attributes:
        root_path: the path to the root directory of the cloned oasislmf repo
        ktools_path: the path to the root directory of the cloned ktools repo
        platform: the platform the ktools are being compiled for
        extra: whether to install the extra packages
    """
    def __init__(self, root_path: str, ktools_path: str, extra: bool = True) -> None:
        """
        The constructor for the InstallOasisLmf class.

        :param root_path: the path to the root directory of the cloned oasislmf repo
        :param ktools_path: the path to the root directory of the cloned ktools repo
        :param extra: whether to install the extra packages
        """
        self.root_path = Path(root_path).resolve()
        self.ktools_path = Path(ktools_path).resolve()
        self.platform: str = util.get_platform().replace("-", "_").replace(".", "_")
        self.extra: bool = extra

    def install(self) -> None:
        """
        Installs the oasislmf package.

        :return: None
        """
        TerminalCommand("pip install pip-tools").wait()

        env_vars = {
            "KTOOLS_TAR_FILE_DIR": str(self.ktools_path)
        }
        TerminalCommand(
            f"cd {str(self.root_path)} && python setup.py install bdist_wheel --plat-name {self.platform}",
            environment_variables=env_vars
        ).wait()
        TerminalCommand(
            f"cd {str(self.root_path)} && pip install -r requirements-package.in"
        ).wait()
        if self.extra is True:
            TerminalCommand(
                f"cd {str(self.root_path)} && pip install -r optional-package.in"
            ).wait()
