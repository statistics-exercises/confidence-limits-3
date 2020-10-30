# (revision) The sample mean of dice rolls

The previous exercise demonstrated how you can create a more complicated random variable by combining easier to generate random variables.  In that exercise, the simple random variable was a uniform discrete random variable that was greater than or equal to a and less than or equal to b.  The more complex random variable was then a sum of these simpler random variables.  We can make this even more complicated by calculating a sample mean from m samples of these sums of n uniform discrete random variables.  In other words, we can generate a random variable as:

![](https://render.githubusercontent.com/render/math?math=\overline{Y}=\frac{1}{m}\sum_{i=1}^{m}\sum_{j=1}^{n}X_{ij})

In this expression, each of the ![](https://render.githubusercontent.com/render/math?math=X_{ij}) is a uniform discrete random variable that lies between a and b.  An expression similar to this one would be used to calculate the average value that we get when we roll n fair dice m times.

__Your task is to write a code to sample random variables using the expression above.__  To complete this task you will need to write three functions:

1. `uniform_discrete` - takes two arguments `a` and `b` in input.  It should return a uniform discrete random variable that is greater than or equal to `a` and less than or equal to `b`.
2. `n_uniform_discrete` - takes three arguments `n`, `a` and `b`.  It should return the sum of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  Notice that you can call `uniform_discrete` in this function.
3. sample_mean - takes four arguments in input `m`, `n`, `a` and `b`.  It should generate `m` sums of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  It then should calculate a sample mean from these `m` random variables.  In other words, this function should return a random variable that is generated using the formula on this page.  Please note that you may want to include calls to `n_uniform_discrete` in this function.

Once you have completed these three functions and run the code four values for the average value obtained when you roll 2 dice 100 times will be output.

