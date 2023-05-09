# browser_drivers_mirror

[![Last Updated](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/HansBug/4ff4fe9d279fa2bc2cef37fec8cde822/raw/data_last_update.json)](${REPO_DIR})

Mirror of browser's drivers. The resource will be refreshed daily
on [HansBug/browser_drivers_mirror on huggingface](${REPO_DIR}).

## Supported Browsers

* [Google Chrome](${GOOGLE_DIR}) (up to [${GOOGLE_LATEST_RELEASE}](${GOOGLE_LATEST_RELEASE_DIR}))
    * [Linux Driver](${GOOGLE_LINUX64_URL})
    * [macOS Driver](${GOOGLE_MAC64_URL})
    * [Windows Driver](${GOOGLE_WIN64_URL})
* [Microsoft Edge](${EDGE_DIR) (up to [${EDGE_LATEST_RELEASE}](${EDGE_LATEST_RELEASE_DIR}))
    * [Linux Driver](${EDGE_LINUX64_URL})
    * [macOS Driver](${EDGE_MAC64_URL})
    * [Windows (64bit) Driver](${EDGE_WIN64_URL})
    * [Windows (32bit) Driver](${EDGE_WIN32_URL})
* [Mozilla Firefox](${FIREFOX_DIR}) (up to [${FIREFOX_LATEST_RELEASE}](${FIREFOX_LATEST_RELEASE_DIR}))
    * [Linux Driver](${FIREFOX_LINUX64_URL})
    * [macOS Driver](${FIREFOX_MAC64_URL})
    * [macOS (arch) Driver](${FIREFOX_MAC64_ARCH_URL})
    * [Windows (64bit) Driver](${FIREFOX_WIN64_URL})
    * [Windows (32bit) Driver](${FIREFOX_WIN32_URL})
* [Opera](${OPERA_DIR}) (up to [${OPERA_LATEST_RELEASE}](${OPERA_LATEST_RELEASE_DIR}))
    * [Linux Driver](${OPERA_LINUX64_URL})
    * [macOS Driver](${OPERA_MAC64_URL})
    * [Windows (64bit) Driver](${OPERA_WIN64_URL})
    * [Windows (32bit) Driver](${OPERA_WIN32_URL})
* [IE (not recommended)](${IE_DIR}) (up to [${IE_LATEST_RELEASE}](${IE_LATEST_RELEASE_DIR}))
    * [Windows (64bit) Driver](${IE_WIN64_URL})
    * [Windows (32bit) Driver](${IE_WIN32_URL})

## How to use

### With command line

* Chrome

```bash
# get latest version
wget -qO- '${GOOGLE_LATEST_RELEASE_URL}'

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
wget -qO- '${FIREFOX_LATEST_RELEASE_URL}'

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
wget -qO- '${OPERA_LATEST_RELEASE_URL}'

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
wget -qO- '${EDGE_LATEST_RELEASE_URL}'

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
wget -qO- '${IE_LATEST_RELEASE_URL}'

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

