import datetime;
import time;
from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_insert_options

class AddNutrient(Resource):

    """

        Endpoint that is called to add a new nutrient detail to the DB

    """

    input_args = {
    'crop_name':fields.Str(required=True),
    'irrigation_type_code':fields.Str(required=True),
    'taluka_code':fields.Int(required=True),
    'n_kg_per_acre':fields.Float(required=True),
    'p_kg_per_acre':fields.Float(required=True),
    'k_kg_per_acre':fields.Float(required=True),
    'user_id':fields.Str(required=True)
    }

    @use_args(input_args)

    def __init__(self,args):

        ###################### Inputs from API ######################

        self.crop_name = args["crop_name"];
        self.irrigation_type_code = args["irrigation_type_code"];
        self.taluka_code = args["taluka_code"];
        self.n_kg_per_acre = args["n_kg_per_acre"]
        self.p_kg_per_acre = args["p_kg_per_acre"]
        self.k_kg_per_acre = args["k_kg_per_acre"]
        self.user_id = args["user_id"]

        #############################################################

        self.input_list = []
        self.activity = "insert"

    def post(self):

        # Insert a new nutrient detail into the nutrient_ref_tbl

        ts = time.time()
        self.activity_timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        self.input_list = [self.crop_name, self.irrigation_type_code, self.taluka_code,self.n_kg_per_acre, self.p_kg_per_acre,self.k_kg_per_acre, self.user_id, self.activity,self.activity_timestamp]

        input_parm = tuple(self.input_list)

        sql = api_insert_options.insert_nutrient_ref_tbl

        message = DatabaseConnection().insert_table_detail(sql,input_parm)

        return message
