
insert_fertilizer_ref_tbl = "insert into fertilizer_ref_tbl(fertilizer_name,cost_per_kg, bag_weight_kg,bag_cost_inr,n_per_bag_kg,p_per_bag_kg,k_per_bag_kg,taluka_code,user_id,activity,activity_timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

insert_fertilizer_audit_tbl = "insert into fertilizer_audit_tbl (audit_ref_id, audit_fertilizer_name, audit_cost_per_kg, audit_bag_weight_kg, audit_bag_cost_inr,audit_n_per_bag_kg, audit_p_per_bag_kg, audit_k_per_bag_kg, audit_taluka_code, audit_user_id, audit_activity,audit_activity_timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

insert_transaction_fertilizer_tbl = "insert into fertilizer_transaction_tbl (fertilizer_ID, fertilizer_name, unit_in_kg, fertilizer_qty_kgs, fertilizer_qty_bags) values (%s,%s,%s,%s,%s)"

insert_transaction_tbl = "insert into transaction_tbl (crop_name, irrigation_type_code, variety, farmer_ID, area_acre,n_soil_test, p_soil_test, k_soil_test, taluka_code, n_deficit,p_deficit, k_deficit, estimated_cost, user_id, fertilizer_ID) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

insert_nutrient_ref_tbl = "insert into nutrient_ref_tbl (crop_name,irrigation_type_code, taluka_code, n_kg_per_acre,p_kg_per_acre,k_kg_per_acre,user_id,activity,activity_timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

insert_nutrient_audit_tbl = "insert into nutrient_audit_tbl (audit_ref_id, audit_crop_name, audit_irrigation_type_code, audit_taluka_code,audit_n_kg_per_acre, audit_p_kg_per_acre, audit_k_kg_per_acre, audit_user_id,audit_activity, audit_activity_timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# insert_raitamitra_dtl_tbl = "insert into raitamitra_dtl_tbl (raitamitra_email, raitamitra_name,raitamitra_father_name, raitamitra_farmer_ID, raitamitra_mobile_number, raitamitra_gram_panchayat_code, raitamitra_village_code, raitamitra_taluka_code) values (?,?,?,?,?,?,?,?)"
