# browser_drivers_mirror

[![Last Updated](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/HansBug/4ff4fe9d279fa2bc2cef37fec8cde822/raw/data_last_update.json)](https://huggingface.co/HansBug/browser_drivers_mirror)

Mirror of browser's drivers. The resource will be refreshed daily
on [HansBug/browser_drivers_mirror on huggingface](https://huggingface.co/HansBug/browser_drivers_mirror).

## Supported Browsers

* [Google Chrome](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/google) (up
  to [${GOOGLE_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/google/${GOOGLE_LATEST_RELEASE}))
    * [Linux Driver](${GOOGLE_LINUX64_URL})
    * [macOS Driver](${GOOGLE_MAC64_URL})
    * [Windows Driver](${GOOGLE_WIN64_URL})
* [Microsoft Edge](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/edge) (up
  to [${EDGE_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/edge/${EDGE_LATEST_RELEASE}))
    * [Linux Driver](${EDGE_LINUX64_URL})
    * [macOS Driver](${EDGE_MAC64_URL})
    * [Windows (64bit) Driver](${EDGE_WIN64_URL})
    * [Windows (32bit) Driver](${EDGE_WIN32_URL})
* [Mozilla Firefox](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/firefox) (up
  to [${FIREFOX_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/firefox/${FIREFOX_LATEST_RELEASE}))
    * [Linux Driver](${FIREFOX_LINUX64_URL})
    * [macOS Driver](${FIREFOX_MAC64_URL})
    * [macOS (arch) Driver](${FIREFOX_MAC64_ARCH_URL})
    * [Windows (64bit) Driver](${FIREFOX_WIN64_URL})
    * [Windows (32bit) Driver](${FIREFOX_WIN32_URL})
* [Opera](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/opera) (up
  to [${OPERA_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/opera/${OPERA_LATEST_RELEASE}))
    * [Linux Driver](${OPERA_LINUX64_URL})
    * [macOS Driver](${OPERA_MAC64_URL})
    * [Windows (64bit) Driver](${OPERA_WIN64_URL})
    * [Windows (32bit) Driver](${OPERA_WIN32_URL})
* [IE (not recommended)](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/ie) (up
  to [${IE_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/ie/${IE_LATEST_RELEASE}))
    * [Windows (64bit) Driver](${IE_WIN64_URL})
    * [Windows (32bit) Driver](${IE_WIN32_URL})

## How to use

### With command line

* Chrome

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/LATEST_RELEASE'

# download for linux
wget '${GOOGLE_LINUX64_URL}'
# download for macos
wget '${GOOGLE_MAC64_URL}'
# download for windows
wget '${GOOGLE_WIN64_URL}'
```

* Firefox

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/LATEST_RELEASE'

# download for linux
wget '${FIREFOX_LINUX64_URL}'
# download for macos
wget '${FIREFOX_MAC64_URL}'
# download for macos (arch)
wget '${FIREFOX_MAC64_ARCH_URL}'
# download for win64
wget '${FIREFOX_WIN64_URL}'
# download for win32
wget '${FIREFOX_WIN32_URL}'
```

* Opera

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/LATEST_RELEASE'

# download for linux
wget '${OPERA_LINUX64_URL}'
# download for macos
wget '${OPERA_MAC64_URL}'
# download for win64
wget '${OPERA_WIN64_URL}'
# download for win32
wget '${OPERA_WIN32_URL}'
```

* Edge

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/edge/LATEST_STABLE'

# download for linux
wget '${EDGE_LINUX64_URL}'
# download for macos
wget '${EDGE_MAC64_URL}'
# download for win64
wget '${EDGE_WIN64_URL}'
# download for win32
wget '${EDGE_WIN32_URL}'
```

* IE

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/ie/LATEST_RELEASE'

# download for win64
wget '${IE_WIN64_URL}'
# download for win32
wget '${IE_WIN32_URL}'
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

