import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, Slider
from typing import List
from knn_container import NeighborContainer

classes = ['Class 1', 'Class 2']


x = []
y = []
k = 3
point_classes = []
area = 500  # 0 to 15 point radii


fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(left = 0.3, bottom = 0.25)
plt.xlim([0, 40])
plt.ylim([0, 40])
p = ax.scatter(x, y, s=area, c=[classes.index(c) for c in point_classes], alpha=0.5)

def reset_plot():
    global p
    p.remove()
    p = ax.scatter(x, y, s=area, c=[classes.index(c) for c in point_classes], alpha=0.5)
    fig.canvas.draw()


mode = 'Train'



#######
# GUI #
#######

def set_mode(new_mode):
    global mode
    mode = new_mode
    print(f"Setting mode to {mode}")

ax_radio = plt.axes([0.02, 0.2, 0.2,0.3])
train_eval = RadioButtons(ax_radio, ['Train', 'Eval'], active = 0, activecolor = 'r')
train_eval.on_clicked(set_mode)


selected_class = classes[0]
def set_class(new_class):
    global selected_class
    selected_class = new_class
    print(f"Setting mode to {selected_class}")
ax_radio = plt.axes([0.02, 0.5, 0.2,0.3])
class_button = RadioButtons(ax_radio, classes, active = 0, activecolor = 'r')
class_button.on_clicked(set_class)


def clear(val):
    x.clear()
    y.clear()
    point_classes.clear()
    reset_plot()

ax_button = plt.axes([0.25, 0.1, 0.08,0.05])
clear_button = Button(ax_button, 'Clear', color = 'white', hovercolor = 'grey')
clear_button.on_clicked(clear)


def remove_last(val):
    i = len(x) - 1
    x.pop(i)
    y.pop(i)
    point_classes.pop(i)
    reset_plot()

ax_button2 = plt.axes([0.45, 0.1, 0.18,0.05])
rm_button = Button(ax_button2, 'Remove last', color = 'white', hovercolor = 'grey')
rm_button.on_clicked(remove_last)


def set_k(val):
    global k
    k = int(val)


k_space = plt.axes([0.25, 0.05, 0.38, 0.05])
k_slider = Slider(k_space, "Neighbors", 1, 5, 1, valstep=[i for i in range(1, 6)])
k_slider.on_changed(set_k)

#########
# CLICK #
#########

def onclick(event):
    if not event.inaxes == ax:
        return

    if (mode == 'Train'):
        new_point(event, selected_class)
    elif mode == 'Eval':
        eval_point(event)


def new_point(event, cls):
    x.append(event.xdata)
    y.append(event.ydata)
    point_classes.append(cls)
    reset_plot()

def eval_point(event):
    nc = NeighborContainer(k, x, y, point_classes)
    nc.test_point((event.xdata, event.ydata))

    new_point(event, nc.vote())
    circle_points(nc.get_neighbor_indexes())


def circle_points(indexes : List[int]):
    temp_x = x.copy()
    temp_y = y.copy()
    temp_areas = [area for _ in range(len(x))]
    temp_classes = [classes.index(c) for c in point_classes]

    for index in indexes:
        x_coor, y_coor = x[index], y[index]
        temp_x.append(x_coor)
        temp_y.append(y_coor)
        temp_areas.append(80)
        temp_classes.append(0.5)

    global p
    p.remove()
    p = ax.scatter(temp_x, temp_y, s= temp_areas, c= temp_classes, alpha=0.5)
    fig.canvas.draw()



cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()