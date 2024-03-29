from fastapi import FastAPI, Query
# from main import app
import uvicorn

# Create FastAPI app
app = FastAPI()

# Define routes using the app object
@app.get('/')  # Use app.get() for GET requests
async def greet():
    return "Hello World Welcome Sahil Here"

@app.get('/greet1')
async def greet1():
    return "Welcome to other url Here"

@app.get('/tata')
async def tata():
    return "Have a good day"

@app.post('/addition')
async def addition(num1: int = Query(..., description="First number"), num2: int = Query(..., description="Second number")):
    return {"result": num1 + num2}

# For /addition1, since it's expecting query parameters, use GET method
@app.get('/addition1')
async def addition1(num1: int = Query(15, description="First number"), num2: int = Query(25, description="Second number")):
    return {"result": num1 + num2}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
# if __name__ == "__app__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
