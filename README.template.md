# browser_drivers_mirror

[![Last Updated](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/HansBug/4ff4fe9d279fa2bc2cef37fec8cde822/raw/data_last_update.json)](https://huggingface.co/HansBug/browser_drivers_mirror)

Mirror of browser's drivers. The resource will be refreshed daily
on [HansBug/browser_drivers_mirror on huggingface](https://huggingface.co/HansBug/browser_drivers_mirror).

## Supported Browsers

* [Google Chrome](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/google) (up
  to [${GOOGLE_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/google/${GOOGLE_LATEST_RELEASE}))
* [Microsoft Edge](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/edge) (up
  to [${EDGE_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/edge/${EDGE_LATEST_RELEASE}))
* [Mozilla Firefox](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/firefox) (up
  to [${FIREFOX_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/firefox/${FIREFOX_LATEST_RELEASE}))
* [Opera](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/opera) (up
  to [${OPERA_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/opera/${OPERA_LATEST_RELEASE}))
* [IE (not recommended)](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/ie) (up
  to [${IE_LATEST_RELEASE}](https://huggingface.co/HansBug/browser_drivers_mirror/tree/main/ie/${IE_LATEST_RELEASE}))

## How to use

### With command line

* Chrome

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/google/LATEST_RELEASE'
```

* Firefox

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/firefox/LATEST_RELEASE'
```

* Opera

```bash
# get latest version
wget -qO- 'https://huggingface.co/HansBug/browser_drivers_mirror/resolve/main/opera/LATEST_RELEASE'
```

* Edge

Edge's version metadata is written in `utf-16` encoding, so it is not recommended to be read with `wget` command.

### With [hf-webdriver-manager](https://github.com/HansBug/hf_webdriver_manager)

We recommend you to use [hf-webdriver-manager](https://github.com/HansBug/hf_webdriver_manager) instead of native
command line. This is written in Python, can be installed with the following command:

```bash
pip install hf-webdriver-manager
```
