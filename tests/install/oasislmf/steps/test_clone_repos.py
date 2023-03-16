from unittest import main, TestCase
from unittest.mock import patch, PropertyMock

from water_seller.install.oasislmf.steps.clone_repos import CloneRepos


class TestCloneRepos(TestCase):

    def setUp(self) -> None:
        self.path = "some/path/"
        self.git_url = "https://github.com/OasisLMF/OasisLMF.git"
        self.package_name = "oasislmf"
        self.test = CloneRepos(root_path=self.path, git_url=self.git_url, package_name=self.package_name)

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        self.assertEqual(self.test._root_path, self.path)
        self.assertEqual(self.test.git_url, self.git_url)
        self.assertEqual(self.test.package_name, self.package_name)

    @patch("water_seller.install.oasislmf.steps.clone_repos.TerminalCommand")
    @patch("water_seller.install.oasislmf.steps.clone_repos.CloneRepos.root_path", new_callable=PropertyMock)
    def test_clone_repo(self, mock_root_path, mock_terminal) -> None:
        mock_root_path.return_value = "some/path/"
        self.test.clone_repo()
        mock_terminal.assert_called_once_with(f"cd some/path/ && git clone {self.git_url}")
        mock_terminal.return_value.wait.assert_called_once_with()

    @patch("water_seller.install.oasislmf.steps.clone_repos.os.getcwd")
    def test_root_path(self, mock_getcwd) -> None:
        mock_getcwd.return_value = "some/path/"
        self.assertEqual(self.test.root_path, "some/path/some/path/stash")

    @patch("water_seller.install.oasislmf.steps.clone_repos.os.getcwd")
    def test_package_path(self, mock_getcwd) -> None:
        mock_getcwd.return_value = "some/path/"
        self.assertEqual(self.test.package_path, "some/path/some/path/stash/oasislmf")


if __name__ == '__main__':
    main()
