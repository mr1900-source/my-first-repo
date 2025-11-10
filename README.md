
### Virtual Environment

Create and activate a virtual environment:

```sh
conda create -n my-first-env-2025 python=3.11
conda activate my-first-env-2025
```

### Packages

Install packages:

```sh
# pip install pytest
pip install -r requirements.txt
```

## Configuration

The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:


```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"

## Usage

Play a game of rock, paper scissors:
```sh
# only works if this file does NOT import from other local py files:
python app/rps.py
# if this file imports from other local py files:
python -m app.rps
```

Run the stocks dashboard:

```sh
python -m app.stocks
```

## Tests

Run the tests:
```sh
# find all the tests and run them:
pytest
```

