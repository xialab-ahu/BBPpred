# BBBPred
BBBPred uses machine learning to predict BBB. Users can run program with specified protein sequences.

![draft](https://github.com/loneMT/BBBPred/blob/master/codes/flow.jpg)


Figure 1. Framework of BBB peptides prediction using machine learning methods. The 1st stage is dataset preparation to form training dataset and independent dataset; The 2nd stage is feature encoding; The 3rd stage is to train and evaluate prediction models. The independent test is usually to validate the ability of a trained model. The 4th stage is to compare the model performance. The 5th is to construction our user friendly webserver for our BBB peptide prediction tool.

<br />

# Abstract

### Motivation:
Neurologic and psychiatric disorders account for a remarkable 28%of all years of life lived with a disability, and effective medicines for these diseases are in scarcity .The physical and enzymatic barrier called blood-brain barrier is the main bottleneck in the delivery of therapeutic drugs to the brain. Blood-brain barrier peptides (BBB peptides) have recently emerged as promising therapeutic agents which can cross the blood-brain barrier. Due to the avalanche of protein sequence data in the post-genomic era, there is an urgent need to develop automated computational methods to enable fast and accurate identification of novel BBB peptides within the vast number of candidate proteins and peptides. <br />

web-server is also available at  [http://bioinfo.ahu.edu.cn:8080/BBBpred/]

### Results:
In this work, we present BBBPred, a novel bioinformatics tool that allows users to rapidly and accurately identify the blood–brain barrier peptide. BBBPred was developed by using the most suitable machine learning models combined with optimized feature representations. We evaluated BBBPred based on well-prepared up-to-date benchmark and independent test datasets. The independent test proved that BBBPred have well prediction performance for BBB peptides prediction. In summary, our tool provides users with high-quality predicted blood-brain barrier peptides for hypothesis generation and biological validation. <br />
<br />




# Installation
* Install Python 3.5 in Linux and Windows.
* Because the program is written in Python 3.5, python 3.5 with the pip tool must be installed first. 
* BBBPred uses the following dependencies: numpy, pandas, collection, biopython and sklearn You can install these packages first, by the following commands:
```
pip install numpy
pip install biopython==1.73 
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


# Run BBBPred on a New Test File (Fasta file)

1- Protein sequences have to be saved in a fasta format similar to following format: <br />

   .>Seq1 <br />
   MPKFYCDYCDTYLTHDSPSVRKTHCSGRKHKENVKDYYQKWMEEQAQSLIDKTTAAFQQG <br />

where '>Seq1' represents the fasta id and the second line is the protein sequence. <br />

2- Download the model files by running the following command: <br />

git clone https://github.com/loneMT/BBBPred.git <br />

3- Run the following two commands after downloading the model files: <br />
* unzip download <br />
* rm download <br />

4- To test your protein sequences using Test.py run the following command: <br />

$ python Test.py <file.fasta> <br />

5- The output will be generated in the current working directory. The name of the output file is prediction_results.csv. <br />

   | Sequence ID | Prediction |
   |-------------|------------|
   | Seq1        |yes|
   
6- If you run on test.fasta that's uploaded on this github, you can compare the results with the Expected_Prediction_Result.csv that's also uploaded on this github. <br />


**Example:**

`python predict.py  ../codes/example.fasta ../codes/results.csv`

After entering predict.py, you will enter the data you need to predict and the csv file that stores the predicted results in turn.

**Example:**

`python predict.py test.fasta result.csv`

# Announcements

* In order to obtain the prediction results, please save the query protein sequences and protein name in fasta format. Users can refer to the example.fasta under the codes folder. Also of note, each protein name should be added by '>', otherwise the program will occur error.
* The accepted amino acids are: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y. If the protein fragments contain other amino acids, the program only will predict fragments which contain above-mentioned 20 amino acids.
* To save the prediction results, the result should be in csv format.


