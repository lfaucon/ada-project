# ADA - project
# Unsupervised extraction of students navigation patterns on an EPFL MOOC

## Group members

- Thibault Asselborn
- Victor Faramond
- Louis Faucon

## Abstract

How do students learn in MOOCs? Are there efficient and inefficient learning patterns? This project will aim at giving answers to these questions by analysing the activities of hundreds of thousands of students registered on EPFL Scala MOOC on Coursera. The task of modeling student's knowledge and learning has been broadly studied with several emerging fields such as Intelligent Tutors or BKT (Bayesian Knowledge Tracing). With the rapid growth of MOOCs, a lot of learning data has become available to scientists leading to extensive usage of machine learning in educational science (example: EDM-Educational Data Mining, LAS-Learning At Scale, etc.). 

This project focus on studying an EPFL MOOCs hosted on Coursera about Functionnal Programming with Scala. In particular, we are interested in what we call *learning patterns* which are the short sequences of activities that a student performs in order to learn. In the case of a MOOC, the learning activities usually are one of *Watching a Video*, *Reading or Posting on the Forum*, *Working on and Submitting Assignments*. We will use several machine learning techniques to gain insights on the students behaviour and produce a simple and efficient visualization tool in order to provide feedback to teachers to help them understand the potential difficulties encountered by their students during the course and (if necessary) adjust it accordingly.

## Content of the repository
- `poster`: Latex files and figures needed to generate the poster used during thepresentation

- `0-EXPLORATION`: Playing with the dataset, to understand the challenges and the opportunities.

- `1-PREPROCESSING`: Preprocessing of the data. From the csv files containing lists of Forum, Problem and Video events, creates dataset of json object of the format `{ 'StudentID': string, 'ProblemID': integer, 'NavigationPattern': list }`.  We implemented the preprocessing with Spark with the aim to being able to run our analysis on a cluster if need be, but 8 cores and 16G of ram appeared to be enough along all of our project.

- `2-FEATURE-ENGINEERING`: As sequences of events with each different types and features are not fit to be analysed by most data science tools and machine learning algorithms, we perform here a transformation of the navigation pattens into vectors of features. We realise the importance of this step for all the future results of the project.

- `3-COMPARISON-CHOICE-V-A` and `3-COMPARISON-V-A-M`: Analyses and compare students based on a simple supervised clustering of navigation patterns (Starting with a video event (V) or starting with an assignment event (A) or changing approach along time (M)). This work gave interesting statistics to understand students behavior, but we did not include it in our final report

- `3-GRADE-PREDICTION`: Failed attempt at using machine learning techniques for predicting students grades at assignments. We did not investigate this option in depth

- `3-NAVIGATION-SANKEY`: Producing sankey diagrams to show the navigation of all the students on a specific assignment

- `3-UNSUPERVISED-CLUSTERING`: Uses K-means and PCA on the vectors of features of navigation patterns to extract the mains trends and differences between these patterns. K-means gives us three gruops of students that we interpret as being typical students, struggling students and certificate seeker. PCA gives us three axes corresponding to the previous knowledge, the learning gain and the procrastination of students. Finally we draw a sankey diagram to show the changes in navigation pattern types of students along the MOOC.

- `utils.py`: Some methods used by the notebooks, externalised for cleanliness of the code.

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
- Extensive analysis of the learning patterns, measures of correlations between pattern used and grade improvement and report of the results of our machine learning techniques.

## Timeplan

- **October**:
Getting the Scala MOOC data from EPFL lab CHILI and starting to explore it using Pandas and Spark in an IPython notebook.
- **November**:
Handling the data: cleaning, parsing, transforming and extracting. Producing basic aggregations measures and visualisations to give us insights on the learning patterns
- **December**:
Apply more complex Machine Learning models (Clustering, Prediction of Learning gain from the learning pattern). Define the structure of the visualisation to represents students and learning patterns (As a tree? As a Flow?)
- **January**:
Finalizing results and writing report
