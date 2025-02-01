
# Water Seller

This is a tool for handling local processes in order to run OasisLMF products. 

## Installation
To install the package with pip use the following command:

```bash
pip install git+https://github.com/OasisLMF/water_seller.git     
```

## Usage

Water seller currently supports the following processes:

* Local installation of the MDK (`oasislmf` Python package)


### Local MDK Installation

This process installs the `oasislmf` package, and will install all of the required dependencies. Note that as part of the installation [ktools](https://github.com/OasisLMF/ktools), which is a C++ component separate from the Python component, is cloned and built from sources. Unlike `pip install oasislmf` (which calls [`python setup.py install`](https://github.com/OasisLMF/OasisLMF/blob/main/setup.py#L147), the `water_seller` tool allows the ktools build configuration and compilation to be customised at runtime.

The base command is `ws-install-oasislmf` with optional arguments for build configuration and compilation provided after the `--extra` flag, as described below.
```bash
usage: ws-install-oasislmf [-h] [--extra] [--ktools-enable-osx] [--ktools-enable-o3] [-m MDK_BRANCH] [-k KTOOLS_BRANCH]
                           [--ktools-disable-parquet]

Example script using argparse

options:
  -h, --help            show this help message and exit
  --extra               If extra OasisLMF requirements are installed Use this flag to set the value to True
  --ktools-enable-osx   Enable OS X / Mac specific configuration / compilation options when building ktools
  --ktools-enable-o3    Enable level 3 compiler optimisations when building ktools
  -m MDK_BRANCH, --mdk-branch MDK_BRANCH
                        (Optional) specific MDK Git branch or tag to install
  -k KTOOLS_BRANCH, --ktools-branch KTOOLS_BRANCH
                        (Optional) specific ktools Git branch or tag to install
  --ktools-disable-parquet
                        Disable Parquet option when configuring ktools
```

The basic usage is:
```bash
ws-install-oasislmf --extra
```
which will install the [`oasislmf`](https://github.com/OasisLMF/OasisLMF) package directly from the ```master``` 
branch of the [OasisLMF](https://github.com/OasisLMF/OasisLMF) github repository.

To install a specific branch or release or tag use the same command as above with additional options as follows:
```bash
ws-install-oasislmf --extra --mdk-branch <MDK branch or release or tag name> --ktools-branch <ktools branch or release or tag name> [--ktools-disable-parquet]
```
For example to install MDK release [`2.3.5`](https://github.com/OasisLMF/OasisLMF/releases/tag/2.3.5), which is linked to ktools release [`v3.12.3`](https://github.com/OasisLMF/ktools/releases/tag/v3.12.3) use:
```bash
ws-install-oasislmf --extra --mdk-branch 2.3.5 --ktools-branch v3.12.3 [--ktools-disable-parquet]
```

To customise the ktools build configuration and/or compilation use the following flags (after `--extra`):

* `--ktools-enable-osx` - for Mac-specific customisations
* `--ktools-enable-o3` - for [level 3 C++ compiler optimisations](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#index-O3)
* `--ktools-disable-parquet` - for disabling the Parquet flag when configuring ktools
