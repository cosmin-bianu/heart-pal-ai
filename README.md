# Heart Pal - Artificial Intelligence

This is the Heart Pal AI module. It is the core part of the project since it is used to detect several types of abnormal heart rhythm. 

 DISCLAIMER: The code has NOT been tested on an actual test subject. It has been tested only in virtual environments with real world prerecorded data from the PhyisioNet Database, which has data recorded in controlled environments with minimal phyiscal disturbance. It has not been tested on an actual patient live and as a result we do not know how it performs with the mentioned "phyisical disturbance".



## Getting started

First of all, we STRONGLY suggest that you do some research on ECG's and how to read them. Sparkfun has some detailed and easy to understand resources on their page about [ECGs](https://learn.sparkfun.com/tutorials/ad8232-heart-rate-monitor-hookup-guide?_ga=2.240534727.572863605.1518885884-1726391607.1518537906).

It uses the TensorFlow's predefined models and a different file with a different trained model for each heart problem detectable at the moment. 
As it is stated in the disclaimer (if you haven't read it, we strongly advise you to do so), the models were trained using data from the [PhysioBank Database](https://www.physionet.org/physiobank/). The MIT-BIH Arrhythmia Database (mitdb) to be precise. The naming scheme follows the one from the [PhysioBank Annotation guide](https://www.physionet.org/physiobank/annotations.shtml). So:

A = Atrial premature beat

V = Premature ventricular contraction

Following this rule the files will be named with the prefix 'N' followed by the letter corresponding to the problem it assesses. For example, NA_model is the folder which houses the model for the 'atrial premature beat detection' AI.



The models used for each file ar as follows:

NA - Linear Regression

NV - Deep Neural Network

Now inputs and outputs:

NA: It takes in one number which is the 'delta R-R'. For those that do not know, in short, it is the time between two beats and spits out N for normal or A if it is abnormal.

NV: It takes a waveform centered around every QRS complex with 0.4s padding in each side of the R point (so each is 0.8). The frequency has also been scaled down from 360Hz to 65Hz for performance purposes. It spits out N for normal and V for abnormal.

Training and evaluation is done through CSV files, detailed in the 'CSV Structure' section.

## Prerequisites

You need to have Python 2.7 installed. This will work with Python 3 but will require some code tinkering since the one distribuited here is designed for the former. 
Then, you need to install TensorFlow.

Just open the terminal and type the following command
```
pip install tensorflow
```
Wait for the installation to finish. It will take a while. You can find the full TensorFlow install and troubleshooting guide [here](https://www.tensorflow.org/install/).

Next you will have to install the pandas package for reading the CSV files.
```
pip install pandas
```
Now you are all set! If you encounter any problems please do not hesitate to contact us.
## Usage

Execution is designed for automated scripts. You will have to pass the test and evaluation files as arguments when running the training script.

The first argument is the CSV file with the training data.
The second argument is the CSV file with the evaluation data.

ORDER IS IMPORTANT!

An example for running the NA training and evaluating script.
```
sudo python NA_te.py NA_data/A.csv NA_data/A_EVAL.csv
```
This will take A.csv as training and A_EVAL.csv as evaluation.

The output should look something like this:

```
Training now...
Evaluating...

Test set accuracy: 0.961
```


## CSV Structure
```
NA: 2 Columns 
1st column: delta time
2nd column: label (which can be either 'N' or 'A')
```

```
NV: 7 Columns
1-6 columns: waveform data
7th column: label (which can be either 'N' or 'V')
```

## Running the tests

If you want to run just the evaluation, comment out the training part from the scripts. 


## Deployment

We haven't published any scripts for prediction since different use cases need different scripts.

Our approach was to run the scripts as services and read data from a buffer file that was updated every five seconds. If the models noticed any anomalies then they would send a signal to the Android device and also record the event locally.

## Contributing

This section will be updated soon.

## Versioning

This section will be updated soon. 

## Authors

This project is made possible by the 'I.L. Caragiale' National College, Bucharest.

Project Leader: Florea Andrei

Cardiology specialist: Dr. Bucşă Adrian, Fundeni Hospital Bucharest

Lead Programmer: Bianu Cosmin

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [PhyioNet](http://physionet.org)
