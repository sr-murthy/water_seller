"""
This file defines the PackageKtools class which is responsible for packaging the ktools.
"""
import os
from distutils import util

from gerund.commands.terminal_command import TerminalCommand


class PackageKtools:
    """
    The PackageKtools class is used to package the ktools.

    Attributes:
        ktools_path: the path to the ktools directory
        platform: the platform the ktools are being compiled for
    """
    def __init__(self, ktools_path: str) -> None:
        self.ktools_path: str = ktools_path
        self.platform: str = util.get_platform().replace("-", "_").replace(".", "_")

    def package(self) -> None:
        """
        Packages the ktools into tar file.

        :return: None
        """
        TerminalCommand(f"cd {self.bin_path} && tar -zcvf ../../{self.platform}.tar.gz ./").wait()

    @property
    def bin_path(self) -> str:
        return str(os.path.join(self.ktools_path, "build", "bin"))
