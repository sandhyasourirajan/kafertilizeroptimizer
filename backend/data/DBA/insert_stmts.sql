-- insert region detail 

insert into region_dtl_tbl (state_name,district_name, taluka_name) values ('Karnataka','Dharwad','Navalagund');
insert into region_dtl_tbl (state_name,district_name, taluka_name) values ('Karnataka','Bellary','Siruguppa');

select * from region_dtl_tbl;

-- insert variety

insert into crop_variety_ref_tbl (crop_name,variety_name) values ('Chilli','Poosa Jawal');
insert into crop_variety_ref_tbl (crop_name,variety_name) values ('Chilli','Arka Lohith');

select * from crop_variety_ref_tbl;

-- insert nutrient 

insert into nutrient_ref_tbl (crop_name, irrigation_type_code, N_kg_per_ha, P_kg_per_ha, K_kg_per_ha,activity) values ('Paddy','R',100,75,75,'dataload');
insert into nutrient_ref_tbl (crop_name, irrigation_type_code, N_kg_per_ha, P_kg_per_ha, K_kg_per_ha,activity) values ('DSR Paddy','R',100,50,50,'dataload');
insert into nutrient_ref_tbl (crop_name, irrigation_type_code, N_kg_per_ha, P_kg_per_ha, K_kg_per_ha,activity) values ('Sorghum','I',100,75,40,'dataload');
insert into nutrient_ref_tbl (crop_name, irrigation_type_code, N_kg_per_ha, P_kg_per_ha, K_kg_per_ha,activity) values ('Sorghum','R',50,25,0,'dataload');
insert into nutrient_ref_tbl (crop_name, irrigation_type_code, N_kg_per_ha, P_kg_per_ha, K_kg_per_ha,activity) values ('Chilli','I',75,50,0,'dataload');
insert into nutrient_ref_tbl (crop_name, irrigation_type_code, N_kg_per_ha, P_kg_per_ha, K_kg_per_ha,activity) values ('Chilli','R',25,25,0,'dataload');

-- insert fertilizer fertilizer_ref_tbl

insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Urea',300,50,46.5,0,0,1,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Vijetha',300,50,46.5,0,0,1,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Amonium Chloride',1170,50,26.16,0,0,1,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Amonium Sulphate',600,50,21.21,0,0,2,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Single Super Phosphate',350,50,0,16,0,1,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('MOP',579,50,0,0,52.3,2,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Potassium Nitrate',110,2,13.86,0,38.61,2,'dataload');
insert into fertilizer_ref_tbl (fertilizer_name,bag_cost_INR,bag_weight_kg,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,region_code,activity) values ('Potassium Nitrate',110,2,13.86,0,38.61,1,'dataload');

select * from fertilizer_ref_tbl;
select * from fertilizer_audit_tbl;
select * from nutrient_ref_tbl;

--select * from fertilizer_transaction_tbl;

select * from transaction_tbl;

select a.*, b.* from transaction_tbl a, fertilizer_transaction_tbl b where a.fertilizer_ID = b.fertilizer_ID;
select a.fertilizer_ID, a.crop_name, a.variety, a.irrigation_type_code, a.N_deficit, a.P_deficit, a.K_deficit, a.estimated_cost , group_concat(b.Value)
--b.fertilizer_name, b.unit_in_kg, b.fertilizer_qty_kgs, b.fertilizer_qty_bags 
from transaction_tbl a, fertilizer_transaction_tbl b where a.fertilizer_ID = b.fertilizer_ID group by a.fertilizer_ID;


select f.fertilizer_name, f.bag_weight_kg, f.bag_cost_INR, s.region_code, f.n_per_bag_kg, f.p_per_bag_kg, f.k_per_bag_kg, s.taluka_name
from 	fertilizer_ref_tbl f join
		region_dtl_tbl s
		on f.region_code = s.region_code;

select * from fertilizer_ref_tbl
	
	select * from region_dtl_tbl

select n.crop_name, n.irrigation_type_code, n.n_kg_per_acre, n.p_kg_per_acre, n.k_kg_per_acre, s.taluka_code, s.taluka_name
from  nutrient_ref_tbl n join
	  state_taluka_xref_tbl s
	on n.taluka_code = s.taluka_code;
