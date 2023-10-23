import pandas as pd
import numpy as np
from etl_data_bouffe.obj.download_ciqual import downloadCiqual
from tools.data_treatment_class import TableManager


class ExtractMealDictionaryCiqual(TableManager):
    table_name = "meal_dict_ciqual.csv"

    def __init__(self):
        super().__init__()

    def process(self):
        file = downloadCiqual()
        file.read()

        df_raw = file.df_raw
        df_data = df_raw.loc[:, ['alim_grp_code', 'alim_ssgrp_code', 'alim_ssssgrp_code',
                                 'alim_grp_nom_fr', 'alim_ssgrp_nom_fr', 'alim_ssssgrp_nom_fr',
                                 'alim_code', 'alim_nom_fr', 'alim_nom_sci']]

        df_no_dup = df_data[~df_data.duplicated(subset=['alim_code'])]
        self.df_final = df_no_dup.replace("\<", "", regex=True).replace("\,", ".", regex=True).dropna()


if __name__ == "__main__":
    dictionary = ExtractMealDictionaryCiqual()
    dictionary.process()
    dictionary.save_data_table()
