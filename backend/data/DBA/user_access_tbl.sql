drop table if exists user_access_tbl;

create table user_access_tbl(
		email_ID varchar(100) PRIMARY KEY,
		user_access varchar(20)
);

create unique index user_access_idx on user_access_tbl(email_ID, user_access);


INSERT INTO user_access_tbl (email_ID,user_access) VALUES ('sandhya.sourirajan@gmail.com','admin');


select distinct fertilizer_name from fertilizer_ref_tbl where taluka_code  = 1;

select * from state_taluka_xref_tbl 

