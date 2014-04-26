import math

import pylab

halfLives=[50,100,200,300]
time = pylab.linspace(0,500,100)
N0=100

for halfLife in halfLives:
    dec = math.log(2)/halfLife
    y = [N0*math.exp(-dec*ti) for ti in time]
    pylab.plot(time,y,label='Half-life = {0} years'.format(halfLife))
    ax= pylab.gca()
    ax.arrow(halfLife, N0*0.5, 0.0, -N0*0.5,head_width=5.0, head_length=N0*0.03, length_includes_head=True,fc='k', ec='k',alpha=0.7,linestyle='dashed')

pylab.grid(color='0.7')
pylab.ylabel('Percentage of atoms remaining (%)')
pylab.xlabel('Time (years)')
pylab.legend(loc='upper right')
pylab.axhline(y=N0*0.5,xmax=3/5.,color='k',ls='--')

pylab.show()

