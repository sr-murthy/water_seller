from unittest import main, TestCase
from unittest.mock import patch, PropertyMock

from water_seller.install.oasislmf.steps.compile_ktools import CompileKtools


class TestCompileKtools(TestCase):

    def setUp(self) -> None:
        self.path = "some/path/"
        self.test = CompileKtools(ktools_path=self.path)

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        pass


if __name__ == '__main__':
    main()
