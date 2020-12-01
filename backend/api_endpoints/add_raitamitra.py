from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_insert_options

class AddRaitamitra(Resource):

    """

        Endpoint that is called to add a new Raitamitra to the DB

    """

    input_args = {
    'raitamitra_email':fields.Str(required=True),
    'raitamitra_name':fields.Str(required=True),
    'raitamitra_father_name':fields.Str(required=True),
    'raitamitra_farmer_ID':fields.Int(required=True),
    'raitamitra_mobile_number':fields.Int(required=True),
    'raitamitra_gram_panchayat_code':fields.Int(required=True),
    'raitamitra_village_code':fields.Int(required=True),
    'raitamitra_taluka_code':fields.Int(required=True)
    }

    @use_args(input_args)

    def __init__(self,args):

        ###################### Inputs from API ######################

        self.raitamitra_email = args["raitamitra_email"];
        self.raitamitra_name = args["raitamitra_name"];
        self.raitamitra_father_name = args["raitamitra_father_name"]
        self.raitamitra_farmer_ID = args["raitamitra_farmer_ID"]
        self.raitamitra_mobile_number = args["raitamitra_mobile_number"]
        self.raitamitra_gram_panchayat_code = args["raitamitra_gram_panchayat_code"]
        self.raitamitra_village_code = args["raitamitra_village_code"]
        self.raitamitra_taluka_code = args["raitamitra_taluka_code"]

        #############################################################

        self.input_list = []
        self.activity = "insert"

    def post(self):

        # Insert a new raitamitra into the raitamitra_dtl_tbl

        self.input_list = [self.raitamitra_email, self.raitamitra_name, self.raitamitra_father_name, self.raitamitra_farmer_ID,self.raitamitra_mobile_number, self.raitamitra_gram_panchayat_code,self.raitamitra_village_code, self.raitamitra_taluka_code ]

        input_parm = tuple(self.input_list)

        sql = api_insert_options.insert_raitamitra_dtl_tbl

        message = DatabaseConnection().insert_table_detail(sql,input_parm)

        return message
