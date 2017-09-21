# pm25watcher

A watcher for pm25 data from pm25.in

# Introduction

Very simple program for collecting data from pm25.in

# Usage

1. Copy `config.ini-template` into `config.ini`.
2. Change the `token` string to what you applyed from pm25.in (the default value works but is limited in functions).
3. Change the `file_pattern` where you save your file, the `%s` will be replaced with a timestamp.
4. Run `python watcher.py`

The API provided by pm25.in returns a list of monitor data of air.
Totally 190 cities and 946 items

* aqi
* area
* co
* co_24h
* no2
* no2_24h
* o3
* o3_24h
* o3_8h
* o3_8h_24h
* pm10
* pm10_24h
* pm2_5
* pm2_5_24h
* position_name
* primary_pollutant
* quality
* so2
* so2_24h
* station_code
* time_point