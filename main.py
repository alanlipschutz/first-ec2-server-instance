import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return 'Hello, this is my first server running in an EC2 instance using FastAPI!'


if __name__ == '__main__':
    uvicorn.run(app, host='', port=8000)

