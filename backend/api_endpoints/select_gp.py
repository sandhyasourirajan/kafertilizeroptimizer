import copy;
from flask_restful import Resource;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_select_options;

class FetchGPCode(Resource):

    """

        Endpoint that is to fetch the Gram Panchayat code corresponding to the taluka code

    """

    def __init__(self):
        self.gp_json = {};
        self.temp_array = [];

    def get(self):

        # Fetch data from gp_taluka_xref_tbl
        sql = api_select_options.select_gp_code;

        g = DatabaseConnection().select_table_detail(sql=sql,params=None);

        # Convert tuple data from gp_taluka_xref_tbl to JSON array gp_json
        for i in range(len(g)):
            for j in range(3):
                if (j == 0):
                    self.gp_json["gp_code"] = g[i][j]
                if (j == 1):
                    self.gp_json["gp_name"] = g[i][j]
                if (j == 2):
                    self.gp_json["taluka_code"] = g[i][j]
                j=j+1;

            self.temp_array.append(copy.deepcopy(self.gp_json))
            i=i+1;

        gp_dtl_json = {"GP": copy.copy(self.temp_array)}

        return gp_dtl_json
