import datetime;
import time;
from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_insert_options

class AddFertilizer(Resource):

    """

        Endpoint that is called to add a new fertilizer to the DB

    """

    input_args = {
    'fertilizer_name':fields.Str(required=True),
    'bag_weight_kg':fields.Float(required=True),
    'bag_cost_INR':fields.Int(required=True),
    'n_per_bag_kg':fields.Float(required=True),
    'p_per_bag_kg':fields.Float(required=True),
    'k_per_bag_kg':fields.Float(required=True),
    'taluka_code':fields.Int(required=True),
    'user_id':fields.Str(required=True)
    }

    @use_args(input_args)

    def __init__(self,args):

        ###################### Inputs from API ######################

        self.fertilizer_name = args["fertilizer_name"];
        self.bag_weight_kg = args["bag_weight_kg"];
        self.bag_cost_INR = args["bag_cost_INR"]
        self.n_per_bag_kg = args["n_per_bag_kg"]
        self.p_per_bag_kg = args["p_per_bag_kg"]
        self.k_per_bag_kg = args["k_per_bag_kg"]
        self.taluka_code = args["taluka_code"]
        self.user_id = args["user_id"]

        #############################################################
        self.cost_per_kg = 0
        self.input_list = []
        self.activity = "insert"

    def post(self):

        # Insert a new fertilizer into the fertilizer_ref_tbl
        ts = time.time()
        self.activity_timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        self.cost_per_kg = self.bag_cost_INR / self.bag_weight_kg

        self.input_list = [self.fertilizer_name, self.cost_per_kg, self.bag_weight_kg, self.bag_cost_INR,self.n_per_bag_kg,self.p_per_bag_kg,self.k_per_bag_kg,self.taluka_code,self.user_id, self.activity,self.activity_timestamp]

        input_parm = tuple(self.input_list)

        sql = api_insert_options.insert_fertilizer_ref_tbl

        message = DatabaseConnection().insert_table_detail(sql,input_parm)

        return message
