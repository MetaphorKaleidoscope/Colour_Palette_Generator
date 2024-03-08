import numpy as np
from numpy import reshape
import matplotlib.pyplot as plt
from PIL import Image  # for reading image files
import pandas as pd


"""# Use your Own Image!"""
FILE_NAME = 'static/img/jellyfish.jpg'
my_array = np.array(Image.open(FILE_NAME))
fig1 = plt.figure(1)
plt.imshow(my_array)
size = my_array.shape
array_rgb = reshape(my_array, (size[0]*size[1], size[2]))

if '.png' in FILE_NAME:
    my_array_rgb = array_rgb[:, :-1]
else:
    my_array_rgb = array_rgb

df = pd.DataFrame(my_array_rgb)
df.columns = ['r', 'g', 'b']
df['color_str'] = df["r"].astype(str) + df['g'].astype(str) + df['b'].astype(str)
df['hex_code'] = '#' + df['r'].apply(lambda x: f'{x:02x}') + df['g'].apply(lambda x: f'{x:02x}') \
                 + df['b'].apply(lambda x: f'{x:02x}')
df['times'] = 1
#
repeat = df.groupby(['color_str', 'r', 'g', 'b', 'hex_code'], as_index=False).agg({'times': pd.Series.count}).\
    sort_values('times', ascending=False)
total = len(repeat)
no_colors = 10
repeat['percentage'] = repeat['times']/total
more_repeat = repeat.head(no_colors)
colors_extract = more_repeat.values.tolist()
print(more_repeat)
