
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


frequency_head = 0
frequency_tail = 0

coin = ['head', 'tail']
for i in range(6_000_000):
    face = random.choice(coin)
    if face == 'head':
        frequency_head += 1
    elif face == 'tail':
        frequency_tail += 1

values, frequencies = ['head', 'tail'], [frequency_head, frequency_tail]

##
title = 'Fliping Coin 6,000,000 times Simulation '

sns.set_style('darkgrid')

axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)


axes.set_ylim(top=max(frequencies) * 1.10)

for value, frequency in zip(axes.patches, frequencies):
    text_x = value.get_x() + value.get_width() / 2
    text_y = value.get_height()
    text = f'{frequency:,}\n\n{frequency / 6_000_000:.3%}'
    axes.text(text_x,text_y, text, fontsize=12, ha='center', va='center')

plt.show()