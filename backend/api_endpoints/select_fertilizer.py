import copy;
from flask_restful import Resource;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_select_options;

class FetchFertilizerDetail(Resource):

    """

        Endpoint that is called to select a fertilizer to the DB

    """

    def __init__(self):
        self.fertilizer_json = {}
        self.temp_array = []

    def get(self):

        # Fetch data from micronutrient_ref_tbl
        sql = api_select_options.select_fertilizer_ref_tbl;
        g = DatabaseConnection().select_table_detail(sql=sql,params=None);

        # Convert tuple data from fertilizer_ref_tbl to JSON array fertilizer_dtl_json
        for i in range(len(g)):
            for j in range(8):
                if (j == 0):
                    self.fertilizer_json["fertilizer_name"] = g[i][j]
                if (j == 1):
                    self.fertilizer_json["bag_weight_kg"] = g[i][j]
                if (j == 2):
                    self.fertilizer_json["bag_cost_INR"] = g[i][j]
                if (j == 3):
                    self.fertilizer_json["taluka_code"] = g[i][j]
                if (j == 4):
                    self.fertilizer_json["n_per_bag_kg"] = g[i][j]
                if (j == 5):
                    self.fertilizer_json["p_per_bag_kg"] = g[i][j]
                if (j == 6):
                    self.fertilizer_json["k_per_bag_kg"] = g[i][j]
                if (j == 7):
                    self.fertilizer_json["taluka_name"] = g[i][j]
                j=j+1;

            self.temp_array.append(copy.deepcopy(self.fertilizer_json))
            i=i+1;

        fertilizer_dtl_json = {"fertilizer": copy.copy(self.temp_array)}

        return fertilizer_dtl_json
