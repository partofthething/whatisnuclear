"""
Basic plots describing radioactive decay. 

Made by N. Touran for whatisnuclear.com. 

Created to be featured on whatisnuclear.com's Age of Earth page at
http://www.whatisnuclear.com/physics/age_of_earth.html

"""

import math

import pylab

def basicHalfLife():
    """
    Plot some basic traces of number vs. time with varying half lives
    """
    halfLives=[50,100,200,300]
    time = pylab.linspace(0,500,100)
    N0=100
    pylab.figure()
    for halfLife in halfLives:
        dec = math.log(2)/halfLife
        y = [N0*math.exp(-dec*ti) for ti in time]
        pylab.plot(time,y,label='Half-life = {0} years'.format(halfLife))
        ax= pylab.gca()
        ax.arrow(halfLife, N0*0.5, 0.0, -N0*0.5,head_width=5.0, head_length=N0*0.03, 
                 length_includes_head=True,fc='k', ec='k',alpha=0.7,linestyle='dashed')

    pylab.grid(color='0.7')
    pylab.ylabel('Percentage of atoms remaining (%)')
    pylab.xlabel('Time (years)')
    pylab.legend(loc='upper right')
    pylab.axhline(y=N0*0.5,xmax=3/5.,color='k',ls='--')

    pylab.show()


def plotLeadUranium():
    """
    Make a plot of U-238 turning in Pb-206
    """
    secondsPerYear=365.25*3600*24
    halfLife = 4.47e9*secondsPerYear # 4.47 billion years (in seconds)
    dec = math.log(2)/halfLife
    time = pylab.linspace(0,5e9,100)
    N0=1.0
    u238  = [N0*math.exp(-dec*ti*secondsPerYear) for ti in time]
    pb206 = [u238[-1]*(math.exp(dec*ti*secondsPerYear)-1) for ti in time]
    pylab.figure()
    pylab.plot(time,u238,label='Uranium-238 atoms')
    pylab.plot(time,pb206,label='Lead-206 atoms')
    pylab.grid(color='0.7')
    pylab.ylabel('Relative number of atoms')
    pylab.xlabel('Time (years)')
    pylab.legend(loc='upper right')
    pylab.show()
    
if __name__=='__main__':
    basicHalfLife()
    plotLeadUranium()
    
