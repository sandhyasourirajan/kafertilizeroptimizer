import copy;
import numpy as np;
from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection;
from backend.queries import api_select_options;
from backend.optimization import linear;

class FertilizerOptimizer(Resource):

    """

        Endpoint that is called after deficit N,P,K calculation to suggest fertilizer based on N,P,K

    """

    input_args = {
    'N_deficit':fields.Int(required=True),
    'P_deficit':fields.Int(required=True),
    'K_deficit':fields.Int(required=True),
    'fertilizer_name':fields.List(fields.Str(),required=True),
    'taluka_code':fields.Int(required=True)
    }

    @use_args(input_args)

    def __init__(self,args):

        self.fertilizer_json = {};
        self.npk_json = {};
        self.temp_array = [];

        ###################### Inputs from API ######################

        self.fertilizer_name = args["fertilizer_name"];
        self.taluka_code = args["taluka_code"];

        #optimizer variables - constraint for N,P,K calculation
        self.N_deficit = args["N_deficit"];
        self.P_deficit = args["P_deficit"];
        self.K_deficit = args["K_deficit"];
        #############################################################

        #N,P,K composition for each fertilizer
        self.N_qty_per_bag = [];
        self.P_qty_per_bag = [];
        self.K_qty_per_bag = [];

        self.fertilizer_bag_cost = [];
        self.fertilizer_bag_weight = [];

    def post(self):

        self.temp_array = []

        fertilizer_name_list = []
        sql = api_select_options.select_fertilizer_npk
        params = tuple(self.fertilizer_name)

        npk_output = DatabaseConnection().select_table_detail(sql,(params,))

        for i in range(len(npk_output)):
            for j in range(6):

                if (j == 0):
                    self.N_qty_per_bag.append(npk_output[i][j])
                if (j == 1):
                    self.P_qty_per_bag.append(npk_output[i][j])
                if (j == 2):
                    self.K_qty_per_bag.append(npk_output[i][j])
                if (j == 3):
                    fertilizer_name_list.append(npk_output[i][j])
                if (j == 4):
                    self.fertilizer_bag_weight.append(npk_output[i][j])
                if (j == 5):
                    self.fertilizer_bag_cost.append(npk_output[i][j])
                j=j+1;

            i=i+1;

        order = len(self.fertilizer_name)

        fertilizer_bag_required = np.zeros(order)
        optimized_output = linear.optimize_minimize(self.N_deficit,self.P_deficit,self.K_deficit,fertilizer_bag_required,self.fertilizer_bag_cost,fertilizer_name_list,self.N_qty_per_bag, self.P_qty_per_bag, self.K_qty_per_bag,self.fertilizer_bag_weight)
        final_output = {"optimized_output": optimized_output}

        return final_output
