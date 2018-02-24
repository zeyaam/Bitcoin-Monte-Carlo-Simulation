# Bitcoin Monte Carlo Simulation

The following python program uses Bitcoin price data from 9/2011 to 11/2017. 

##Dicslaimer

*The daily returns on Bitcoin **closely** follow a normal distribution. The excel file and the python program both use inverse cumulative normal distribution function for the Brownian motion component. Because of this, the simulation should not be taken seriously as I did not compute my own distribution function based on available data and went for the closest match* 

The data was manually downloaded from Quandl (https://www.quandl.com/collections/markets/bitcoin-data) as a csv file.
