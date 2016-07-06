#FitCompete - Run to compete with similar users

##Intoduction

[FitCompete] (www.fitcompete.club:5000) is an application which suggests similar users based on profile match. The main goal of the project is to 
find similar users in linear time complexity rather than using quadratic time complexity by comparing all possible pairs.
One solution for this is using hashing techniques. The existing hashing techniques like min-hashing and LSH work well for discerete 
features. My current problem has 9 features with continuous values for which the above hashing techniques don't
work well. I have implemented an algorithm which discretizes these feature based on their values into Low (L), Medium (M) and High (H) ranges 
by providing L or M or H tag for each feature. Thus, every user is tagged with a 9 letter string. All the users with similar tags 
are considered to be similar.

Also, when a user selects another user to compete with from the UI, a stream is generated for the two users with 1000 data points per second. This stream is processed in spark streaming to compute the average heart-rate and pace over a 3-seconds window. The average heart-rate is computed for a 3sec window in-order to smoothen the variations in the randomly generated values and the pace is computed by considering the total steps taken for the past 3 seconds and by considering a step to be approximately equal to 2.5 feet.   


##Technologies Used

- Kafka - As message queue for data ingestion into InfluxDB 
- InfluxDB - Timeseries database which computes daily aggregates for each user to get a summary of a user's performance 
- Spark - Similarity computation is done in batch mode and average heart-rate and pace calculation is done in streaming
- Redis - Key-value lookup for storing the computed similarity results and a message queue for the computed streaming average and pace 

##Pipeline

![Alt text](/pipeline.JPG?raw=true)

## Demo

Website [fitcompete.club] (www.fitcompete.club:5000)

Presentation [Fit Compete] (http://www.slideshare.net/NiharikaBollapragada)



