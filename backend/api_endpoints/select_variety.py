from flask_restful import Resource;
from webargs import fields;
from webargs.flaskparser import use_args;
from backend.data.database_handler import DatabaseConnection
from backend.queries import api_select_options

class FetchVariety(Resource):

    """

        Endpoint that is called for selection of variety for a given crop

    """

    input_args = {
                'crop_name':fields.Str(required=True),
                }

    @use_args(input_args)

    def __init__(self,args):

        self.crop_name = args["crop_name"];
        self.params = {"crop_name":self.crop_name}
        self.variety_list = []

    def post(self):

        # Fetch data from crop_variety_ref_tbl for a given crop
        sql = api_select_options.select_variety;
        g = DatabaseConnection().select_table_detail(sql=sql,params=self.params);

        # Convert tuple data from crop_variety_ref_tbl to list
        for i in range(len(g)):
            self.variety_list.append(g[i][0])
            i=i+1;

        self.variety_list.append('Local')
        self.variety_list.append('Others')

        return self.variety_list
