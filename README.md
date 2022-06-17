# DominionAPI

An API for the game Dominion

Powered by FastAPI

## Installation and setup instructions:

### Set up the database:
DominionAPI currently supports cloud firestore. 

#### Set up a cloud firestore database:
1. Create a firestore database by following the instructions at <a href="https://firebase.google.com/docs/firestore/quickstart#create" target="_blank" rel="noopener noreferrer">https://firebase.google.com/docs/firestore/quickstart#create</a>.

3. Create a service account for your database by following the instructions at <a href="https://firebase.google.com/docs/admin/setup#initialize-sdk" target="_blank" rel="noopener noreferrer">https://firebase.google.com/docs/admin/setup#initialize-sdk</a>.

4. Add the path to the service account JSON file to a `.env` file in the project:

      ```
      echo GOOGLE_APPLICATION_CREDENTIALS=<path/to/serviceAccount.json> >> .env
      ```

5. Set up the project to use firestore by setting `DB_TYPE=firestore` in the `.env` file.

### Run the development server:
Make sure you have `poetry` installed on your machine. Instructions can be found at <a href="https://python-poetry.org/docs/master" target="_blank" rel="noopener noreferrer">https://python-poetry.org/docs/master</a>.

Running `make run` will install the project dependencies and run the development server.

Run `make seed` to seed the database.

Run `make help` to view the list of available commands.
