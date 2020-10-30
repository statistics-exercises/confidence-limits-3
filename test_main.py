import unittest
import scipy.stats as st
import scipy.special as sp
from main import *

class UnitTests(unittest.TestCase) :
    def test_uniform_discrete(self) : 
        for a in range(1,4) :
            for b in range(6,8) : 
                mean = 0
                for i in range(10) : 
                    var = uniform_discrete(a,b)
                    self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your function uniform_discrete returns a number that is not an integer" )
                    self.assertTrue( var>=a and var<=b, "your function uniform_discrete returns a number that is outside the range of possible values")
                    mean = mean + var
                mean = mean / 10
                var = ( (b-a+1)*(b-a+1) - 1 ) / 12 
                bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                self.assertTrue( np.fabs( mean - 0.5*(b+a) )<bar, "your function uniform_discrete appears to be sampling from the wrong distribution" )
    
    def test_n_uniform_discrete(self) : 
        for n in range(2,4) : 
            for a in range(1,3) :
                for b in range(6,7) : 
                    mean = 0
                    for i in range(10) : 
                        var = n_uniform_discrete(n,a,b)
                        self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your function n_uniform_discrete returns a number that is not an integer" )
                        self.assertTrue( var>=n*a and var<=n*b, "your function n_uniform_discrete returns a number that is outside the range of possible values")
                        mean = mean + var
                    mean = mean / 10
                    var = n/12*( (b-a+1)*(b-a+1) - 1 )
                    bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean - n*0.5*(b+a) )<bar, "your function n_uniform_discrete appears to be sampling from the wrong distribution" )
      
      def test_mean(self) :
          for n in range(2,4) : 
             for a in range(1,3) :
                for b in range(6,7) :
                    mean = sample_mean( 10, n, a, b )
                    var = n/12*( (b-a+1)*(b-a+1) - 1 )
                    bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean - n*0.5*(b+a) )<bar, "Your function for generating the sampling the sample mean appears to be sampling from the wrong distribution" )
