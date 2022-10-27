# DominionAPI

An API for the game Dominion

Powered by [FastAPI](https://fastapi.tiangolo.com/)

## Installation and setup instructions:

### Set up the database:
Add `DATABASE_URL=<your_database_url>` to the `.env` file. By default this is set to `sqlite:///dominion.db`.

DominionAPI currently supports sqlite and postgresql databases. 


### Run the development server:
Make sure you have `poetry` installed on your machine. Instructions can be found at [https://python-poetry.org/docs](https://python-poetry.org/docs).

Running `make run` will install the project dependencies, seed the database, and start the development server. (To set up the project without running the dev server, simply run `make`.)

To get new card data, run `make scrape`. (All card data is obtained from http://wiki.dominionstrategy.com/index.php/List_of_cards.) Then, run `make seed` to load the data into the database.

Run `make help` to view the list of available commands.


### Deployment:
Dominion API is deployed by [deta](https://www.deta.sh/). See the [docs](https://docs.deta.sh/docs/home) for details about deployment or you can quickly deploy your own instance of the API with the button below.

Make sure to configure the `API_KEY` and `DATABASE_URL` environment variables.

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/ethansaxenian/DominionAPI)
