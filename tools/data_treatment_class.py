from pathlib import Path


class TableManager:
    table_name: str

    def __init__(self):
        self.database_path = Path('database')
        self.file_path = self.database_path
        self.file_path.mkdir(parents=True, exist_ok=True)

        self.df_final = None

    def save_data_table(self):
        self.df_final.to_csv(self.file_path / Path(self.table_name), index=False, sep='\t')
