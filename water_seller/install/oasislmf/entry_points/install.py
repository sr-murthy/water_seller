"""
This file defines the entry point for building ktools locally and installing OasisLMF.
"""
import os
import shutil

from water_seller.install.oasislmf.steps.clone_repos import CloneRepos
from water_seller.install.oasislmf.steps.compile_ktools import CompileKtools
from water_seller.install.oasislmf.steps.install_oasislmf import InstallOasisLmf
from water_seller.install.oasislmf.steps.package_ktools import PackageKtools


def main() -> None:
    """
    The main function for building ktools and installing oasislmf.
    """
    root_path: str = str(os.getcwd())
    stash_path: str = str(os.path.join(root_path, "stash"))

    if os.path.exists(stash_path):
        shutil.rmtree(stash_path)
    os.mkdir(stash_path)

    clone_ktools: CloneRepos = CloneRepos(
        root_path=root_path,
        git_url="https://github.com/OasisLMF/ktools.git",
        package_name="ktools"
    )
    clone_ktools.clone_repo()

    compile_ktools: CompileKtools = CompileKtools(ktools_path=clone_ktools.package_path)
    compile_ktools.compile()

    package_ktools: PackageKtools = PackageKtools(ktools_path=clone_ktools.package_path)
    package_ktools.package()

    clone_oasislmf: CloneRepos = CloneRepos(
        root_path=root_path,
        git_url="https://github.com/OasisLMF/OasisLMF.git",
        package_name="oasislmf"
    )
    clone_oasislmf.clone_repo()

    install_oasislmf: InstallOasisLmf = InstallOasisLmf(root_path=clone_oasislmf.package_path,
                                                        ktools_path=clone_ktools.package_path)
    install_oasislmf.install()
