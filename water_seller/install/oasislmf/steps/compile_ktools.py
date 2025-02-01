"""
This file defines the CompileKtools class which is responsible for compiling the ktools.
"""
import os

from gerund.commands.terminal_command import TerminalCommand


class CompileKtools:
    """
    The CompileKtools class is used to compile the ktools.

    Attributes:
        ktools_path: the path to the ktools directory
    """
    def __init__(
        self,
        ktools_path: str,
        enable_osx: bool = False,
        enable_o3: bool = True,
        disable_parquet: bool = False) -> None:
        """
        The constructor for the CompileKtools class.

        :param ktools_path: the path to the ktools directory
        """
        self.ktools_path: str = ktools_path
        self.enable_osx = enable_osx
        self.enable_o3 = enable_o3
        self.disable_parquet = disable_parquet

    def compile(self) -> None:
        """
        Compiles the ktools.

        :return: None
        """
        TerminalCommand(f"cd {self.ktools_path} && ./autogen.sh").wait()
        TerminalCommand(
            f"cd {self.ktools_path} "
            "&& ./configure "
            f"{'--enable-osx' if self.enable_osx else ''} "
            f"{'--enable-o3' if self.enable_o3 else ''}  "
            f"{'--disable-parquet' if self.disable_parquet else ''} "
            f"--prefix={self.bin_path}"
        ).wait()
        TerminalCommand(f"cd {self.ktools_path} && make check").wait()
        TerminalCommand(f"cd {self.ktools_path} && make install").wait()

    @property
    def bin_path(self) -> str:
        return str(os.path.join(self.ktools_path, "build"))
