# Múinteoir Gift Exchange

Matches gift givers and receivers together. Takes input from a Google Form with its data exported as a CSV with the following headers:

 - timestamp
 - live_in_ireland
 - instagram
 - address
 - email
 - other

# Installation

```
$ pipenv install .
```

# Running

```
$ pipenv run python -m muinteoir_gift_exchange generate --csv-file data.csv
```