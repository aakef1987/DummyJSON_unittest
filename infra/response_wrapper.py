class ResponseWrapper:
    def __init__(self, response):
        self.raw = response

    @property
    def status_code(self):
        return self.raw.status_code

    def json(self):
        try:
            return self.raw.json()
        except ValueError:
            return None

    @property
    def success(self):
        return 200 <= self.raw.status_code < 300

    def get(self, key, default=None):
        data = self.json()
        return data.get(key, default) if isinstance(data, dict) else default
