class FileSharer:
    """Uploading a pdf file filstack and share the URL"""

    def __init__(self, filepath, api_key="Ay8jx9TiXQD6Cr93xc8tpz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url