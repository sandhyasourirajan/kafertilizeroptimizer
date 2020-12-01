import time;
import datetime;
from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_insert_options;

class Updatetransaction(Resource):

    """

        Endpoint that is called to insert a row into the transaction table whenever the optimizer runs

    """

    input_args = {
    "crop_name": fields.Str(required=True),
    "irrigation_type_code":fields.Str(required=True),
    "variety": fields.Str(required=True),
    "farmer_ID":fields.Int(required=True),
    "area_acre":fields.Float(required=True),
    "n_soil_test":fields.Float(required=True),
    "p_soil_test":fields.Float(required=True),
    "k_soil_test":fields.Float(required=True),
    "taluka_code":fields.Int(required=True),
    "n_deficit": fields.Float(required=True),
    "p_deficit": fields.Float(required=True),
    "k_deficit": fields.Float(required=True),
    "estimated_cost": fields.Float(required=True),
    "user_id": fields.Str(required=True),
    "fertilizer_name": fields.List(fields.Str(),required=True),
    "fertilizer_bag_weight":fields.List(fields.Float(),required=True),
    "fertilizer_quantity_kg": fields.List(fields.Float(),required=True),
    "fertilizer_bag_required":fields.List(fields.Float(),required=True)
    }

    @use_args(input_args)

    def __init__(self,args):

        ###################### Inputs from API ######################

        self.crop_name = args["crop_name"];
        self.irrigation_type_code = args["irrigation_type_code"];
        self.variety = args["variety"];
        self.farmer_ID = args["farmer_ID"]
        self.area_acre = args["area_acre"]
        self.n_soil_test = args["n_soil_test"];
        self.p_soil_test = args["p_soil_test"];
        self.k_soil_test = args["k_soil_test"];
        self.taluka_code = args["taluka_code"];
        self.n_deficit = args["n_deficit"];
        self.p_deficit = args["p_deficit"];
        self.k_deficit = args["k_deficit"];
        self.user_id = args["user_id"]
        self.estimated_cost = args["estimated_cost"]
        self.fertilizer_name_list = args["fertilizer_name"]
        self.fertilizer_bag_weight_list = args["fertilizer_bag_weight"]
        self.fertilizer_quantity_kg_list = args["fertilizer_quantity_kg"]
        self.fertilizer_bag_required_list = args["fertilizer_bag_required"]

        #############################################################

        self.input_list = []
        self.fertilizer_input_list= []

    def post(self):

        ts = time.time()
        self.fertilizer_ID = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        self.input_list = [self.crop_name, self.irrigation_type_code, self.variety, self.farmer_ID,
        self.area_acre, self.n_soil_test, self.p_soil_test, self.k_soil_test, self.taluka_code,
        self.n_deficit, self.p_deficit, self.k_deficit, self.estimated_cost, self.user_id, self.fertilizer_ID]
        params = tuple(self.input_list)
        print(params)
        sql = api_insert_options.insert_transaction_tbl

        message = DatabaseConnection().insert_table_detail(sql,params)

        for i in range(0,len(self.fertilizer_name_list)):
            self.fertilizer_input_list= []
            self.fertilizer_input_list.append(self.fertilizer_ID)
            self.fertilizer_input_list.append(self.fertilizer_name_list[i]);
            self.fertilizer_input_list.append(self.fertilizer_bag_weight_list[i]);
            self.fertilizer_input_list.append(self.fertilizer_quantity_kg_list[i]);
            self.fertilizer_input_list.append(self.fertilizer_bag_required_list[i]);
            input_parm = tuple(self.fertilizer_input_list)

            sql = api_insert_options.insert_transaction_fertilizer_tbl
            message = DatabaseConnection().insert_table_detail(sql,self.fertilizer_input_list)

        return message
