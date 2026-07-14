def missing_values(df):

    return df.isnull().sum()


def duplicate_rows(df):

    return df.duplicated().sum()