import numpy as np

def uniform_discrete(a,b) :
  # Your code to generate the uniform discrete random variable goes here
  
  
def n_uniform_discrete( n, a, b ) : 
  # You code to generate the sum of n uniform discrete random variables goes here
  
def sample_mean( m, n, a, b ) : 
  # Your code to calculate the mean of m sums of n uniform discrete random variables
  # goes here


# This outputs the average values you do four separate experiments in which you roll two fair dice 100 times.
print( sample_mean(100,2,1,6), sample_mean(100,2,1,6), sample_mean(100,2,1,6), sample_mean(100,2,1,6) )
