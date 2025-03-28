# [Travel Itinerary Generator]
***

<img title="Travel-Itinerary-Generator" align='right' src="/static/logo.png" alt="Travel Itinerary Generator Logo" width="150"/>

Effortlessly design your perfect getaway with the Travel Itinerary Generator! This intuitive trip planner is your go-to assistant for creating smooth and well-organized travel experiences. Whether you're setting off on a road trip, exploring a new city, or traveling abroad, our tool streamlines every step of the planning process.

<p align="center">
Make your travel dreams a reality. Start planning your next adventure with the Travel Itinerary Generator today!
</p>
<p align="center">
<i>Explore, discover, and make every trip unforgettable.*</i>
</p>

## Table of Contents

- [Travel Itinerary Generator](#travel-itinerary-generator)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Limitations \& Future Work](#limitations--future-work)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup and Installation](#setup-and-installation)
  - [API Keys](#api-keys)
  - [Usage](#usage)


## About

The Travel Itinerary Generator is a software tool designed to help travelers easily craft customized travel plans. By taking into account users' preferences, budgets, and travel dates, this application provides detailed recommendations for activities, attractions, and accommodations. Whether you're a seasoned explorer or a first-time traveler, the Travel Itinerary Generator helps you save time while ensuring a fulfilling and well-organized trip..

## Limitations & Future Work
- The Travel Itinerary Generator works only based on the user's source and destination and time of travel.

##Future Work
- The Travel Itinerary Generator is not able to generate itineraries for multiple destinations.
- The Travel Itinerary Generator is not able to suggest hotels and flights.
- **Real-time Collaboration:** In an increasingly interconnected world, we plan to introduce real-time collaboration features. Users will be able to share their itineraries with travel companions or collaborators, making group travel planning an effortless and collaborative experience.

## Features

- **Weather Forecast:** The Travel Itinerary Generator provides a weather forecast of the destination for the whole travel time.
- **Travel Itinerary:** The Travel Itinerary Generator provides a travel itinerary for the whole travel time in an optimum budget.

## Requirements

- Python 3.11
- Flask
- Flask-SQLAlchemy
- google-generativeai==0.2.2

## Setup and Installation

1.   cd Travel-Itinerary-Generator
2. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```

## API Keys
- Visual Crossing Weather API Key: [Sign up](https://www.visualcrossing.com/weather-api) for a free account and get your API key.
- Google Palm API: [Sign up](https://makersuite.google.com) for a free account and get your API key.

## Usage
- Please follow the instructions below to run the application locally.

Write API keys: In a `.env` file.
```shell
WEATHER_API_KEY='Your Visual Crossing Weather API Key'
PALM_API_KEY='Your Google Palm API Key'
```
and save it in the root directory of the project.

Run the following command to start the application:
```shell
python wsgi.py
```




