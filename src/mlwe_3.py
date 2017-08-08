'''
Created on 06 ago 2017

@author: davide
'''

import compute_log_loss 

import numpy as np

def define():
    actual_labels = np.array([1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.])
    
    correct_confident_prediction = np.array([0.95,  0.95,  0.95,  0.95,  0.95,  0.05,  0.05,  0.05,  0.05,  0.05])
    correct_not_confident_prediction = np.array([ 0.65,  0.65,  0.65,  0.65,  0.65,  0.35,  0.35,  0.35,  0.35,  0.35])
    wrong_not_confident_prediction = np.array([ 0.35,  0.35,  0.35,  0.35,  0.35,  0.65,  0.65,  0.65,  0.65,  0.65])
    wrong_confident_prediction = np.array([ 0.05,  0.05,  0.05,  0.05,  0.05,  0.95,  0.95,  0.95,  0.95,  0.95])
    
    return actual_labels, correct_confident_prediction, correct_not_confident_prediction, wrong_not_confident_prediction, wrong_confident_prediction

actual_labels, correct_confident_prediction, correct_not_confident_prediction, wrong_not_confident_prediction, wrong_confident_prediction = define()

print('Actual labels: ' + str(actual_labels) + '.')
print()

correct_confident_prediction_logloss = compute_log_loss.compute_log_loss(correct_confident_prediction, actual_labels)
print('Correct, confident prediction: ' + str(correct_confident_prediction) + '.')
print('Log loss for correct, confident prediction: ' + str(correct_confident_prediction_logloss) + '.')

 # Compute and print log loss for 1st case
correct_confident = compute_log_loss.compute_log_loss(correct_confident_prediction, actual_labels)
print("Log loss, correct and confident: {}".format(correct_confident)) 

# Compute log loss for 2nd case
correct_not_confident = compute_log_loss.compute_log_loss(correct_not_confident_prediction, actual_labels)
print("Log loss, correct and not confident: {}".format(correct_not_confident)) 

# Compute and print log loss for 3rd case
wrong_not_confident = compute_log_loss.compute_log_loss(wrong_not_confident_prediction, actual_labels)
print("Log loss, wrong and not confident: {}".format(wrong_not_confident)) 

# Compute and print log loss for 4th case
wrong_confident = compute_log_loss.compute_log_loss(wrong_confident_prediction, actual_labels)
print("Log loss, wrong and confident: {}".format(wrong_confident)) 

# Compute and print log loss for actual labels
actual_labels = compute_log_loss.compute_log_loss(actual_labels, actual_labels)
print("Log loss, actual labels: {}".format(actual_labels)) 