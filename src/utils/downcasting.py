import numpy as np


def downcast_dtypes(df):
    '''
    Changes column types in the dataframe: 
        `float64` type to `float32`
        `int64`   type to `int32`
    '''
    
    # Select columns to downcast
    float_cols = [c for c in df if df[c].dtype == 'float64']
    int_cols =   [c for c in df if df[c].dtype == 'int64']
    
    # Downcast
    df[float_cols] = df[float_cols].astype(np.float32)
    df[int_cols]   = df[int_cols].astype(np.int32)
    
    return df
