import twint 

c = twint.Config()
#tweets that contain these texts 
c.Search = 'raised Series A'
#timeframe 
c.Since = '2020-01-01'
#language of tweets 
c.Lang = "en"
#store to csv 
# c.Output = "datascience4.csv"
# c.Store_csv = True
#store in elastic search instance
c.Elasticsearch = "http://127.0.0.1:9200/"
#run
twint.run.Search(c)
