from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b

w = interactive(f, a=10, b=10)
print(type(w))

display(w)

a = widgets.IntSlider()
display(a)
#python33