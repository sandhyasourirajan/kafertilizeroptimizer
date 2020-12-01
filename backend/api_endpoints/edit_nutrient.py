from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_select_options, api_insert_options, api_update_options;

class EditNutrient(Resource):

    """

        Endpoint that is called to edit the details of an existing nutrient detail

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
        self.activity = "edit"

        self.params = { "crop_name":self.crop_name,
                        "irrigation_type_code":self.irrigation_type_code,
                        "taluka_code":self.taluka_code
                        }

    def post(self):

        # Add a row to audit history table before inserting into nutrient dtl table

        sql = api_select_options.select_nutrient_edits;
        g = DatabaseConnection().select_table_detail(sql=sql,params=self.params);
        self.input_list = [g[0][0], g[0][1], g[0][2],g[0][3],g[0][4],g[0][5],g[0][6],g[0][7],g[0][8],g[0][9]]

        audit_input_parm = tuple(self.input_list)
        sql = api_insert_options.insert_nutrient_audit_tbl

        DatabaseConnection().insert_table_detail(sql,audit_input_parm)

        # Edit existing row in nutrient_ref_tbl after adding detail into audit table
        sql = api_update_options.update_nutrient_ref_tbl
        self.input_list = []
        self.input_list = [self.n_kg_per_acre, self.p_kg_per_acre, self.k_kg_per_acre, self.user_id, self.activity,self.crop_name, self.irrigation_type_code]
        ref_input_parm = tuple(self.input_list)

        message = DatabaseConnection().update_table_detail(sql,ref_input_parm)

        return message
