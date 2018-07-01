#!/usr/bin/python

#Checkpoint - 96.1% accuracy
#model_checkpoint_path: "model.ckpt-60000"
#all_model_checkpoint_paths: "model.ckpt-1"
#all_model_checkpoint_paths: "model.ckpt-60000"

import sys
import tensorflow as tf
import pandas as pd

#Hyperparameters
batch_size = 100
train_steps = 60000

args = sys.argv

MODEL_DIR = 'NA_model/'
TRAINING_FILE = args[1]
EVAL_FILE = args[2]

label_name = 'label'

#Number of columns
nc = 2 # {'N', 'A'}

#Training
def load_data(label_name=None):
    train_path = TRAINING_FILE
    train = pd.read_csv(filepath_or_buffer = train_path,
                                header=0)
    train_features, train_labels = train, train.pop(label_name)
    test_path = EVAL_FILE
    test = pd.read_csv(filepath_or_buffer = test_path,
                                header=0)
    test_features, test_labels= test, test.pop(label_name)
    return (train_features, test_features), (train_labels, test_labels)


(train_features , test_features), (train_labels, test_labels) = load_data(label_name)

fc = []
for key in train_features.keys():
    fc.append(tf.feature_column.numeric_column(key=key))

classifier = tf.estimator.LinearClassifier(
    n_classes=nc,
    feature_columns = fc
    ,model_dir=MODEL_DIR
)


def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(buffer_size=1000).repeat(count=None).batch(batch_size)
    return dataset

print("Training now...")

classifier.train(
    input_fn=lambda:train_input_fn(train_features, train_labels, batch_size)
    ,steps=train_steps
)


#Evaluating
print("Evaluating...")

def eval_input_fn(features, labels=None, batch_size=None):
    features = dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)
    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    assert batch_size is not None, "batch_size must have a value"
    dataset = dataset.batch(batch_size)
    return dataset.make_one_shot_iterator().get_next()

eval_result = classifier.evaluate(
    input_fn=lambda:eval_input_fn(test_features, test_labels, batch_size))

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))