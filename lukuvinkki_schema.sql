CREATE TABLE lukuvinkki (
    id serial primary key,
	user foreign key,
	current_type text,
	title text,
	author text,
	isbn text,
	is_read boolean,
	link text,
	descript text,
	comment text
);