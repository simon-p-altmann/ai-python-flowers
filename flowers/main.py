# Check the versions of libraries

# Python version 
# leaving this here for demo purposes only
# if you were getting this prod ready you would leave the imports to the seperate modules, and load only what was needed
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# add other modules to the path
sys.path.insert(0, 'D:/code/python/ai/flowers/dataset')
sys.path.insert(1, 'D:/code/python/ai/flowers/learning')
sys.path.insert(1, 'D:/code/python/ai/flowers/format')
# importing the hello
from pandasService import greeting,shape,read_csv,head,basicStat
from psykitLearnService import trainModels
from formatService import printBlankLines,printLineheading



printBlankLines(5)
greeting('timmy')

# Load libraries





...
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# creates a pandas dataset
dataset = read_csv(url, names=names)


# shape
#print(dataset.shape)
printLineheading('shape',2)
shape(dataset)
printLineheading('head',2)
head(dataset,10)
printLineheading('basicStat',2)
basicStat(dataset)
printLineheading('trainModels',2)
trainModels(dataset)



