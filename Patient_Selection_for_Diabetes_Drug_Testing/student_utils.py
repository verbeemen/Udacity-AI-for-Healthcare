import pandas as pd
import numpy as np
import os
import tensorflow as tf
import functools

####### STUDENTS FILL THIS OUT ######
#Question 3
def reduce_dimension_ndc(df, ndc_df):
    '''
    df: pandas dataframe, input dataset
    ndc_df: pandas dataframe, drug code dataset used for mapping in generic names
    return:
        df: pandas dataframe, output dataframe with joined generic drug name
    '''
    
    return pd.merge(df, ndc_df[['NDC_Code','Proprietary Name']].rename({'NDC_Code':'ndc_code',
                                                                        'Proprietary Name': 'generic_drug_name'},axis=1), 
               on='ndc_code', 
               how='left').drop('ndc_code',axis=1)

#Question 4
def select_first_encounter(df):
    '''
    df: pandas dataframe, dataframe with all encounters
    return:
        - first_encounter_df: pandas dataframe, dataframe with only the first encounter for a given patient
    '''
    return df.sort_values('encounter_id').drop_duplicates(subset=["patient_nbr"], keep='first').reset_index(drop=True)


#Question 6
def patient_dataset_splitter(df, patient_key='patient_nbr'):
    '''
    df: pandas dataframe, input dataset that will be split
    patient_key: string, column that is the patient id

    return:
     - train: pandas dataframe,
     - validation: pandas dataframe,
     - test: pandas dataframe,
    '''
    # shuffle the data
    df = df.sample(frac=1)
    
    # add a simple id for each patient
    # (in theory you can also use the patient_nbr ... and you can also assume that their ids are random)
    df['temp_id'] = df.groupby([patient_key], sort=False).ngroup().add(1)
    
    # calculate the modulp of the temp_id
    df['temp_modulo_id'] = df['temp_id'] % 10

    # simply select the percentage
    train = df[ df['temp_modulo_id'] < 6 ] # 60%
    validation = df[ (df['temp_modulo_id'] == 6) | (df['temp_modulo_id'] == 7) ] # 20%
    test = df[ df['temp_modulo_id'] >=8 ] # 20%
    
    # return without the last 2 columns
    return train.iloc[:,:-2], validation.iloc[:,:-2], test.iloc[:,:-2]

#Question 7

def create_tf_categorical_feature_cols(categorical_col_list, vocab_dir='./diabetes_vocab/'):
    '''
    categorical_col_list: list, categorical field list that will be transformed with TF feature column
    vocab_dir: string, the path where the vocabulary text files are located
    return:
        output_tf_list: list of TF feature columns
    '''
    
    # key
    ## A unique string identifying the input feature.
    ## It is used as the column name and the dictionary key for feature parsing configs,
    ## feature Tensor objects, and feature columns.
    
    # vocabulary_file
    ## The vocabulary file name.
    
    
    # default_value
    ## The integer ID value to return for out-of-vocabulary feature values,
    ## defaults to -1. This can not be specified with a positive num_oov_buckets.
    
    # num_oov_buckets
    ## Non-negative integer, the number of out-of-vocabulary buckets. 
    ## All out-of-vocabulary inputs will be assigned IDs in the range 
    ## [vocabulary_size, vocabulary_size+num_oov_buckets) based on a hash of the input value.
    ## A positive num_oov_buckets can not be specified with default_value.
    
    output_tf_list = []
    for c in categorical_col_list:
        vocab_file_path = os.path.join(vocab_dir,  c + "_vocab.txt")
        '''
        Which TF function allows you to read from a text file and create a categorical feature
        You can use a pattern like this below...
        tf_categorical_feature_column = tf.feature_column.......

        '''
        tf_categorical_feature_column = tf.feature_column\
                                          .categorical_column_with_vocabulary_file(key=c, 
                                                                                   vocabulary_file = vocab_file_path, 
                                                                                   default_value=0) 
                                                                                   # assign that the first value in the text file
                                                                                   # is the default out of vocabulary value
        
        output_tf_list.append( tf.feature_column.indicator_column(tf_categorical_feature_column) )
    return output_tf_list

#Question 8
def normalize_numeric_with_zscore(col, mean, std):
    '''
    This function can be used in conjunction with the tf feature column for normalization
    '''
    return (col - mean)/std



def create_tf_numeric_feature(col, MEAN, STD, default_value=0):
    '''
    col: string, input numerical column name
    MEAN: the mean for the column in the training data
    STD: the standard deviation for the column in the training data
    default_value: the value that will be used for imputing the field

    return:
        tf_numeric_feature: tf feature column representation of the input field
    '''
    normalizer = functools.partial(normalize_numeric_with_zscore, mean=MEAN, std=STD)
    return tf.feature_column.numeric_column( col, 
                                             default_value = default_value, 
                                             normalizer_fn = normalizer,
                                             dtype=tf.float64)

#Question 9
def get_mean_std_from_preds(diabetes_yhat):
    '''
    diabetes_yhat: TF Probability prediction object
    '''
    m = diabetes_yhat.mean()
    s = diabetes_yhat.stddev()
    return m, s

# Question 10
def get_student_binary_prediction(df, col):
    '''
    df: pandas dataframe prediction output dataframe
    col: str,  probability mean prediction field
    return:
        student_binary_prediction: pandas dataframe converting input to flattened numpy array and binary labels
    '''
    return (df[col] >= 5).astype(np.int32).values
