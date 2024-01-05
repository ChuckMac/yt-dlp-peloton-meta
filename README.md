A [yt-dlp](https://github.com/yt-dlp/yt-dlp) postprocessor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) for Peloton.

Stores the full json metadata from the Peloton workout into the "peloton_meta" field of the output json.


## Installation

Requires yt-dlp `2023.01.01` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/chuckmac/yt-dlp-peloton-meta/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.

## Usage

Pass `--use-postprocessor  pelotonmeta:when=pre_process` to activate the PostProcessor