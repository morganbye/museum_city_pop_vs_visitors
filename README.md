# Museum city population to visitation correlation

## Scenario
A new world organization has just been created. It includes all the museum management committees that have more than 2,000,000 visitors annually (in 2018).

This new organization wishes to correlate the tourist attendance at their museums with the population of the respective cities. To achieve this, a small, common and harmonized database must be built to be able to extract features. This DB must include the characteristics of museums as well as the population of the cities in which they are located. You have been chosen to build this database. In addition, you are asked to create a small linear regression ML algorithm to correlate the city population and the influx of visitors.  You must use the Wikipedia APIs to retrieve this list of museums and their characteristics. You are free to choose the source of your choice for the population of the cities concerned.

## Usage
The project is supplied with `docker-compose.yml` and `Dockerfile`s for one-step processing.

To build a new Docker image

```bash
make build
```

To run the built Docker image
```bash
make run
```

The Jupyter notebook can be found in the `notebook-docker` directory.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)