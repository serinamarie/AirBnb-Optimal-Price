# AirBnB Optimal Price Team 1

An API to predict daily AirBnB rates in Tokyo from property features.

## Getting Started

This section is dedicated to software developers that want to contribute to this API. You must have `pipenv` installed on your local machine to continue.

[Pipenv: Python Development Workflow for Humans
](https://github.com/pypa/pipenv)

### Environment Variables

If you have been provided rights, simply clone this repo. If not, you may fork and clone the repo:

```
git clone <url>
```

Once cloned, create a `.env` file in the main directory and add the following variables:

```
FLASK_APP=api:APP 
FLASK_ENV=development
```

Then you can use the following commands to create a local pipenv environment and install all required dependencies:

```
pipenv shell
pipenv install
```

### Start the API

Finally, you can run the following command to start the API:

```
flask run
```

## Endpoints

### POST /predict

#### Request
Cleaning fee is in **Yen**. Options currently available for **neighbourhood_cleansed** are:
* Sumida Ku
* Hino Shi
* Chuo Ku

For **property_type**:
* Apartment
* House
* Hostel
* Hotel

For **room_type**:
* Entire home/apt
* Private room
* Hotel room
* Shared room

```json
{
	"host_response_rate": 100,
	"neighbourhood_cleansed": "Sumida Ku",
	"property_type": "Apartment",
	"room_type": "Shared room",
	"bathrooms": 1,
	"cleaning_fee": 323,
	"minimum_nights": 1,
	"instant_bookable": 0,
	"kitchen": 1,
	"smoke_detector": 0,
	"self_check_in": 1,
	"hot_water": 0,
	"accommodates":0,
	"local_host": 0
}
```

#### Response
Predicted price is returned in **Yen**.

```json
{
    "predicted_price": 1211
}
```