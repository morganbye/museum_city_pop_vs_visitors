# Museum city population to visitation correlation

## Scenario
A new world organization has just been created. It includes all the museum 
management committees that have more than 2,000,000 visitors annually (in 2018).

This new organization wishes to correlate the tourist attendance at their 
museums with the population of the respective cities. To achieve this, a small, 
common and harmonized database must be built to be able to extract features. 
This DB must include the characteristics of museums as well as the population 
of the cities in which they are located. You have been chosen to build this 
database.

In addition, you are asked to create a small linear regression ML algorithm 
to correlate the city population and the influx of visitors.

## Usage
The project is supplied with `docker-compose.yml` and `Dockerfile`s for one-step processing.

To build a new Docker image

```bash
make build
```

To run the application

```bash
make run
```

The Jupyter notebook can be found in the `notebook-docker` directory, and can be called directly using

```bash
make run-notebook
```

If running locally, you'll need to mount a local volume to write the results to. In which case, call

```bash
docker run -v /full/path/to/results:/app/notebook/results museums_notebook
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)