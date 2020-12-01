/*

        This table lists the N-P-K composition for a crop-irrigation type combination 

*/


drop table if exists nutrient_ref_tbl;

create table nutrient_ref_tbl(
		ref_id serial PRIMARY KEY,
        crop_name varchar(50) NOT NULL,
        irrigation_type_code char(1) NOT NULL,
        n_kg_per_acre int NOT NULL,
        p_kg_per_acre int NOT NULL,
        k_kg_per_acre int NOT NULL,
        taluka_code int,
        user_id varchar(50) NOT NULL,		
        activity varchar(10) NOT NULL,
		activity_timestamp TIMESTAMP default CURRENT_TIMESTAMP
);

create unique index nutrient_idx on nutrient_ref_tbl(crop_name,irrigation_type_code, taluka_code);

select n.crop_name, n.irrigation_type_code, n.n_kg_per_acre, n.p_kg_per_acre, n.k_kg_per_acre, s.taluka_code, s.taluka_name
from  nutrient_ref_tbl n join
	  state_taluka_xref_tbl s
	on n.taluka_code = s.taluka_code;


/*

        This table has the audit history of the changes done to nutrient_ref_tbl

*/

drop table if exists nutrient_audit_tbl;

create table nutrient_audit_tbl(
		audit_ref_id integer NOT NULL,
        audit_crop_name varchar(50) NOT NULL,
        audit_irrigation_type_code char(1) NOT NULL,
        audit_N_kg_per_ha int NOT NULL,
        audit_P_kg_per_ha int NOT NULL,
        audit_K_kg_per_ha int NOT NULL,
        audit_user_id varchar(50),
        audit_activity varchar(10)  NOT NULL,
		audit_activity_timestamp timestamp default current_timestamp PRIMARY KEY
);


INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Cotton','R',30,15,15,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Cotton','I',80,40,40,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Chilli','R',100,50,50,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Chilli','I',150,75,75,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Sorghum','R',50,20,0,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Sorghum','I',100,75,37.5,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Maize','R',100,50,25,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Maize','I',187.5,75,37.5,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Bengal gram','R',10,25,0,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Bengal gram','I',25,50,0,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Green gram','R',12.5,25,20,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Paddy (Transplanted)','R',150,75,75,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Paddy (Transplanted)','I',150,75,75,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('DSR Paddy','R',100,50,50,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Onion','R',125,50,125,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Wheat','R',100,75,50,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Wheat','I',50,25,0,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Safflower','R',75,75,40,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Safflower','I',40,40,12.5,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Red gram','R',25,50,20,'Sandhya','Dataload',1);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Wheat','R',100,75,50,'Sandhya','Dataload',2);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Wheat','I',50,25,0,'Sandhya','Dataload',2);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Safflower','R',75,75,40,'Sandhya','Dataload',2);
INSERT INTO nutrient_ref_tbl (crop_name,irrigation_type_code,n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,taluka_code) VALUES ('Safflower','I',40,40,12.5,'Sandhya','Dataload',2);

select n_per_bag_kg, p_per_bag_kg, k_per_bag_kg,fertilizer_name,bag_weight_kg, bag_cost_INR from fertilizer_ref_tbl where fertilizer_name in 
('Urea','Vijetha')
order by fertilizer_name


select variety_name from crop_variety_ref_tbl where crop_name = 'Chilli'

select * from crop_variety_ref_tbl 


select ref_id, crop_name, irrigation_type_code, taluka_code,n_kg_per_acre, p_kg_per_acre, k_kg_per_acre, user_id, activity, 
activity_timestamp from nutrient_ref_tbl 
where crop_name = 'Chilli' and irrigation_type_code = 'R' and taluka_code = 1


select * from state_taluka_xref_tbl 


