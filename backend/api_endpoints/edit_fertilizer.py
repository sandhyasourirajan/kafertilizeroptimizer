from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_select_options, api_insert_options, api_update_options;

class EditFertilizer(Resource):

    """

        Endpoint that is called to edit the details of an existing fertilizer

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
        self.activity = "edit"

    def post(self):

        # Add a row to audit history table before inserting into fertilizer table

        sql = api_select_options.select_fertilizer_edits;
        # .format(self.fertilizer_name,self.taluka_code);
        params = {
        "fertilizer_name": self.fertilizer_name,
        "taluka_code": self.taluka_code
        }
        g = DatabaseConnection().select_table_detail(sql,params);
        print(g)

        self.input_list = [g[0][0], g[0][1], g[0][2],g[0][3],g[0][4],g[0][5],g[0][6],g[0][7],g[0][8],g[0][9],g[0][10],g[0][11]]
        print(self.input_list)
        audit_input_parm = tuple(self.input_list)
        print(audit_input_parm)
        sql = api_insert_options.insert_fertilizer_audit_tbl

        DatabaseConnection().insert_table_detail(sql,audit_input_parm)

        # Edit existing row in fertilizer_ref_tbl after adding detail into audit table

        self.cost_per_kg = self.bag_cost_INR / self.bag_weight_kg

        sql = api_update_options.update_fertilizer_ref_tbl
        self.input_list = []
        self.input_list = [self.cost_per_kg, self.bag_weight_kg, self.bag_cost_INR, self.n_per_bag_kg, self.p_per_bag_kg, self.k_per_bag_kg, self.user_id, self.activity, self.fertilizer_name, self.taluka_code]
        ref_input_parm = tuple(self.input_list)

        message = DatabaseConnection().update_table_detail(sql,ref_input_parm)

        return message
