/*

        This table lists the region code for a state-district-taluka combination. 
        Region code from this table is used in fertilizer_ref_tbl & transaction_tbl

*/

drop table if exists state_taluka_xref_tbl;

create table state_taluka_xref_tbl(
		taluka_code serial PRIMARY KEY,
        state_name varchar(30) NOT NULL,
        district_name varchar(50) NOT NULL,
        taluka_name varchar(50) NOT NULL
);

create unique index state_taluka_xref_idx on state_taluka_xref_tbl(state_name, district_name, taluka_name);

insert into state_taluka_xref_tbl (state_name, district_name, taluka_name) values ('Karnataka','Dharwad','Navalagund');
insert into state_taluka_xref_tbl (state_name, district_name, taluka_name) values ('Karnataka','Bellary','Siruguppa');

select * from state_taluka_xref_tbl;

select * from transaction_tbl;

select * from fertilizer_transaction_tbl where fertilizer_ID;

select * from nutrient_ref_tbl;
select * from fertilizer_audit_tbl;

delete from nutrient_ref_tbl where crop_name = 'Capsicum';