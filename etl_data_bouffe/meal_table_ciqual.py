import pandas as pd
import numpy as np
from etl_data_bouffe.obj.download_ciqual import downloadCiqual
from tools.data_treatment_class import TableManager


class TreatTableCiqual(TableManager):
    table_name = "ciqual.csv"

    def __init__(self):
        super().__init__()

    def process(self):
        file = downloadCiqual()
        file.read()

        df_raw = file.df_raw
        df_raw.rename(columns={
            "Energie, Règlement UE N° 1169/2011 (kcal/100 g)": "kcal",
            "Protéines, N x 6.25 (g/100 g)": "protein",
            "Glucides (g/100 g)": "glucid",
            "Lipides (g/100 g)": "lipid"}, inplace=True)

        df_data = df_raw.loc[:, ['alim_code', 'kcal', 'protein', 'glucid', 'lipid']]

        df_no_dup = df_data[~df_data.duplicated(subset=['alim_code'])]
        df_no_na = df_no_dup.replace("\<", "", regex=True).replace("\,", ".", regex=True).dropna()

        df_float = df_no_na.astype(
            {
                'kcal': 'float',
                'protein': 'float',
                'glucid': 'float',
                'lipid': 'float',
            }
        )

        df_kcal_exist = df_float[df_float['kcal'] > 0]

        self.df_final = df_kcal_exist.copy()

if __name__ == "__main__":
    table = TreatTableCiqual()
    table.process()
    table.save_data_table()