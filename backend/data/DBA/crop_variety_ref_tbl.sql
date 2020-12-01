/*

        This table lists the different varieties present under a crop 

*/

drop table if exists crop_variety_ref_tbl;

create table crop_variety_ref_tbl(
		ref_ID serial PRIMARY KEY,
        crop_name varchar(50) NOT NULL,
        variety_name varchar(80) NOT NULL
        --FOREIGN KEY(crop_name) REFERENCES nutrient_ref_tbl(crop_name)
);


select * from nutrient_ref_tbl

create unique index crop_variety_idx on crop_variety_ref_tbl(crop_name, variety_name);

--insert into crop_variety_ref_tbl (crop_name,variety_name) values ('Chilli','Poosa Jawal');
--insert into crop_variety_ref_tbl (crop_name,variety_name) values ('Chilli','Arka Lohith');
--
--select * from crop_variety_ref_tbl;