import csv
import matplotlib.pyplot as plt

def main():

  a = input("paste file path (with file name) of the target data: ")
  b = input("paste file path for save location of new data: ")
  c = input("name for save of new data: ")
  d = int(input("threshold in % of error value: "))

  #data path, file save path, save file name, threshold for error correction

  file_path = a
  output_path = b
  name = c

  out_name = output_path+"\\"+name+".csv"

  # this part reads and extracts data

  with open(file_path, newline="") as file:
    x = []
    y = []

    with open(file_path, newline="") as file:
      rows = csv.reader(file)
      for row in rows:
        if row:
          x.append(float(row[0]))
          y.append(float(row[1]))
  cln_dat = clean(x, y, d)

  #this part writes the data to a new csv file

  with open(out_name, "w", newline="") as file:
    file.write("x,y\n")
    for x_value, y_value in zip(x, cln_dat):
      file.write(f"{x_value},{y_value}\n")

  plt.plot(x, cln_dat)
  plt.show()


def clean(x = [], y = [], threshold = 5):
  n_sety=y.copy()
  i=2
  while i!= len(x):
    slope = (n_sety[i-1]-n_sety[i-2])/(x[i-1]-x[i-2]) # takes slope of two previous points
    predict = n_sety[i-1] + slope * (x[i]-x[i-1]) # uses the slope from the previous lines to predict the next point
    error = abs(n_sety[i] - predict) / abs(predict) * 100 # calculates error of the actual point from the slope predicted point
    if error>=threshold:
      correction = predict - n_sety[i]
      for e in range(i, len(x)):
        n_sety[e] += correction # this fixes the data at and past the point that was detected as past the error threshold by measuring the value of how off the errored point was and adding that value to the following data
    i+=1
  return n_sety

if (__name__== "__main__"):
  main()