import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from logic import bubble_sort


DATA_SIZE = 30
DELAY_MS = 120

data = [random.randint(1, 100) for _ in range(DATA_SIZE)]

fig, ax = plt.subplots()
bars = ax.bar(range(len(data)), data, color="lightgray")

ax.set_title("Bubble Sort Visualization")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.set_ylim(0, max(data) + 10)


def update(frame):
    arr, i, j, swapped = frame

    for idx, bar in enumerate(bars):
        bar.set_height(arr[idx])
        bar.set_color("lightgray")

    # highlight compared bars
    bars[i].set_color("orange")
    bars[j].set_color("orange")

    # highlight swap
    if swapped:
        bars[i].set_color("red")
        bars[j].set_color("red")

    return bars


ani = animation.FuncAnimation(
    fig,
    update,
    frames=bubble_sort(data),
    interval=DELAY_MS,
    repeat=False
)

plt.show()
