#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Financial Concepts in Python

# The following shows how Python can be used to calculate financial concepts and make it more efficient to do calculations

# ### Growth and Rate of Return
# 
# Growth and Rate of Return are two concepts that are ubiquitous throughout the financial world. Recall that the cumulative returns from investing $100 in an asset that grows at 5% per year, over a 2 year period can be calculated as:
# 
# 100∗(1+0.05)**2
# 
# Ex:
# 1. Calculate the future value (cumulative return) of a $100 investment which grows at a rate of 6% per year for 30 years in a row and assign it to future_value.

# In[1]:


# Calculate the future value of the investment and print it out
future_value = 100* (1+0.06)**30
print("Future Value of Investment: " + str(round(future_value, 2)))


# This can compare to how someone could do it in excel by having cells that store each variable. As long as the variables and equations are correct, the calculation should yield the same result without error

# ### Compound Interest
# 
# 
# 
# Another important variable is the number of compounding periods, which can greatly affect compounded returns over time.
# I stored the values into different variables to keep it clean and ensure that others will understand what I did and can modify easily
# 

# In[3]:


# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))


# In[3]:


# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))

# Calculate the value for the investment compounded quarterly
compound_periods_2 = 4
investment_2 = initial_investment*(1 + growth_rate / compound_periods_2)**(compound_periods_2*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))
print("Investment 2: " + str(round(investment_2, 2)))


# In[4]:


# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment*(1+growth_rate)**growth_periods
print("Future value: " + str(round(future_value, 2)))

# Calculate the discount factor
discount_factor = 1/((1 + growth_rate)**(growth_periods))
print("Discount factor: " + str(round(discount_factor, 2)))

# Derive the initial value of the investment
initial_investment_again = future_value*discount_factor
print("Initial value: " + str(round(initial_investment_again, 2)))


# ### Present Value
# 
# One way that make python really efficient and easy to use is the packages. In this case, using numpy's built in libraries can help making it easy to do various computations. The .pv(rate, nper, pmt, fv) function, for example, allows you to calculate the present value of an investment as before with a few simple parameters:
# 
# rate: The rate of return of the investment
# nper: The lifespan of the investment
# pmt: The (fixed) payment at the beginning or end of each period (which is 0 in our example)
# fv: The future value of the investment
# You can use this formula in many ways. For example, you can calculate the present value of future investments in today's dollars.
# 
# - Instructions:
# 1. Import numpy as np.
# 
# 2. Using Numpy's .pv() function, compute the present value of an investment which will yield $10,000 15 years from now at an inflation rate of 3% per year and assign it to investment_1.
# 
# 3. Compute the present value of the same investment, but with a time horizon of only 10 years and an inflation rate of 5%, assigning it to investment_2.
# 
# The key is ensuring a basic understanding with using numpy and importing the packages needed.
# 

# In[5]:


get_ipython().system('pip install numpy_financial')


# In[6]:


# Calculating the exercise  with Numpy Financial
import numpy as np
import numpy_financial as npf
# Calculate investment_1
investment_1 = npf.pv(rate=.03, nper=15, pmt=0, fv=10000)

# Note that the present value returned is negative, so we multiply the result by -1
print("Investment 1 is worth " + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.pv(rate=.05, nper=10, pmt=0, fv=10000)
print("Investment 2 is worth " + str(round(-investment_2, 2)) + " in today's dollars")


# ### Future Value
# 
# The numpy module also contains a similar function, .fv(rate, nper, pmt, pv), which allows you to calculate the future value of an investment as before with a few simple parameters:
# 
# rate: The rate of return of the investment
# nper: The lifespan of the investment
# pmt: The (fixed) payment at the beginning or end of each period (which is 0 in our example)
# pv: The present value of the investment
# It is important to note that in this function call, you must pass a negative value into the pv parameter if it represents a negative cash flow (cash going out). In other words, if you were to compute the future value of an investment, requiring an up-front cash payment, you would need to pass a negative value to the pv parameter in the .fv() function.

# - Instructions :
# 
# 1. Using Numpy's .fv() function, calculate the future value of a $10,000 investment returning 5% per year for 15 years and assign it to investment_1.
# 
# 2. Calculate the future value of a $10,000 investment returning 8% per year for 15 years and assign it to investment_2.

# In[7]:


# Calculate investment_1
investment_1 = npf.fv(rate=.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = npf.fv(rate=.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")


# ### Adjusting Future Values for Inflation
# 
# You can now put together what you learned in the previous exercises by following a simple methodology:
# 
# First, forecast the future value of an investment given a rate of return
# Second, discount the future value of the investment by a projected inflation rate
# The methodology above will use both the .fv() and .pv() functions to arrive at the projected value of a given investment in today's dollars, adjusted for inflation.
# 
# - Instructions:
# 
# 1. Calculate the future value of a $10,000 investment returning 8% per year for 10 years using .fv() and assign it to investment_1.
# 
# 2. Calculate the inflation-adjusted present value of investment_1, using an inflation rate of 3% per year and assign it to investment_1_discounted.

# In[8]:


# Calculate investment_1
investment_1 = npf.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = npf.pv(rate=0.03, nper=10, pmt=0, fv=investment_1)
print("After adjusting for inflation, investment 1 is worth $" + str(round(-investment_1_discounted, 2)) + " in today's dollars")


# ### Discounting Cash Flows
# 
# You can use numpy's net present value function numpy.npv(rate, values) to calculate the net present value of a series of cash flows. You can create these cash flows by using a numpy.array([...]) of values.
# 
# 

# In[9]:



# Predefined array of cash flows
cash_flows = np.array([100, 100, 100, 100, 100])

# Calculate investment_1
investment_1 = npf.npv(rate=.03, values=cash_flows)
print("Investment 1's net present value is $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.npv(rate=.05, values=cash_flows)
print("Investment 2's net present value is $" + str(round(investment_2, 2)) + " in today's dollars")


# ### Initial Project Costs
# 
# The numpy.npv(rate, values) function is very powerful because it allows you to pass in both positive and negative values.
# 
# - Instructions:
# 1. Create a numpy array of the cash flow values for project 1, assigning it to cash_flows_1, and then do the same for project 2, assigning the values to cash_flows_2.
# 
# 2. Calculate the net present value of both projects 1 and 2 assuming a 3% inflation rate.
# 

# In[10]:


# Create an array of cash flows for project 1
cash_flows_1 = np.array([-250, 100, 200, 300, 400])

# Create an array of cash flows for project 2
cash_flows_2 = np.array([-250, 300, -250, 300, 300])


# Calculate the net present value of project 1
investment_1 = npf.npv(rate=0.03, values=cash_flows_1)

print("The net present value of Investment 1 is worth $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate the net present value of project 2
investment_2 = npf.npv(rate=0.03, values=cash_flows_2)
print("The net present value of Investment 2 is worth $" + str(round(investment_2, 2)) + " in today's dollars")


# ### Diminishing Cash Flows
# 
# Remember how compounded returns grow rapidly over time? Well, it works in the reverse, too. Compounded discount factors over time will quickly shrink a number towards zero.
# 

# In[11]:


# Calculate investment_1
investment_1 = npf.pv(rate=.03, nper=30, pmt=0, fv=100)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.pv(rate=.03, nper=50, pmt=0, fv=100)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")


# The comments and steps serve as guidelines so that even beginners who doesn't have financial knowlege can pick up the reason behind the computation. The only thing is that for simple tasks like this, a more seasoned financial practioner who have been used to using excel can do the same calculations without error. For beginners, it may be more difficult to pick up python rather than excel. Hence, leading to corporates preferring to use excel rather than python
