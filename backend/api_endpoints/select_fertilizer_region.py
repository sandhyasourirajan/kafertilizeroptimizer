import copy
from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection
from backend.queries import api_select_options

class FetchFertilizer(Resource):

    """

        Endpoint that is called after deficit N,P,K calculation to suggest fertilizer based on N,P,K

    """

    input_args = {
    'taluka_code':fields.Int(required=True)
    }

    @use_args(input_args)


    def __init__(self,args):
        self.fertilizer_json = {};
        self.temp_array = [];
        self.taluka_code = args["taluka_code"]
        self.params = {"taluka_code": self.taluka_code}
        
    def post(self):

        # Fetch data from micronutrient_ref_tbl
        sql = api_select_options.select_fertilizer.format(self.taluka_code);
        g = DatabaseConnection().select_table_detail(sql=sql,params=self.params);

        # Convert tuple data from fertilizer_ref_tbl to JSON array fertilizer_dtl_json
        for i in range(len(g)):
            for j in range(3):
                if (j == 0):
                    self.fertilizer_json["fertilizer_name"] = g[i][j]
                if (j == 1):
                    self.fertilizer_json["bag_weight_kg"] = g[i][j]
                if (j == 2):
                    self.fertilizer_json["bag_cost_INR"] = g[i][j]
                j=j+1;

            self.temp_array.append(copy.deepcopy(self.fertilizer_json))
            i=i+1;

        fertilizer_dtl_json = {"fertilizer": copy.copy(self.temp_array)}

        return fertilizer_dtl_json
