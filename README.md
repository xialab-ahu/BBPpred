# BBBPred
BBBPred uses machine learning to predict BBB. Users can run program with specified protein sequences.
# Installation
* Install Python 3.5 in Linux and Windows.
* Because the program is written in Python 3.5, python 3.5 with the pip tool must be installed first. 
* BBBPred uses the following dependencies: numpy, pandas, collection, biopython and sklearn You can install these packages first, by the following commands:
```
pip install numpy
pip install biopython ==1.73 
pip install sklearn
```

* If you have run above commands in Linux for the first time, you can run the following command:
```
sudo apt install python3-pip
```
* After that, users can change the commands into:
```
pip install numpy
pip install biopython ==1.73 
pip install sklearn
```

# Running BBBPred
open cmd in Windows or terminal in Linux, then cd to the BBBPred-master/codes folder which contains predict.py 

To predict general BBB using our model, run: 

`python predict.py [custom predicting data in fasta format]  [ predicting results in csv format]`

**Example:**

`python predict.py  ../codes/example.fasta ../codes/results.csv`

After entering predict.py, you will enter the data you need to predict and the csv file that stores the predicted results in turn.

**Example:**
`python predict.py test.fasta result.csv`

# Announcements

* In order to obtain the prediction results, please save the query protein sequences and protein name in fasta format. Users can refer to the example.fasta under the codes folder. Also of note, each protein name should be added by '>', otherwise the program will occur error.
* The accepted amino acids are: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y. If the protein fragments contain other amino acids, the program only will predict fragments which contain above-mentioned 20 amino acids.
* To save the prediction results, the result should be in csv format.


