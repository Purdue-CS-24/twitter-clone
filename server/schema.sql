DROP TABLE IF EXISTS users;
DROP INDEX IF EXISTS user_username;

DROP TABLE IF EXISTS posts;

PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id INTEGER UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    pw_hash BLOB NOT NULL,

    PRIMARY KEY(id)
);
CREATE UNIQUE INDEX user_username ON users(username);

CREATE TABLE posts (
    id INTEGER UNIQUE NOT NULL,
    time_posted TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);
