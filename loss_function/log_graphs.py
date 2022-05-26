# Make a chart with 6 log graphs

import numpy as np
import matplotlib.pyplot as plt
import math

# This code uses the OO-style matplotlib, using subplots().
fig, ax = plt.subplots(3, 3,   # 3 rows, 3 col of subplots
    figsize = (16,17)          # dimensions of the figure in inches
)


#########################################################################
#  Title Area
#########################################################################

# main title above everything else
plt.suptitle("Log Graphs", 
    fontsize=30,
    fontweight='bold'
)

# text just below the title
plt.figtext(0.06, 0.92,
    "Since it's undefined, taking log(0) or log( negative number) will result in python ValueError: math domain error",
    ha="left",
    fontsize=18)


#########################################################################
#  Helper Functions 
#########################################################################

def make_text_section( _ax):
    # remove spines
    for loc in ['top','right','bottom','left']:
        _ax.spines[loc].set_visible(False)

    # remove x ticks and y ticks
    _ax.set_xticks([])
    _ax.set_yticks([])


TOP = 0.94
CENTER = 0.4
BOTTOM = 0.04

def write_text( _ax, y, txt, _fontsize=28):
    _ax.text(0.3,
        y,
        txt,
        ha="left",  # horizontalalignment
        va= "top" if y==TOP else "bottom",
        fontsize=_fontsize)


#########################################################################
#  subplot 0,0:  
#########################################################################

make_text_section(ax[0][0])
write_text( ax[0,0], CENTER, "For 0<x<10") 


#########################################################################
#  subplot 0,1: 
#########################################################################

ax[0,1].set_title("y = log(x)", 
    {'color':'blue', 'size':20})
x = np.arange(1,10)
y = [ math.log(i) for i in x]
ax[0,1].plot(x,y,':r')


#########################################################################
#  subplot 0,2: 
#########################################################################

ax[0,2].set_title("y = -log(x)", 
    {'color':'blue', 'size':20})
x = np.arange(1,10)
y = [ -math.log(i) for i in x]
ax[0,2].plot(x,y,':r')


#########################################################################
#  subplot 1,0:
#########################################################################

make_text_section(ax[1,0])
write_text( ax[1,0], CENTER, "For 0<x<1") 


#########################################################################
#  subplot 1,1:  
#########################################################################

ax[1,1].set_title("y = log(x)", 
    {'color':'blue', 'size':20})
# Can't take a log of 0 or negative number, so start x above 0
x = np.linspace(0.1,1,9)  # 0.1, 0.2, ...  1.0
y = [ round(math.log(i), 2) for i in x]
ax[1,1].plot(x,y,':b')


#########################################################################
#  subplot 1,2:  
#########################################################################

ax[1,2].set_title("y = -log(x)", 
    {'color':'blue', 'size':20})
x = np.linspace(0.1,1,9)  # 0.1, 0.2, ...  1.0
y = [ -round(math.log(i), 2) for i in x]
ax[1,2].plot(x,y,':b')


#########################################################################
#  subplot 2,0:  
#########################################################################

make_text_section(ax[2,0])
write_text( ax[2,0], CENTER, "For 0<x<1") 


#########################################################################
#  subplot 2,1:  
#########################################################################

ax[2,1].set_title("y = log( 1 - x )", 
    {'color':'blue', 'size':20})
x = np.linspace(0,0.9,9)  # 0.0, 0.1, 0.2, ...  0.9
y = [ round(math.log(1-i), 2) for i in x]
ax[2,1].plot(x,y,':b')


#########################################################################
#  subplot 2,2:  
#########################################################################

ax[2,2].set_title("y = -log( 1 - x )", 
    {'color':'blue', 'size':20})
x = np.linspace(0,0.9,9)  # 0.0, 0.1, 0.2, ...  0.9
y = [ -round(math.log(1-i), 2) for i in x]
ax[2,2].plot(x,y,':b')


#########################################################################

# adjust the spacing between subplots
fig.subplots_adjust(left=0.06,
    right=0.9,
    bottom=0.07,
    top=0.86,
    wspace=0.2,
    hspace=0.5)


plt.figtext(0.06, 0.02,
    "Chart: @roannav",
    ha="left",
    fontsize=14)

plt.savefig('log_graphs.png')  # savefig must happen before show()
