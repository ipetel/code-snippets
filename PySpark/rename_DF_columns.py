import pyspark.sql.functions as F

df_data= '<your Spark DataFrame>'
new_header_list=['col0_new','col1_new']
old_header_list=['col0','col1']

def df_col_rename(X, to_rename, replace_with):
    """
    :param X: spark dataframe
    :param to_rename: list of original names
    :param replace_with: list of new names
    :return: dataframe with updated names
    """
    mapping = dict(zip(to_rename, replace_with))
    X = X.select([F.col(c).alias(mapping.get(c, c)) for c in to_rename])
    return X

df_data=df_col_rename(df_data,old_header_list,new_header_list)
