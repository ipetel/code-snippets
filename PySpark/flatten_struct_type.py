def flatten_struct(df):
    struct_cols = [name for name, dtype in df.dtypes if 'struct' in dtype]
    if struct_cols:
        col_to_flatten=[{'from':f'{nc}.{c}','to':f'{nc}_{c}'} for nc in struct_cols for c in df.select(f'{nc}.*').columns]
        for col in col_to_flatten:
            df = df.withColumn(col['to'],F.col(col['from']))
        
        for col in struct_cols:
            df = df.drop(col)
            
        return df    
    else:
        return df
