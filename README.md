# DominionAPI

An API for the game Dominion

Powered by [FastAPI](https://fastapi.tiangolo.com/) and [Deta](https://deta.space/)

## Installation and setup instructions:

### Set up the database:
DominionAPI uses [Deta Base](https://deta.space/docs/en/reference/base/about). 
To configure, add `DETA_BASE_PROJECT_KEY=<your_project_key>` to the `.env` file.

To create a new project key, visit your [Deta builder page](https://deta.space/builder/).

### Run the development server:
Make sure you have `poetry` installed on your machine. Instructions can be found at [https://python-poetry.org/docs](https://python-poetry.org/docs).

To get card data, run `make scrape`. (All card data is obtained from http://wiki.dominionstrategy.com/index.php/List_of_cards.) Then, run `make seed` to load the data into the database.

Running `make insatll` will install the project dependencies and `make run` will start the development server.


Run `make help` to view the list of available commands.
