CREATE TABLE users (
    id serial PRIMARY KEY,
    name varchar(100) NOT NULL,
    email varchar(60) NOT NULL UNIQUE,
    PASSWORD varchar(100) NOT NULL
);

CREATE TABLE tags (
    id serial PRIMARY KEY,
    name varchar(25) NOT NULL,
    user_id integer NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE (name, user_id)
);

CREATE TABLE tasks (
    id serial PRIMARY KEY,
    title varchar(50) NOT NULL,
    content text,
    creation_date timestamp NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    tag_id integer REFERENCES tags(id) ON DELETE SET NULL
);