"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    # <YOUR CODE HERE>
    intersection = 2 * np.sum( (a>0) * (b>0) ).astype(np.float32)
    volumes = (np.sum(a>0) + np.sum(b>0)).astype(np.float32)
    
    return  intersection / volumes  if volumes != 0 else -1

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    # <YOUR CODE GOES HERE>

    intersection = np.sum( (a > 0) * (b > 0) ).astype(np.float32)
    union = np.sum(a > 0) + np.sum(b > 0) - intersection
    
    return  intersection / union  if union != 0 else -1


def Sensitivity(a, b):
    """
    This will compute the Sensitivity for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume  (PRED)
        b {Numpy array} -- 3D array with second volume (REAL)

    Returns:
        float
        
    Formula: Sensitivity == TPR == TP / (TP + FN)
    
    Low Sensitivity = under segmentation
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")
        
    # Sens = TP/(TP+FN)
    tp = np.sum((b > 0)[ (a > 0) == (b > 0) ])
    fn = np.sum((b > 0)[ (a == 0) == (b > 0) ])

    return -1 if fn+tp == 0 else (tp)/(fn+tp)   


def Specificity(a, b):
    """
    This will compute the Specificity for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume (PRED)
        b {Numpy array} -- 3D array with the predicted volume (REAL)

    Returns:
        float
        
    Formula: Specificity == TNR == TN / (TN + FP)
    
    Low Specitivity = Over segmentation
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # Sens = TP/(TP+FN)
    tn = np.sum((b==0)[ (a == 0) == (b == 0) ])
    fp = np.sum((b==0)[ (a > 0) == (b == 0) ])

    return -1 if tn+fp == 0 else (tn)/(tn+fp)   