# Patient Selection for Diabetes Drug Testing

<img src="https://raw.githubusercontent.com/verbeemen/Udacity-AI-for-Healthcare/main/Proj_3_-_Patient_Selection_for_Diabetes_Drug_Testing/ai-and-work.jpg" alt="image to cheer things up"/>

## Context
EHR _(electronic health record)_ data is becoming a key source of real-world evidence (RWE) for the pharmaceutical industry and regulators to make decisions on clinical trials. You are a data scientist for an exciting unicorn healthcare startup that has created a groundbreaking diabetes drug that is ready for clinical trial testing. It is a very unique and sensitive drug that requires administering the drug over at least 5-7 days of time in the hospital with frequent monitoring/testing and patient medication adherence training with a mobile application. You have been provided a patient dataset from a client partner and are tasked with building a predictive model that can identify which type of patients the company should focus their efforts testing this drug on. Target patients are people that are likely to be in the hospital for this duration of time and will not incur significant additional costs for administering this drug to the patient and monitoring.

In order to achieve your goal you must <b>build a regression model that can predict the estimated hospitalization time for a patient</b> and use this to select/filter patients for your study.

Expected Hospitalization Time Regression Model: Utilizing a synthetic dataset(denormalized at the line level augmentation) built off of the UCI Diabetes readmission dataset, students will build a regression model that predicts the expected days of hospitalization time and then convert this to a binary prediction of whether to include or exclude that patient from the clinical trial.

This project will demonstrate the importance of building the right data representation at the encounter level, with appropriate filtering and preprocessing/feature engineering of key medical code sets. This project will also require students to analyze and interpret their model for biases across key demographic groups.

# Dataset
Due to healthcare PHI regulations (HIPAA, HITECH), there are limited number of publicly available datasets and some datasets require training and approval. So, for the purpose of this exercise, we are using a dataset from UC Irvine that has been modified for this course. Please note that it is limited in its representation of some key features such as diagnosis codes which are usually an unordered list in 835s/837s (the HL7 standard interchange formats used for claims and remits).


# The notebook (More user friendly)
- [student_project.ipynb](https://nbviewer.jupyter.org/github/verbeemen/Udacity-AI-for-Healthcare/blob/main/Proj_3_-_Patient_Selection_for_Diabetes_Drug_Testing/student_project.ipynb)
