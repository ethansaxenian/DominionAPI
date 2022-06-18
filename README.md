# DominionAPI

An API for the game Dominion

Powered by FastAPI

## Installation and setup instructions:

### Set up the database:
DominionAPI currently supports Google Cloud Firestore and the various [dialects supported by SQLAlchemy](https://docs.sqlalchemy.org/en/14/dialects/). 

#### Set up a Cloud Firestore database:
1. Create a firestore database by following the instructions at [https://firebase.google.com/docs/firestore/quickstart#create](https://firebase.google.com/docs/firestore/quickstart#create).

2. Ccreate a service account for your database by following the instructions at [https://firebase.google.com/docs/admin/setup#initialize-sdk](https://firebase.google.com/docs/admin/setup#initialize-sdk).

3. Add the following lines to a `.env` file with values from the service account JSON file:
   ```shell
   FIRESTORE_PROJECT_ID=<"project_id">
   FIRESTORE_PRIVATE_KEY=<"private_key">
   FIRESTORE_CLIENT_EMAIL=<"client_email">
   FIRESTORE_TOKEN_URI=<"token_uri">
   ```

4. Set up the project to use Firestore by setting `DB_TYPE=firestore` in the `.env` file.

#### Set up a SQL database:
1. Add `DB_URI=<your_database_uri>` to the `.env` file. By default this is set to `sqlite:///dominion.db`.

2. Set up the project to use your SQL database by setting `DB_TYPE=sqlalchemy` in the `.env` file.

### Run the development server:
Make sure you have `poetry` installed on your machine. Instructions can be found at [https://python-poetry.org/docs/master](https://python-poetry.org/docs/master).

Running `make run` will install the project dependencies and start the development server.

Run `make seed` to seed the database.

Run `make help` to view the list of available commands.
