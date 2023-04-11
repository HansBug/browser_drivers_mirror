# browser_drivers_mirror

[![Last Updated](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/HansBug/4ff4fe9d279fa2bc2cef37fec8cde822/raw/data_last_update.json)](https://huggingface.co/HansBug/browser_drivers_mirror)

Mirror of browser's drivers. The resource will be refreshed daily
on [HansBug/browser_drivers_mirror on huggingface](https://huggingface.co/HansBug/browser_drivers_mirror).

## Supported Browsers

* [Google Chrome](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/google) (up
  to [112.0.5615.49](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/google/112.0.5615.49))
    * [Linux Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/111.0.5563.64/chromedriver_linux64.zip)
    * [macOS Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/112.0.5615.49/chromedriver_mac64.zip)
    * [Windows Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/112.0.5615.49/chromedriver_win32.zip)
* [Microsoft Edge](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/edge) (up
  to [112.0.1722.34](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/edge/112.0.1722.34))
    * [Linux Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/111.0.1661.62/edgedriver_linux64.zip)
    * [macOS Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/112.0.1722.39/edgedriver_mac64.zip)
    * [Windows (64bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/112.0.1722.39/edgedriver_win64.zip)
    * [Windows (32bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/112.0.1722.39/edgedriver_win32.zip)
* [Mozilla Firefox](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/firefox) (up
  to [v0.33.0](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/firefox/v0.33.0))
    * [Linux Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz)
    * [macOS Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos.tar.gz)
    * [macOS (arch) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos-aarch64.tar.gz)
    * [Windows (64bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win64.zip)
    * [Windows (32bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win32.zip)
* [Opera](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/opera) (up
  to [v.111.0.5563.65](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/opera/v.111.0.5563.65))
    * [Linux Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_linux64.zip)
    * [macOS Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_mac64.zip)
    * [Windows (64bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_win64.zip)
    * [Windows (32bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_win32.zip)
* [IE (not recommended)](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/ie) (up
  to [selenium-4.8.0](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/ie/selenium-4.8.0))
    * [Windows (64bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.8.0/IEDriverServer_x64_4.8.0.zip)
    * [Windows (32bit) Driver](https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.8.0/IEDriverServer_Win32_4.8.0.zip)

## How to use

### With command line

* Chrome

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/LATEST_RELEASE'

# download for linux
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/111.0.5563.64/chromedriver_linux64.zip'
# download for macos
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/112.0.5615.49/chromedriver_mac64.zip'
# download for windows
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/112.0.5615.49/chromedriver_win32.zip'
```

* Firefox

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/LATEST_RELEASE'

# download for linux
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz'
# download for macos
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos.tar.gz'
# download for macos (arch)
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-macos-aarch64.tar.gz'
# download for win64
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win64.zip'
# download for win32
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/v0.33.0/geckodriver-v0.33.0-win32.zip'
```

* Opera

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/LATEST_RELEASE'

# download for linux
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_linux64.zip'
# download for macos
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_mac64.zip'
# download for win64
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_win64.zip'
# download for win32
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/v.111.0.5563.65/operadriver_win32.zip'
```

* Edge

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/LATEST_STABLE'

# download for linux
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/111.0.1661.62/edgedriver_linux64.zip'
# download for macos
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/112.0.1722.39/edgedriver_mac64.zip'
# download for win64
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/112.0.1722.39/edgedriver_win64.zip'
# download for win32
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/112.0.1722.39/edgedriver_win32.zip'
```

* IE

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/ie/LATEST_RELEASE'

# download for win64
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.8.0/IEDriverServer_x64_4.8.0.zip'
# download for win32
wget 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/ie/selenium-4.8.0/IEDriverServer_Win32_4.8.0.zip'
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

