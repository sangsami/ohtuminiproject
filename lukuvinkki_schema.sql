CREATE TABLE lukuvinkki (
    id serial primary key,
	current_type lukuvinkki_type,
	title text,
	author text,
	is_read boolean,
	link text,
	descript text,
	comment text
);