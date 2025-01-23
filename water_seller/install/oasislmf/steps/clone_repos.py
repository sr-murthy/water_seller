"""
This file defines the CloneRepos class which is responsible for cloning a git repo.
"""
import os

from gerund.commands.terminal_command import TerminalCommand


class CloneRepos:
    """
    The CloneRepos class is used to clone a git repo.

    Attributes:
        git_url: the url of the git repo to clone
        package_name: the name of the package to clone
    """
    def __init__(self, root_path: str, git_url: str, package_name: str, branch: str = None) -> None:
        """
        The constructor for the CloneRepos class.

        :param root_path: the path to the root directory where the repo will be cloned
        :param git_url: the url of the git repo to clone
        :param package_name: the name of the package to clone
        """
        self._root_path = root_path
        self.git_url = git_url
        self.package_name = package_name
        self.branch = branch

    def clone_repo(self) -> None:
        """
        Clones the git repo.

        :return: None
        """
        clone_options = "" if not self.branch else f"--depth 1 --branch {self.branch}"
        TerminalCommand(f"echo 'Cloning {self.git_url}@{self.branch if self.branch else '''latest'''}'").wait()
        TerminalCommand(f"cd {self.root_path} && git clone {clone_options} {self.git_url}").wait()

    @property
    def root_path(self) -> str:
        return str(os.path.join(os.getcwd(), self._root_path, "stash"))

    @property
    def package_path(self) -> str:
        return str(os.path.join(self.root_path, self.package_name))
