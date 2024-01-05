"""
Fields defined in "PMD_FIELDS" are added using the information from the API.
"""

from yt_dlp.postprocessor.common import PostProcessor


PMD_FIELDS = {
    'peloton_meta': 'data',
}

SUPPORTED_EXTRACTORS = {
    'Peloton',
}


class pelotonmetaPP(PostProcessor):
    def run(self, info):
        extractor = info['extractor_key']
        if extractor not in SUPPORTED_EXTRACTORS:
            self.to_screen(f'{self.PP_NAME} is not supported for {extractor}')
            return [], info

        self.to_screen(f'{self.PP_NAME} is enabed')

        metadata = self._download_json(
            f'https://api.onepeloton.com/api/ride/{info["id"]}/details?stream_source=multichannel') or {}

        peloton_data = {}
        peloton_data['data'] = metadata

        info['PMD'] = {
            'response': peloton_data,
            'original': {k: info.get(k) for k in PMD_FIELDS.keys()}
        }
        if peloton_data:
            info.update({k: peloton_data.get(v) for k, v in PMD_FIELDS.items()})

        return [], info