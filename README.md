# DominionAPI

An API for the game Dominion

Powered by FastAPI

## Installation and setup instructions:

### Set up the database:
DominionAPI currently supports cloud firestore. 

#### Set up a cloud firestore database:
1. Create a firestore database by following the instructions at [https://firebase.google.com/docs/firestore/quickstart#create](https://firebase.google.com/docs/firestore/quickstart#create).

2. Create a service account for your database by following the instructions at [https://firebase.google.com/docs/admin/setup#initialize-sdk](https://firebase.google.com/docs/admin/setup#initialize-sdk).

3. Add the path to the service account JSON file to a `.env` file in the project:

      ```
      echo GOOGLE_APPLICATION_CREDENTIALS=<path/to/serviceAccount.json> >> .env
      ```

4. Set up the project to use firestore by setting `DB_TYPE=firestore` in the `.env` file.

### Run the development server:
Make sure you have `poetry` installed on your machine. Instructions can be found at [https://python-poetry.org/docs/master](https://python-poetry.org/docs/master).

Running `make run` will install the project dependencies and run the development server.

Run `make seed` to seed the database.

Run `make help` to view the list of available commands.
