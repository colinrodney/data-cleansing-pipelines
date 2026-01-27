def ingest_data():
    import pandas as pd
    df = pd.read_csv(r"C:\Users\Cessn\OneDrive\Desktop\data_cleansing_CI_CD_pipeline\.github\workflows\dirty_cafe_sales-csv.csv")
    df_2 = df.copy()
    print("Data ingested successfully!")
    df_2.info()
    return df_2
