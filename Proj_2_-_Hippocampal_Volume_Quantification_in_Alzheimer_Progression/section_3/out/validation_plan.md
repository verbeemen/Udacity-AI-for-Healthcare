# Validation plan
---
# What is the intended use of the product?
- The intended use of this algorithm is to support and assist radiologists with the identification of hippocampal volume, posterior and anterior.

# How was the training data collected?
*We are using the "Hippocampus" dataset from the Medical Decathlon competition. This dataset is stored as a collection of NIFTI files, with one file per volume, and one file per corresponding segmentation mask. The original images here are T2 MRI scans of the full brain. As noted, in this dataset we are using cropped volumes where only the region around the hippocampus has been cut out. This makes the size of our dataset quite a bit smaller, our machine learning problem a bit simpler and allows us to have reasonable training times.*

- The dataset is available via: [http://medicaldecathlon.com](http://medicaldecathlon.com)
- The dataset is collected from the "Hippocampus" dataset from the Medical Decathlon competition
- The dataset consists of 263 training images and 131 testing images.

# How did you label your training data?
- Silver Standard
- All data has been labeled and verified by experts (Radiologists).

# How was the training performance of the algorithm measured and how is the real-world performance going to be estimated?
- The performance of the model was measured on a test set. This test set contained 10% of the entire dataset and was only used once.
- The measurements which we have used on the test set are:
	- Jacard distance
    - Dice scores
    - Sensitivity
    - Specificity


- Real world performances of the algorithm can be evaluated by:
    - New independent datasets
    - Evaluated by radiologists

# What data will the algorithm perform well in the real world and what data it might not perform well on?
- [x] The algorithm performs well on images of human brains with a clear view of the hippocambus.
         (SeriesDescription = "HippoCrop")
    *Random Sample*:
    - "filename": "hippocampus_383.nii.gz",
    - "dice": 0.9083910700538876,
    - "jaccard": 0.8321579689703809,
    - "sensitivity": 0.8625730994152047,
    - "specificity": 0.9990512189938368
      
- [ ] We didn't have any information about the patients. (Age, Gender, Conditions, ...)  
         this might have a impact on the performance