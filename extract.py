import twint 

c = twint.Config()
c.Search = 'data science role hiring'
c.Lang = "en"
c.Limit = 200
c.Output = "datascience2.csv"
c.Store_csv = True

#run
twint.run.Search(c)
