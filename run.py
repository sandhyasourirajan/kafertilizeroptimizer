from webargs import fields
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_restful import Api


from backend.api_endpoints.select_region import FetchRegionDetail
from backend.api_endpoints.select_variety import FetchVariety
from backend.api_endpoints.select_gp import FetchGPCode
from backend.api_endpoints.select_user_access import FetchUserAccessInfo
from backend.api_endpoints.fertilizer_optimizer import FertilizerOptimizer
from backend.api_endpoints.select_fertilizer_region import FetchFertilizer
from backend.api_endpoints.transaction_update import Updatetransaction

from backend.api_endpoints.select_fertilizer import FetchFertilizerDetail
from backend.api_endpoints.add_fertilizer import AddFertilizer
from backend.api_endpoints.edit_fertilizer import EditFertilizer

from backend.api_endpoints.select_nutrient import FetchNutrientDetail
from backend.api_endpoints.add_nutrient import AddNutrient
from backend.api_endpoints.edit_nutrient import EditNutrient


#from backend.config.production_web_server import StandaloneApplication
#from flask_compress import Compress

import multiprocessing


def number_of_workers():

    """
        Number of threads = CPU cores + 1
        :return:
    """

    return (multiprocessing.cpu_count() * 2) + 1


app = Flask(__name__)

#Compress(app)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# =================================
#  Set up the routing here
# =================================

api.add_resource(FetchNutrientDetail, '/nutrient') ###working
api.add_resource(FetchFertilizerDetail, '/fertilizerdetail') ###working
api.add_resource(FetchFertilizer, '/fertilizer')  ###working
api.add_resource(FetchGPCode, '/gp')  ###working
api.add_resource(FertilizerOptimizer, '/optimize')
api.add_resource(FetchRegionDetail, '/region') ###working
api.add_resource(FetchVariety, '/variety')    ###working
api.add_resource(FetchUserAccessInfo, '/useraccess')  ###working
api.add_resource(AddFertilizer, '/addfertilizer')
api.add_resource(EditFertilizer, '/editfertilizer')
api.add_resource(AddNutrient, '/addnutrient')
api.add_resource(EditNutrient, '/editnutrient')
api.add_resource(Updatetransaction, '/updatetransaction')

# ====================================================================================================
#  Catch All, wild-card. For any unknown URL, just route it to Vue.JS and let it handle the 404 error
# ====================================================================================================


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

# =================================
#  Initialize the flask app.
#  1) Set the gunicorn options
#  2) Start the web-server
# =================================


if __name__ == "__main__":

    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8000'),
        'workers': number_of_workers(),
    }

    #StandaloneApplication(app, options).run()  # -- Production server (multi threaded)
    app.run(host="0.0.0.0", debug=True, threaded=True, port=8000) # -- Dev server
