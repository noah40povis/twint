

from fastapi import Depends, FastAPI, HTTPException

from database import *



app = FastAPI(
    title= 'Tweet Stock Analysis',
    description= "A web application that runs NLP on tweets and allows the user to run analysis on their investments",
    version= '1.0',
    docs_url= '/',
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/health')
def healthcheck():
    return "OK"


# if __name__ == '__main__':
#     uvicorn.run(app)

