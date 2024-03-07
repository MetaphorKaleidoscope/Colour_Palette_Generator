"""
Program to image colour palette generator
"""

import numpy as np
from numpy import reshape
from PIL import Image
import pandas as pd


def colour_palette(file_name, no_colors):
    my_array = np.array(Image.open(file_name))
    size = my_array.shape
    array_rgb = reshape(my_array, (size[0]*size[1], size[2]))

    if '.png' in str(file_name):
        my_array_rgb = array_rgb[:, :-1]
    else:
        my_array_rgb = array_rgb

    df = pd.DataFrame(my_array_rgb)
    df.columns = ['r', 'g', 'b']
    df['color_str'] = df["r"].astype(str) + df['g'].astype(str) + df['b'].astype(str)
    df['hex_code'] = '#' + df['r'].apply(lambda x: f'{x:02x}') + df['g'].apply(lambda x: f'{x:02x}') \
                     + df['b'].apply(lambda x: f'{x:02x}')
    df['times'] = 1

    repeat_total = df.groupby(df.hex_code.str[0:2], sort=False).agg({'times': 'sum', 'hex_code': 'first'}).\
        sort_values('times', ascending=False)
    total = len(df)
    repeat_total['percentage'] = repeat_total['times']/total
    more_repeat = repeat_total.head(no_colors)
    return more_repeat
