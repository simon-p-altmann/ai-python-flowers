
from matplotlib import pyplot as plt
from pandas import read_csv
from pandas.plotting import scatter_matrix

def readDataFromCsv(url,columnHeaders):
  return read_csv(url, names=columnHeaders)

def greeting(name):
  print("Hello, " + name)

def shape(dataset):
  # shape
  print(dataset.shape)    

def head(dataset,number):
  # shape
  print(dataset.head(number))  

def basicStat(dataset):
  # descriptions
  print(dataset.describe())

def groupBy(dataset,groupByTitle):
  # descriptions
  print(dataset.groupby(groupByTitle).size())

def boxPlot(dataset,groupByTitle):
  dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
  plt.show()

def hist(dataset,groupByTitle):
  # histograms
  dataset.hist()
  plt.show()

def scatterMatrix(dataset,groupByTitle):
  # scatter plot matrix
  scatter_matrix(dataset)
  plt.show()




