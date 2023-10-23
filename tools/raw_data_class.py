from pathlib import Path


class FileManager:
    """A class for downloading and managing files in a specific directory structure.

        Attributes:
            raw_data (str): The root directory for raw data.
            source_name (str): The name of the data source.
            folder_name (str): The name of the download folder.

        Args:
            raw_data (str): The root directory for raw data.
            source_name (str): The name of the data source.
            folder_name (str): The name of the download folder.
        """

    source_name: str
    source_url: str
    folder_name: str
    file_name: str

    def __init__(self):
        self.file_path = Path('etl_data_bouffe') / Path("raw_data") / self.source_name / self.folder_name

        self.file_path.mkdir(parents=True, exist_ok=True)
