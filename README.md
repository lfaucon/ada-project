# ada-project
# Extraction of learning patterns of students in MOOCs

## Group members

- Thibault Asselborn
- Victor Faramond
- Louis Faucon

## Abstract

How do students learn in MOOCs? Are there efficient and inefficient learning patterns? This project will aim at giving answers to these questions by analysing the activities of hundreds of thousands of students registered on EPFL Scala MOOC on Coursera. A simple and efficient visualization tool will be developped to provide usefull feedback to teachers in order to let them understand potential difficulties encountered by students during learning and (if necessary) adjusting the course accordingly. 

## Data description

The data is divided in 56 `csv` files corresponding to 7 different datasets for 8 sessions of EPFL Scala MOOC. Each session has about 50 thousands of students and several millions of events.

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
- `User_Grades`: a table containing one line per student of the session and their final average grade.
- `User_Hash_Mapping`: mapping between the fields `UserSessionID` and `UserAccountID`, which differentiates between the students ID for the session of the MOOC and the general Coursera user ID.
- `Forum_Info`: Metadata about the forum.
- `Video_Info`: Metadata about the lecture videos.
- `Problem_Events_With_Info`: Time series of events concerning the assignments.
- `Video_Events`: Time series of events concerning the videos.
- `Forum_Events`: Time series of events concerning the forum.

## Challenging aspects

- **Visualizations**:
All the usefull informations extracted that may be of potential interest for educators would need to be visualized in a simple and efficient way. The goal will be to give to educators a feedback on their courses that they would not have been able to have without this work.

- **Big data**:
The size of the dataset is of approximately 9GB (raw `csv` files) for the moment (it will be less after cleaning and extracting meaningful items). Even if it is not *HUGE*, it makes it quite slow to handle on a single laptop (in particular it is bigger than the RAM of our personal computers). We therefore plan to implement our analysis with Spark to be able to run it on a distributed cluster later on. At first, we will develop our algorithm by testing it locally on a subset of our data, then use the cluster to apply our analysis to the whole dataset.

- **Machine Learning**:
We are willing to try out a variety of machine learning techniques for this project. We identify four use cases:
    * **unsupervised clustering** with techniques such as the K-means algorithm to cluster the learning patterns in a few meaningful category giving us better insight than the list of patterns
    * **collaborative filtering** to measure if some learning patterns would be efficient for a particular group of students but not other students and if we are able to build a pattern recommendation engine.
    * **linear or logistic regressions** to predict students learning gain or students results from their behaviour and other features to be determined.
    * **maximum likelihood estimation** to fit models of students knowledge and probabilities of learning for each possible activity, following the principles of Bayesian Knowledge Tracing.

## Expected results

- Simple and clear visualization of students learning pattern and their efficiency.
- Extensive analysis of the learning patterns and measures of correlations between pattern used and grade improvement in assignments.

## Timeplan

- **October**:
Getting the Scala MOOC data from EPFL lab CHILI and starting to explore it using Pandas and Spark in an IPython notebook.
- **November**:
Handling the data: cleaning, parsing, transforming and extracting. Producing basic aggregations measures and visualisations to give us insights on the learning patterns
- **December**:
Apply more complex Machine Learning models (Clustering, Prediction of Learning gain from the learning pattern). Define the structure of the visualisation to represents students and learning patterns (As a tree? As a Flow?)
- **January**:
Finalizing results and writing report
- ...
