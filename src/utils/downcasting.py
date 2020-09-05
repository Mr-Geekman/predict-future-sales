import numpy as np


def downcast_dtypes(df, from_bytes=64, to_bytes=32):
    '''Changes column types in the dataframe according to num_bytes
        `float64` type to `float{num_bytes}`
        `int64`   type to `int{num_bytes}`

    :param df: input dataframe
    :param from_bytes: num of bytes in transformed colummns
    :param to_bytes: num of bytes in result

    :returns: downcasted dataframe
    '''
    possible_bytes = (8, 16, 32, 64)
    if from_bytes not in possible_bytes:
        raise ValueError('Incorrect value of from_bytes')
    if to_bytes not in possible_bytes:
        raise ValueError('Incorrect value of to_bytes')
    
    # Select columns to downcast
    float_cols = [c for c in df if df[c].dtype == f'float{from_bytes}']
    int_cols =   [c for c in df if df[c].dtype == f'int{from_bytes}']
    
    # Downcast
    df[float_cols] = df[float_cols].astype(f'float{to_bytes}')
    df[int_cols]   = df[int_cols].astype(f'int{to_bytes}')
    
    return df
