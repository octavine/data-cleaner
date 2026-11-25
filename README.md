# data-cleaner
This project came about because I was working on a chemistry lab about initial rates where we mixed a solid and an acid in a flask and used a gas pressure sensor to measure the pressure of CO2 created in the beaker, the gas pressure sensor was in the form of a stopper that went in the top of the beaker, the only issue was that it would pop out because of the pressure when not held securely enough, this was not an issue because we only had to use a small beginning portion of the data but I still wanted to expirement with correcting the flawed data and so I created this algorithm to fix it.

# What the algorithm does internally

It reads a csv file of data with two columns x and y
it runs a loop where it measures the slope between two points and predicts the next
If the actual next point is off by more than a threshold value the following data is corrected by adding the difference of the actual point from the expected
it then returns the corrected data set in a csv format and displays it with mat plot lib

# how do you use it
 - run the file
 - paste the address of your csv file                         ex. C:\Users\User\Downloads\data.csv
 - paste the location of where you want the file to be saved  ex. C:\Users\User\Downloads
 - then name the new data                                     ex. new_data
 - finally input the error threshold value                    ex. 5

# Example
This shows the example file cleaned with an error threshold of about 5% 

![uncleaned data](Screenshot 2026-11-24 010415.png)
![cleaned data](Screenshot 2026-11-24 010620.png)
