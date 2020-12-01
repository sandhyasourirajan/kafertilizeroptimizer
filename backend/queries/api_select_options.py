select_nutrient_ref_tbl = """select n.crop_name, n.irrigation_type_code, n.n_kg_per_acre, n.p_kg_per_acre, n.k_kg_per_acre, s.taluka_code, s.taluka_name
from  nutrient_ref_tbl n join
	  state_taluka_xref_tbl s
	on n.taluka_code = s.taluka_code;"""

select_fertilizer_ref_tbl = """select f.fertilizer_name, f.bag_weight_kg, f.bag_cost_INR, s.taluka_code, f.n_per_bag_kg, f.p_per_bag_kg, f.k_per_bag_kg, s.taluka_name
from 	fertilizer_ref_tbl f join
		state_taluka_xref_tbl s
		on f.taluka_code = s.taluka_code;"""

select_fertilizer =  """select fertilizer_name, bag_weight_kg, bag_cost_INR from fertilizer_ref_tbl where taluka_code = (%(taluka_code)s)"""

select_region_dtl_tbl = """select taluka_code, state_name, district_name, taluka_name from state_taluka_xref_tbl"""

select_fertilizer_npk = "select n_per_bag_kg, p_per_bag_kg, k_per_bag_kg,fertilizer_name,bag_weight_kg, bag_cost_INR from fertilizer_ref_tbl where fertilizer_name in %s order by fertilizer_name"

select_fertilizer_edits = "select ref_id, fertilizer_name, cost_per_kg, bag_weight_kg, bag_cost_INR, n_per_bag_kg, p_per_bag_kg, k_per_bag_kg,taluka_code, user_id, activity, activity_timestamp from fertilizer_ref_tbl where fertilizer_name = (%(fertilizer_name)s) and taluka_code = (%(taluka_code)s)"

select_variety =  """select variety_name from crop_variety_ref_tbl where crop_name = (%(crop_name)s)"""

select_nutrient_edits = "select ref_id, crop_name, irrigation_type_code, taluka_code,n_kg_per_acre, p_kg_per_acre, k_kg_per_acre, user_id, activity, activity_timestamp from nutrient_ref_tbl where crop_name = (%(crop_name)s) and irrigation_type_code = (%(irrigation_type_code)s) and taluka_code = (%(taluka_code)s)"

select_gp_code = "select gp_code, gp_name, taluka_code from gp_taluka_xref_tbl;"

select_user_access = "select email_ID, user_access from user_access_tbl;"

# select_region_dtl = """select taluka_code, GP_code, village_code from region_dtl"""
