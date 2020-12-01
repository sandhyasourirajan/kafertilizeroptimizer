import copy
from flask_restful import Resource
from backend.data.database_handler import DatabaseConnection
from backend.queries import api_select_options

class FetchNutrientDetail(Resource):

    """

        Endpoint that is called on page load to populate crop/nutrient details.

    """

    def __init__(self):
        self.nutrient_json = {};
        self.temp_array = [];


    def get(self):
        # Fetch data from nutrient_ref_tbl
        sql = api_select_options.select_nutrient_ref_tbl;
        g = DatabaseConnection().select_table_detail(sql=sql,params=None);

        # Convert tuple data from nutrient_ref_tbl to JSON array nutrient_dtl_json
        for i in range(len(g)):
            for j in range(7):
                if (j == 0):
                    self.nutrient_json["crop_name"] = g[i][j];
                if (j == 1):
                    self.nutrient_json["irrigation_type_code"] = g[i][j];
                if (j == 2):
                    self.nutrient_json["n_kg_per_acre"] = g[i][j];
                if (j == 3):
                    self.nutrient_json["p_kg_per_acre"] = g[i][j];
                if (j == 4):
                    self.nutrient_json["k_kg_per_acre"] = g[i][j];
                if (j == 5):
                    self.nutrient_json["taluka_code"] = g[i][j];
                if (j == 6):
                    self.nutrient_json["taluka_name"] = g[i][j];
                j=j+1;

            self.temp_array.append(copy.deepcopy(self.nutrient_json));
            i=i+1;

        nutrient_dtl_json = {"nutrient": copy.copy(self.temp_array)};

        return nutrient_dtl_json
