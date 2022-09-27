insert into users (name, email, password) values 
('Mike', 'real@mail.com', '123'),
('Sammy', 'cool@mail.com', 'abc'),
('jon', 'awesome@mail.com', '123'),
('jon', 'bad@mail.com', 'qawsed');

insert into users (name, email, password) values ('AAAA', 'real@mail.com', '123'); --should fail

insert into tags (name, user_id)
	values ('work', 1),
	('school', 1),
	('work', 2),
	('programming', 3),
	('3d printing', 3),
	('work stuff', 4),
	('other', 6);

insert into tags (name, user_id)
	values ('work', 1); --should fail

insert into tasks (title, content, creation_date, user_id, tag_id)
	values ('Do something', 'Big description of something', now()::TIMESTAMP, 1, null),
	('Do something', 'Big description of something else', now()::TIMESTAMP, 1, 1),
	('Do something', null, now()::TIMESTAMP, 1, 2),
	('I just wana quit already', 'Big description of something', now()::TIMESTAMP, 2, null),
	('AAAAAASDSDDSAD', '3d printiiiiing', now()::TIMESTAMP, 3, 5);
    
select users.name, tasks.title, tags.name from users
	join tasks on tasks.user_id = users.id
	left join tags on tags.id = tasks.tag_id;