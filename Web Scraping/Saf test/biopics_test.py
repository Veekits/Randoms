import pandas as pd

def process_data():
    # Do not alter this line.
    biopics = pd.read_csv("biopics.csv", encoding='latin-1')
    # Write your code here.
    unique_data = df.drop_duplicates(biopics)
    # Remember to return the right object.
    df = pd.DataFrame(unique_data)
    print(df)
    return biopics.reset_index(drop=True)

