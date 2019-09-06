"""
------------------------------------------------------------------------------
Author: Paul Barrett (paul.barrett@metoffice.gov.uk)
Copyright: 2019 (c) Met Office, Exeter, UK
Language: Python 3.0
Created: 06/09/2019

------------------------------------------------------------------------------

This module has a class that bins for aerosol or cloud particle size 
distributions and then classes that inherit this behaviour all the way to 
instances for particilar types of instrument and actual isntruments

There are methods that permit standard operations on these bins


CLASSES:



METHODS:


TODO:


HISTORY:
Last modified: 06/09/2019

    06/09/19 - PB - created

EXAMPLES:

@author: frtt paul.barrett@metoffice.gov.uk




"""

# IMPORTS
import numpy as np


# CLASSESS

class bins:
    """ Bin dimensions for a particle size spectrometer

    INPUTS:



    OUTPUT:

    HISTORY:


    """

    def __init__(self, lower, upper, centre, width, 
                n_channels, units, etc
                lower_error, upper_error, centre_error, width_error)
        """
        This is just the dimensions and measurements.
        
        If given lowers and uppers then get centre and width

        if given centre and width then get lower and upper

        What about n_boundaries = n_channels+1?


        Methods compute derived parameters like dlogd, area, volume
        but NOT mass - that can be in an inheritor, which also has density


        COPY FUNCTIONALITY FROM EXISTING BIN_MAKER.PRO

        """


        # CHECK WHAT YOU HAVE (lowers, upper) or (centre, width)
        # and get the opposite
        if lower is not None:
            self.lower = lower
        else:
            try:
                self.lower = self.centre - self.width
            except:
                print("you gotta give me summat to work with")

        # SAME GOES FOR UPPER

        # AND CENTRE


        # AND WIDTH


        # AND ALL ERRORS - WHERE FROM IF NOT DEFINE?
        if lower_error is not None:
            self.lower_error = lower_error
        else:
            self.lower_error = '<<<*** MISSING ***>>>'


        









        if units is not None:
            self.units = units
        else:
            self.units = 'arbitrary'



    def get_dlogd(self)
        """
        produce dlogd for the bins

        WHAT BASE DO YOU WANT YOUR LOG?
        THIS ONE IS NATURAL

        INPUTS:  
            upper
            lower

        OUTPUTS: dlogd


        HISTORY


        """
        
        dlogd = np.alog10(self.upper) - np.alog10(self.lower)

   
    def get_dlog10d(self)
        """
        copy t'uther one but with the base 10 logarithm

        - CAN I COMBINE THIS WITH THE OTHER ONE AND CHOOSE WHEN NEEDED
        AND THEN ALSO CHOOSE AN ARBITRARY BASE COS WHY NOT?

        """
        
        # IS THIS NATURAL LOG? #
        dlogd = np.alog(self.upper) - np.alog(self.lower)


    def get_moment(self, index)
        """
        get area, volume, nth moment

        which elements, upper, lower, centre? 
        - what about say, area, volume, reflectivity weighted centre?
        """















    # WHAT IS THIS - IS IT FOR THE CLASS OR THE METHODS?
    # I THINK FOR THE CLASS
    # The str is good to print into a log file, 
    #   where as 
    # repr can be re-purposed if you want to 
    # run it directly or dump it as commands into a file. 
    #https://stackoverflow.com/questions/3691101/
    #what-is-the-purpose-of-str-and-repr
    def __str__(self):
        return 'Bins boundaries for a spectrometer'

    __repr__ = __str__





