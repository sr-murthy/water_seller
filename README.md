
# Water Seller

This is a tool for handling local processes in order to run OasisLMF products. 

## Installation
To install the package with pip use the following command:

```bash
pip install git+https://github.com/OasisLMF/water_seller.git     
```

## Usage
Water seller currently supports the following processes:

### Local OasisLMF Installation
This process installs the OasisLMF package, including ktools, locally and installs the required dependencies. Note that ktools is a C++ component and is built from sources - the build options for `configure` and `make` can be customised with this tool with the following extra command line options (after the `--extra` option):


```bash
ws-install-oasislmf --extra
```
This will install the [OasisLMF](https://github.com/OasisLMF/OasisLMF) package directly from the ```master``` 
branch of the [OasisLMF](https://github.com/OasisLMF/OasisLMF) github repository.

To install a specific branch or release or tag use the same command as above with additional options as follows:
```bash
ws-install-oasislmf --extra --mdk-branch <MDK branch or release or tag name> --ktools-branch <ktools branch or release or tag name> [--ktools-disable-parquet]
```
For example to install MDK release [`2.3.5`](https://github.com/OasisLMF/OasisLMF/releases/tag/2.3.5), which is linked to ktools release [`v3.12.3`](https://github.com/OasisLMF/ktools/releases/tag/v3.12.3) use:
```bash
ws-install-oasislmf --extra --mdk-branch 2.3.5 --ktools-branch v3.12.3 [--ktools-disable-parquet]
```
The optional boolean `--ktools-disable-parquet` disables the Parquet flag when configuring ktools, e.g.:
```bash
[/build/path/to/ktools] $ ./configure ... --disable-parquet
```
