# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:57:33 2016

@author: Jeffrey
"""
import math

def getDistance(detectedCircle):
    w=2*detectedCircle[2]    
    x=w**(-0.973)
    m=14339
    #b=1263.4
    dist = m*x
    print "radious is " + str(w)
    print "distance to the ball is: " + str(dist)
    return dist
    
def getDistance1(balldimator, detectedCircle):
    #TODO     
    return 0
def getDistance2balls(detectedCircle1, detectedCircle2):
    dist1 = getDistance(detectedCircle1)
    print "distance to ball 1 is: " + str(dist1)
    dist2= getDistance(detectedCircle2)
    print "distance to ball 2 is: " + str(dist2)
    
    return (dist1, dist2) 
    
    """ w=2*detectedCircle[2]    
    x=math.log10(w)
    m=-551.68
    b=1263.4
    dist = m*x+b
    print "radious is " + str(w)
    print "distance to the ball is: " + str(dist)
    return dist"""
    
    """ w=2*detectedCircle[2]    
    y=(w/640)*100
    m=-0.0442
    b=22.533
    dist = (y - b)/m
    print "radious is " + str(w)
    print "distance to the ball is: " + str(dist)"""