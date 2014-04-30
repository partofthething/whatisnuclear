'''
Created on Apr 28, 2014

@author: nick touran

Reads in actual meteorite and terrestrial Pb isotopics and computes the age of earth. 

Data source: Murthy, Patterson, "Primary Isochron of Zero Age for Meteorites and the Earth,"
             J. Geophysical Research, 67, 1, (1962).
             
Created to be featured on whatisnuclear.com's Age of Earth page at
http://www.whatisnuclear.com/physics/age_of_earth.html
'''
import itertools
import math

from scipy.stats import linregress
import scipy.optimize
import pylab

# decay constants of Uranium isotopes
dec_235=9.8485e-10
dec_238=1.55125e-10 # /yr

def loadData(fName='lead_data.txt'):
    """
    read lead isotopic data from text file
    
    Returns
    -------
    leadData : dict
        dataType : [(name, pb206, pb207, pb208)] ratio values (over pb204) 
    """
    leadData = {}
    with open(fName) as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            
            elif ',' not in line:
                dataType=line
                leadData[dataType]=[]
            else:
                name, pb206, pb207, pb208 = line.split(',')
                leadData[dataType].append((name, float(pb206), float(pb207), float(pb208)))
    return leadData
            
def plotData(leadData):
    """
    Plot the data from the table and fit a linear regression. return the slope
    """
    markers=itertools.cycle(['o','v','s']) # different types of markers for the plot
    allX,allY=[],[]
    for dataType, vals in leadData.items():
        xy = [(pb206, pb207) for (name, pb206, pb207, pb208) in vals]
        x,y = zip(*xy)
        pylab.plot(x,y,markers.next(),label=dataType)
        allX.extend(x)
        allY.extend(y) # for regression
    
    # compute the best linear regression
    slope, intercept, rval,pval,stderr = linregress(pylab.array(allX),
                                                    pylab.array(allY))

    
    # plot the regression line
    xi = pylab.linspace(min(allX),max(allX),100)
    yi = [slope*xii+intercept for xii in xi]
    pylab.plot(xi,yi,'-',label='Best fit ($R^2$={0:.4f})'.format(rval))
    
    # add some labels to the axes, etc. 
    pylab.grid(color='0.7')
    pylab.legend(loc='upper left',numpoints=1)
    pylab.xlabel('Pb206/Pb204')
    pylab.ylabel('Pb207/Pb204')
    pylab.savefig('pb-pb-isochron.png')
    
    return slope

def slopeEqn(t,slope):
    """
    Evaluate the isochron equation for any time or slope. 
    
    This is needed as a helper function to the numerical root finder in calcAge.
    """
    # 137.88 is the current abundance ratio of U238/U235. 
    return slope-1.0/137.88*(math.exp(dec_235*t)-1)/(math.exp(dec_238*t)-1)
            
def calcAge(slope):
    """
    Numerically solve for the age of the Earth given a slope of the geochron."""
    val=scipy.optimize.brentq(slopeEqn,100,10e9,args=(slope,))
    return val
            
if __name__ == '__main__':
    ld = loadData()
    slope = plotData(ld)
    age = calcAge(slope)
    print('Slope of Geochron is {0}'.format(slope))
    print('Age of earth is: {0:.2f} billion years'.format(age/1e9))
    