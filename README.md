# pm25watcher

A watcher for pm25 data from pm25.in

# Introduction

Very simple program for collecting data from pm25.in

# Usage

1. Copy `config.ini-template` into `config.ini`.
2. Change the `token` string to what you applyed from pm25.in (the default value works but is limited in functions).
3. Change the `file_pattern` where you save your file, the `%s` will be replaced with a timestamp.
4. Run `python watcher.py`