CREATE TABLE users (
    id serial primary key,
	username text,
	password text,
	time_created time
);

CREATE TABLE lukuvinkki (
    id serial primary key,
	user_id integer references users(id),
	current_type text not null,
	title text not null,
	author text,
	isbn text,
	is_read boolean default false,
	link text,
	descript text,
	comment text
);