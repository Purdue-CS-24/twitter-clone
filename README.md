# peteSpace

peteSpace is a Twitter-like application created using Vue.js, Flask, and SQLite. Created during the Wednesday workshop, _Backend Programming_.

The intention is for you to fork or clone this repository and create a backend application using Flask that connects with the already complete Vue.js client.

## Usage

Ensure that `node`, `yarn`, and `python3` are installed.

### Client

First, install the dependencies for the client app:
```
cd client/
yarn install
```

You can then start a development server to test out the client:
```
cd client/
yarn serve
```
---

### Server 

First, create and activate a virtual environment.

For macOS/Linux:
```
cd server/
python3 -m venv venv
. venv/bin/activate
```

For Windows:
```
cd server\
python3 -m venv venv
. venv\Scripts\activate
```

Install the dependencies for the application:
```
cd server/
pip install -r requirements.txt
```

If you'd like to start over with a new database:
```
cd server/
sqlite3 database.db
sqlite3> .read schema.sql
sqlite3> .quit
```

Now you can run the server in development mode:
```
cd server/
export FLASK_ENV=dev
flask run
```

## Caveats

As stated in the workshop, you should **NOT** actually store a `SECRET_KEY` in a config file that is committed to version control. This key should be stored in a separate place, such as a `.env` file that you read in but do not commit to version control, or as an environment variable.

## License

Licensed under the [MIT License](LICENSE).
