import google.generativeai as palm
import os
from dotenv import load_dotenv
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")
palm.configure(api_key=palm_api_key)
model = palm.GenerativeModel(model_name="gemini-1.5-flash-8b-exp-0924")
def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} on {start_date} to {end_date}, with an optimum budget (Currency:INR)."
    response = model.generate_content(prompt)
    return(response.text)
