# poke-api

## Prerequisites

* Python 3.8+

## Setup

1. Create virtual enviroment
```
    cd poke-api
    $ python3 -m venv venv --system-site-packages
```
2. Activate virtual enviroment
```
    . venv/bin/activate
```
3. Install project requirements
```
    pip install -r requirements.txt 
```
4. Copy example enviroment file into real one. After copying fill the variables in it with the ones you'll use
```
    cp .env.example .env
```

The variable POKE_API_URL should be the base url of the PokeAPI-compatible API to be used with no trailing slash

## Running

1. Start the flask app server
```
    flask run
```

You can now connect to the server using the URL printed in your terminal

## Testing

1. Run the testing commnad from the root directory
```
    python -m pytest tests
```