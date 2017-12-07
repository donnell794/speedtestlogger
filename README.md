#Speedtest Logger

Forked and modified from the Speedcomplainer

Logging can be done to CSV files, with a log file for ping results and speed test results. 

CSV Logging config example:
```
"log": {
    "type": "csv",
    "files": {
        "ping": "pingresults.csv",
        "speed": "speedrestuls.csv"
    }
}
```

## Usage
> python speedcomplainer.py

Or to run in the background:

> python speedcomplainer.py > /dev/null &


