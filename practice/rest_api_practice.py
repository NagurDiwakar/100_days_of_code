import requests
import logging

from fastapi import FastAPI

app = FastAPI()

@app.get("/joke")
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        logging.info(f"Joke fetched: {joke_data['setup']} - {joke_data['punchline']}") 
        return {
            "setup": joke_data["setup"],
            "punchline": joke_data["punchline"]
        }
    else:
        return {"error": "Could not fetch a joke at this time."}
    
@app.get("/")
def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Welcome to the Joke API! Visit /joke to get a random joke."}    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




