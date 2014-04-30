'''
Makes some animations regarding isochrons
Created on 2014-04-26

@author: Nick Touran

Based on info in "Radiogenic Isotope Geology" by Dickin. 

Created to be featured on whatisnuclear.com's Age of Earth page at
http://www.whatisnuclear.com/physics/age_of_earth.html

License: CC BY

'''
import math

import pylab
from matplotlib import animation

NUMFRAMES=5
ax1=None

def plot_isochron(nframe):
    """
    Make and label a plot of an isochron. 
    
    Can be used as part of an animation
    
    Parameters
    ----------
    nframe : int
        the frame number. 
    
    See Also
    --------
    animate_isochron : animates these into a gif. 
    """
    # Rb-87 -> Sr-87
    halfLife = 48.8e9 # years
    decay_const = math.log(2)/halfLife
    sr87_sr86_0=0.712 # and Sr87 will build up with time. (this is usually calculated, not given). 
    rb87_sr86_0=[0,0.1,0.5,0.7,0.9]
    age = nframe/float(NUMFRAMES)*5e9
    rb87 = [r87i*math.exp(-age*decay_const) for r87i in rb87_sr86_0]
    sr87 = [sr87_sr86_0+rb87i*(math.exp(age*decay_const)-1) for rb87i in rb87]

    pylab.cla() # clear last frame
    pylab.title('Isotopic ratios {0:3.1f} billion years after sample was isolated'.format(age/1e9))
    
    pylab.plot(rb87, sr87, 'bo-')
    pylab.xlabel(r'$\frac{Rb87}{Sr86}$')
    pylab.ylabel(r'$\frac{Sr87}{Sr86}$')
    pylab.text(0.45,0.62,'All samples started out with the same amount of Sr87 relative to Sr86. \n'
                         'That\'s why the line is flat at t=0\n'
                        'But samples taken from different parts of the rocks have different Sr/Rb ratios.\n'
                        'As time goes on, radioactive Rb87 decays to become Sr87. \n'
                        'The slope of this line tells us how old the rock is.',ha='center')
    pylab.ylim(0.6,0.8)
    #pylab.text(0.4,0.65,r'$m=e^{{\lambda {0:0.4e}}}-1$'.format(age))
    
    
    # this is an inset axes over the main axes
#     a = pylab.axes([.65, .6, .2, .2], axisbg='y')
#     x_pos=[0.66,0.7]
#     a.bar(x_pos, [rb87[-1],sr87[-1]], align='center', alpha=0.4)
#     pylab.xticks(x_pos, ['Rb87','Sr-87'])
    
   
    
def animate_rb_sr():
    fig = pylab.figure()
    

    anim = animation.FuncAnimation(fig, plot_isochron, frames=NUMFRAMES)
    anim.save('rb-sr.gif', writer='imagemagick', fps=1);
 
 
if __name__=='__main__':
    animate_rb_sr()