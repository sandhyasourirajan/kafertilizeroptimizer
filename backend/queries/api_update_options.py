
update_fertilizer_ref_tbl = '''update fertilizer_ref_tbl set cost_per_kg = %s, bag_weight_kg = %s, bag_cost_INR = %s, n_per_bag_kg = %s, p_per_bag_kg = %s, k_per_bag_kg = %s, user_id = %s, activity = %s where  fertilizer_name = %s and taluka_code= %s'''

update_nutrient_ref_tbl = '''update nutrient_ref_tbl set N_kg_per_acre = %s, P_kg_per_acre = %s, K_kg_per_acre = %s, user_id = %s, activity = %s where  crop_name = %s and irrigation_type_code= %s'''
