import copy
from flask_restful import Resource;
from backend.data.database_handler import DatabaseConnection
from backend.queries import api_select_options

class FetchUserAccessInfo(Resource):

    """

        Endpoint that is called for check the access priveleges of a user

    """

    def __init__(self):
        self.user_access_json = {};
        self.temp_array = [];

    def get(self):
        # Fetch data from region_dtl_tbl
        sql = api_select_options.select_user_access;
        g = DatabaseConnection().select_table_detail(sql=sql,params=None);

        # Convert tuple data from micronutrient_ref_tbl to JSON array micronutrient_dtl_json
        for i in range(len(g)):
            for j in range(2):
                if (j == 0):
                    self.user_access_json["email_ID"] = g[i][j];
                if (j == 1):
                    self.user_access_json["user_access"] = g[i][j];
                j=j+1;

            self.temp_array.append(copy.deepcopy(self.user_access_json));
            i=i+1;

        user_access_json = {"user_access": copy.copy(self.temp_array)};

        return user_access_json
