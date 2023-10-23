import requests
import pandas as pd
from tools.raw_data_class import FileManager


class downloadCiqual(FileManager):
    """
        A class for downloading Ciqual data.

        Attributes:
            source_name (str): The name of the data source.
            source_url (str): The URL of the data source.
            folder_name (str): The name of the folder where data will be saved.
            file_name (str): The base name for downloaded files.
    """
    source_name: str = 'ciqual'
    source_url: str = "https://ciqual.anses.fr/cms/sites/default/files/inline-files/Table%20Ciqual%202020_FR_2020%2007%2007.xls"
    folder_name: str = 'ciqual_meal_table'
    file_name: str = 'meal_table.xls'

    def __init__(self):
        super().__init__()
        self.df_raw = None

    def extract_url_files(self):
        response = requests.get(self.source_url)

        file_path_with_name = self.file_path / self.file_name
        if response.status_code == 200:
            with open(file_path_with_name, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded and saved at {file_path_with_name}")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")

    def custom_converter(value):
        if isinstance(value, str):
            # Replace "< 0,5" with 0.5
            value = value
        return value

    def read(self):
        self.df_raw = pd.read_excel(self.file_path / self.file_name, na_values=['-', 'traces'], decimal=',')


if __name__ == "__main__":
    file = downloadCiqual()
    file.extract_url_files()
    file.read()
