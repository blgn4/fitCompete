#FitCompete - Run to compete with similar users

##Intoduction

[FitCompete] (www.fitcompete.club:5000) is an application which suggests similar users based on profile match. The main goal of the project is to 
find similar users in linear time complexity rather than using quadratic time complexity by comparing all possible pairs.
One solution for this is using hashing techniques. The existing hashing techniques like miin-hashing and LSH work well for discerete 
features. My current problem has only 9 features with continuous values in certain ranges for which the above hashing techniques don't
work well. I have implemented an algorithm which discretizes these feature based on their values into Low (L), Medium (M) and High (H) ranges 
by providing L or M or H tag for each feature. Thus, every user is tagged with a 9 letter string. All the users with similar tags 
are considered to be similar.


##Technologies Used

- Kafka - As message queue for data ingestion into InfluxDB 
- InfluxDB - Timeseries database which computes daily aggregates for each user to get a summary of a user's performance 
- Spark - Similarity computation is done in batch mode and average heart-rate and pace calculation is done in streaming
- Redis - Key-value lookup for storing the computed similarity results and a message queue for the computed streaming average and pace 

##Pipeline

![Alt text](/pipeline.JPG?raw=true)



