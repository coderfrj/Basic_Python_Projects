import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# producing data
rolls = [random.randrange(1, 7) for _ in range(10_000)]
values, frequencies = np.unique(rolls, return_counts=True)


# designing the bar
title = f'Rolling six-sided dice {len(rolls)} times'

sns.set_style('whitegrid')

axes = sns.barplot(x=values, y=frequencies)

axes.set_title(title)
axes.set(xlabel='Dice value', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=12, ha='center', va='center')

plt.show()
