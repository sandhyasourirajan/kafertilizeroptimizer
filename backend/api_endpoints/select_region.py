import copy
from flask_restful import Resource
from backend.data.database_handler import DatabaseConnection
from backend.queries import api_select_options

class FetchRegionDetail(Resource):

    """

        Endpoint that is called on page load to populate state, district and taluka.

    """

    def __init__(self):
        self.region_json = {};
        self.temp_array = [];

    def get(self):
        # Fetch data from region_dtl_tbl
        sql = api_select_options.select_region_dtl_tbl;
        g = DatabaseConnection().select_table_detail(sql=sql,params=None);

        # Convert tuple data from micronutrient_ref_tbl to JSON array micronutrient_dtl_json
        for i in range(len(g)):
            for j in range(4):
                if (j == 0):
                    self.region_json["taluka_code"] = g[i][j];
                if (j == 1):
                    self.region_json["state_name"] = g[i][j];
                if (j == 2):
                    self.region_json["district_name"] = g[i][j];
                if (j == 3):
                    self.region_json["taluka_name"] = g[i][j];
                j=j+1;

            self.temp_array.append(copy.deepcopy(self.region_json));
            i=i+1;

        region_dtl_json = {"region_dtl": copy.copy(self.temp_array)};

        return region_dtl_json
