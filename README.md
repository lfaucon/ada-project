# ada-project
# Extraction of learning patterns of students in MOOCs

## Group members

- Thibault Asselborn
- Victor Faramond
- Louis Faucon

## Abstract

How do students learn in MOOCs? Are there efficient and inefficient learning patterns? This project will aim at giving answers to these question by analysing the activities of hundreds of thousends of students on EPFL Scala MOOC on Cousera. 

## Data description

The data is divided in 56 csv files corresponding to 7 different datasets for 8 sessions of EPFL Scala MOOC. Each session has about 50 thousends of students and several millions of events. 

The sessions names are:
- progfun-002,
- progfun-003,
- progfun-004,
- progfun-005,
- progfun-2012-001,
- progfun1,
- progfun2,
- progfun2-002

For each session the available datasets are:
- `User_Grades`: a table containing one line per student of the session and there final average grade.
- `User_Hash_Mapping`: mapping between the fields `UserSessionID` and `UserAccountID`, which differentiates between the students ID for the session of the MOOC and the general Coursera user ID.
- `Forum_Info`: Meta data about the forum
- `Video_Info`: Meta data about the lecture videos
- `Problem_Events_With_Info`: Time series of events concerning the assignments
- `Video_Events`: Time series of events concerning the videos
- `Forum_Events`: Time series of events concerning the forum

## Challenging aspects 

- **Visualizations**:
The data we are working with would need to be visualized in a simple, because the insights provided will benefit educators who would not be able to un

- **Big data**:
The dataset at hand is of approximately 9G (raw csv files, it will be less after cleaning and extracting meaningfull items). Even if it is not *HUGE*, it makes it quite slow to handle on a single laptop (In particular it is bigger than the RAM memory). That is why we plan to implement our analysis with Spark to be able to run it on a distributed cluster later on. At first we will develop our algorithm by testing in locally on a subset of our data, then use the cluster to apply our analysis to the whole dataset. 

## Expected results 

- Simple and clear visualization of students learning pattern and their efficiency
- Extensive analysis of the learning patterns and measure of correlations between pattern used and grade improvement in assignments

## Timeplan

- **October**: 
Getting the Scala MOOC data from EPFL lab CHILI and starting to explore it using Pandas and Spark in an IPython notebooks.
- **November**: 
Handling the data: cleaning, parsing, transforming and extracting. Producing basic aggregations measures and visualisations to give us insights on the learning patterns
- **December**:
Apply more complex Machine Learning (Clustering, Prediction of Learning gain from the learning pattern). Define the structure of the visualisation to represents students and learning patterns (As a tree? As a Flow?)
- **January**: 
Finalizing results and writing report
- ...








