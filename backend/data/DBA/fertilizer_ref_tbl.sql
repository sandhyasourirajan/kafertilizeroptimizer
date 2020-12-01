drop table if exists fertilizer_ref_tbl;

create table fertilizer_ref_tbl(
		ref_id serial PRIMARY KEY,
        fertilizer_name varchar(50),
        cost_per_kg float,
        bag_weight_kg float,
        bag_cost_INR float,
        n_per_bag_kg float,
        p_per_bag_kg float,
        k_per_bag_kg float,
        taluka_code int,
        user_id varchar(50) NOT NULL,
        activity varchar(10) NOT NULL,
		activity_timestamp timestamp default current_timestamp
);

create unique index fertilizer_idx on fertilizer_ref_tbl(fertilizer_name,cost_per_kg,bag_weight_kg);

INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Urea',5.90,50.0000,295.00,23.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Ammonium Sulphate',12.00,50.0000,600.00,10.30,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Single Super Phosphate',7.00,50.0000,350.00,0.00,3.50,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('MOP',13.60,50.0000,680.00,0.00,0.00,30.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Sulphur',50.00,10.0000,500.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Gypsum',5.00,50.0000,250.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Mangala Gold',60.00,10.0000,600.00,4.60,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('DAP',25.60,50.0000,1280.00,4.50,11.50,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Pottasium Nitrate',110.00,1.0000,110.00,0.13,0.00,0.45,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('28:28:00',22.00,50.0000,1100.00,14.00,14.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('14:35:14',22.00,50.0000,1100.00,7.00,17.50,7.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('16:20:13',16.40,50.0000,820.00,8.00,10.00,6.50,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('12:32:16',23.40,50.0000,1170.00,6.00,16.00,8.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('17:17:17',19.00,50.0000,950.00,8.50,8.50,8.50,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('10:26:26',23.60,50.0000,1180.00,5.00,13.00,13.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('15:15:15',17.00,50.0000,850.00,7.50,7.50,7.50,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('19:19:19',100.00,1.0000,100.00,9.50,9.50,9.50,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('0.5 % EDTA Zinc Sulphate ',750000.00,0.0001,75.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('0.5 % Ferrous Sulphate',150.00,1.0000,150.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('2 % Borax',110.00,1.0000,110.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('2% Calcium Chloride (CaCl2)',200.00,1.0000,200.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Calcium nitrate 30 g/l dry',2666.67,0.0300,80.00,0.01,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Zinc Sulphate',150.00,1.0000,150.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Manganese Sulphate',80.00,1.0000,80.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Magnesium Sulphate',110.00,1.0000,110.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Ferrous Sulphate',43.20,25.0000,1080.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Borax',310.00,1.0000,310.00,0.00,0.00,0.00,1,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Urea',5.80,50.0000,290.00,23.00,0.00,0.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('DAP',21.60,50.0000,1080.00,9.00,23.00,0.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('MOP',11.80,50.0000,590.00,0.00,0.00,30.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('20:20:0:13',17.00,50.0000,850.00,10.00,10.00,0.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('10:26:26',21.00,50.0000,1050.00,5.00,13.00,13.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('19:19:19',17.80,50.0000,890.00,9.50,9.50,9.50,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('17:17:17',15.60,50.0000,780.00,8.50,8.50,8.50,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('28:28:00',23.30,50.0000,1165.00,14.00,14.00,0.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('12% EDTA',700.00,0.5000,350.00,0.00,0.00,0.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('21% EDTA',700.00,0.5000,350.00,0.00,0.00,0.00,2,'Sandhya','Dataload');
INSERT INTO fertilizer_ref_tbl (fertilizer_name,cost_per_kg,bag_weight_kg,bag_cost_INR,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity) VALUES ('Borax',360.00,0.2500,90.00,0.00,0.00,0.00,2,'Sandhya','Dataload');

select count(*) from fertilizer_ref_tbl;

select f.fertilizer_name, f.bag_weight_kg, f.bag_cost_INR, s.taluka_code, f.n_per_bag_kg, f.p_per_bag_kg, f.k_per_bag_kg, s.taluka_name
from 	fertilizer_ref_tbl f join
		state_taluka_xref_tbl s
		on f.taluka_code = s.taluka_code;
	
		
/*

        This table has the audit history of the changes done to nutrient_ref_tbl

*/

drop table if exists fertilizer_audit_tbl;

create table fertilizer_audit_tbl(
		audit_ref_id integer NOT NULL,
        audit_fertilizer_name varchar(50) NOT NULL,
        audit_cost_per_kg float,
        audit_bag_weight_kg float,
        audit_bag_cost_INR float,
        audit_n_per_bag_kg float,
        audit_p_per_bag_kg float,
        audit_k_per_bag_kg float,
        audit_region_code int,
        audit_user_id varchar(50),
        audit_activity varchar(10)  NOT NULL,
		audit_activity_timestamp timestamp default current_timestamp  PRIMARY KEY);
