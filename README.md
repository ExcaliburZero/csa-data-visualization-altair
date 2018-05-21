# CSA Data Visualization
This is a program that hosts a webpage with visualizations of SUNY Oswego's Computer Science Association meeting dataset.

## Usage
To generate the html webpage with the data visualizations, run the following commands.

```
# Grab the dataset
$ mkdir data
$ curl -o data/meetings.csv http://www.cs.oswego.edu/~cwells2/code/csa-data-visualization/meetings.csv

# Generate the plot page
$ pipenv run python plots.py 
```
