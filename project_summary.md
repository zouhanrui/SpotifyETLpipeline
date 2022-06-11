 # SpotifyETLpipeline
Python ETL Data Pipeline with AWS, Terraform and Spotify

## Project goal:
1. Extract my spotify playlists weekly
2. Identify my latest favorite top artists
3. Extract their top albums and tracks
4. Load them to s3 partitioned by date(weekly) for personalized music taste trend analysis


> Tested Spotify public API in Postman and send http request to invoke api calls from Python: **sporifyAPI/**
 
#### Spotipy library
* Connected project in Spotify for Developers dashboard by SpotifyClientCredentials
* Extracted Json data from Spotify, processed data to the targeted results, and Loaded .csv file data into s3 bucket


### Terraform (Infrastructure as code)
* Built out a fully functional aws pipeline  
* **Terreform apply** deploys:
> Cloudwatch alarm: sending weekly event to trigger lambda function
> 
> Lambda function runs code to do the ETL job
> 
> Lambda and Cloudwatch IAM roles with corresponding the least privilege policies and permissions.
> 
> 
