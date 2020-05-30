import requests
import csv
import boto3
from datetime import date
from airflow.exceptions import AirflowException

''' Flattens specified news article information from Newsapi.org and stores that information in AWS s3 bucket
The specification for the type of news article information is by top headlines in English or by specified topic
'''
class News():
    def __init__(self, apikey: str):
        self.apikey = apikey

    def _info(topic = "top_headlines": str):
    '''request information from newsapi.org
       returns json
    '''
        if topic == "top_headlines":
            url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(self.apikey)
        else:
            url = "https://newsapi.org/v2/everything?q={}&apiKey={}".format(topic, self.apikey)
        response = requests.get(url)
        return response.json()

    def flatten(s3bucket: str, sourceName: str, topic = "top_headlines": str):
    ''' Flattens json into a csv and stores the csv in s3 bucket
        Raises an Airflow error if there is an newsapi.org api error
    '''
        info = self._info(topic)
        if info["status"]== "error":
            raise AirflowException("{}:{}".format(info["code"], info["message"]))

        articles, date = info["articles"], date.today()
        filename = "{}_{}.csv".format(date, topic)
        with open(filename, "w") as f:
            writer = csv.writer(f)

            if articles == []:         # no articles for topic
                writer.writerow(["0 resutls for topic"])
            else:
                header = ["Source Name", "Source ID", "Author", "Title","Published",
                          "Description", "URL", "Image url", "Content"]

                
                writer.writerow(header)
                for a in topArticlees:
                    row = [a["source"]["name"], a["source"]["id"], a["author"], a["title"],
                           a["publishedAt"], a["description"], a["url"],
                           a["urlToImage"], a["content"]]
                    writer.writerow(row)

        #store in s3 bucket
        s3 = boto3.resource("s3")
        bucket = "{}/{}".format(s3bucket,sourcename)
        s3.meta.client.upload_file(filename, bucket, filename)
        

        
