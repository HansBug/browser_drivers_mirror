# browser_drivers_mirror

[![Last Updated](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/HansBug/4ff4fe9d279fa2bc2cef37fec8cde822/raw/data_last_update.json)](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/)

Mirror of browser's drivers. The resource will be refreshed daily
on [HansBug/browser_drivers_mirror on huggingface](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/).

## Supported Browsers

* [Google Chrome](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/google) (up to [114.0.5735.90](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/google/114.0.5735.90))
    * [Linux Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/114.0.5735.90/chromedriver_linux64.zip)
    * [macOS Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/114.0.5735.90/chromedriver_mac64.zip)
    * [Windows Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/114.0.5735.90/chromedriver_win32.zip)
* [Microsoft Edge](${EDGE_DIR) (up to [113.0.1774.57](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/edge/113.0.1774.57))
    * [Linux Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/114.0.1823.43/edgedriver_linux64.zip)
    * [macOS Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/113.0.1774.57/edgedriver_mac64.zip)
    * [Windows (64bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/113.0.1774.57/edgedriver_win64.zip)
    * [Windows (32bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/113.0.1774.57/edgedriver_win32.zip)
* [Mozilla Firefox](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/firefox) (up to [v0.33.0](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/firefox/v0.33.0))
    * [Linux Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz)
    * [macOS Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos.tar.gz)
    * [macOS (arch) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos-aarch64.tar.gz)
    * [Windows (64bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win64.zip)
    * [Windows (32bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win32.zip)
* [Opera](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/opera) (up to [v.112.0.5615.87](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/opera/v.112.0.5615.87))
    * [Linux Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_linux64.zip)
    * [macOS Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_mac64.zip)
    * [Windows (64bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_win64.zip)
    * [Windows (32bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_win32.zip)
* [IE (not recommended)](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/ie) (up to [selenium-4.10.0](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/tree/main/ie/selenium-4.10.0))
    * [Windows (64bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.10.0/IEDriverServer_x64_4.10.0.zip)
    * [Windows (32bit) Driver](https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.10.0/IEDriverServer_Win32_4.10.0.zip)

## How to use

### With command line

* Chrome

```bash
# get latest version
wget -qO- 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/LATEST_RELEASE'

# download for linux
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/114.0.5735.90/chromedriver_linux64.zip'
# download for macos
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/114.0.5735.90/chromedriver_mac64.zip'
# download for windows
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/google/114.0.5735.90/chromedriver_win32.zip'

```

* Firefox

```bash
# get latest version
wget -qO- 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/LATEST_RELEASE'

# download for linux
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz'
# download for macos
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos.tar.gz'
# download for macos (arch)
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos-aarch64.tar.gz'
# download for win64
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win64.zip'
# download for win32
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win32.zip'

```

* Opera

```bash
# get latest version
wget -qO- 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/LATEST_RELEASE'

# download for linux
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_linux64.zip'
# download for macos
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_mac64.zip'
# download for win64
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_win64.zip'
# download for win32
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/opera/v.112.0.5615.87/operadriver_win32.zip'

```

* Edge

```bash
# get latest version
wget -qO- 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/LATEST_STABLE'

# download for linux
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/114.0.1823.43/edgedriver_linux64.zip'
# download for macos
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/113.0.1774.57/edgedriver_mac64.zip'
# download for win64
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/113.0.1774.57/edgedriver_win64.zip'
# download for win32
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/edge/113.0.1774.57/edgedriver_win32.zip'

```

* IE

```bash
# get latest version
wget -qO- 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/ie/LATEST_RELEASE'

# download for win64
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.10.0/IEDriverServer_x64_4.10.0.zip'
# download for win32
wget 'https://huggingface.co/datasets/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.10.0/IEDriverServer_Win32_4.10.0.zip'

```

### With [hf-webdriver-manager](https://github.com/HansBug/hf_webdriver_manager)

We recommend you to use [hf-webdriver-manager](https://github.com/HansBug/hf_webdriver_manager) instead of native
command line. This is written in Python, can be installed with the following command:

```bash
pip install hf-webdriver-manager
```

Then use this in Python

```python
from webdriver_manager.dispatch import get_browser_manager

# chrome, ie, edge, firefox, opera are supported
chrome = get_browser_manager('chrome')
print(chrome.browser_version)  # version of browser, None when not installed
print(chrome.latest_version)  # latest version
print(chrome.version_to_download)  # version to download
print(chrome.driver_url)  # online resource

# download and return the executable driver on your disk
# this can be directly used in selenium
print(chrome.driver_executable)
```

