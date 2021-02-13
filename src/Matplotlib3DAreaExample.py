#!/usr/bin/env python3

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

mpl.style.use("seaborn")

countries = ["Brazil", "USA", "France", "Germany"]
months = ["Apr", "May", "Jun", "Jul"]
temperatures = [
    # Each column is a country, each row is a month.
    [24.6, 11.1, 09.9, 07.0],  # Apr: Brazil, USA, France, Germany
    [23.7, 16.0, 13.6, 11.7],  # May: Brazil, USA, France, Germany
    [22.8, 20.4, 16.9, 15.0],  # Jun: Brazil, USA, France, Germany
    [22.4, 22.9, 19.2, 16.6],  # Jul: Brazil, USA, France, Germany
]

# For textual data we need a numeric representation.
ticks_countries = range(0, len(countries))
ticks_months = range(0, len(months))

x, y = np.meshgrid(ticks_countries, ticks_months)
z = np.asarray(temperatures)


fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
plt.title("Average Temperature in Countries")

# Plotting the area.
ax.plot_surface(
    x,
    y,
    z,
    rstride=1,
    cstride=1,
    cmap="viridis",
    antialiased=True,
    shade=True,
    alpha=0.95,
    edgecolor="black",
    linewidth=0.3,
    zorder=1,
)

# Plotting the text labels for each data point.
for month, i_month in zip(months, ticks_months):
    for country, i_country in zip(countries, ticks_countries):
        temperature = temperatures[i_month][i_country]
        # Parameters are: position in X, position in Y, position in Z, text to plot.
        ax.text(
            i_country,
            i_month,
            temperature,
            temperature,
            color="black",
            ha="left",
            va="baseline",
            bbox={"pad": 2, "alpha": 0.5, "facecolor": "white", "linewidth": 0,},
        )

# Now we set the texts for the numeric representation of textual data.
ax.set_xlabel("Countries")
ax.set_xticks(ticks_countries)
ax.set_xticklabels(countries)

ax.set_ylabel("Months")
ax.set_yticks(ticks_months)
ax.set_yticklabels(months)

ax.set_zlabel("Avg Temperature (C)")

fig.set_size_inches(10, 8)
# plt.show()
plt.savefig('./Matplotlib3DAreaExample.png', dpi=150, bbox_inches='tight')
