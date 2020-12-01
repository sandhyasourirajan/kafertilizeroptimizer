<template>
    <div class="fo-english"> <br>

      <v-btn primary color="grey" style="margin:auto; display:block;border:2px solid black;width:100%" @click="help_guide"> Click here for a self starter guide </v-btn>

      <h2 class="text-md-center"> INPUT SECTION </h2>

      <div class="input-section" v-intro-step="1" v-intro="'Welcome to Fertilizer Optimizer. This is a native application to suggest the most optimal fertilizer combination for an input crop-irrigation type combination and soil conditions. Click Next to proceed further with the Getting Started Guide.'">

        <v-layout row  v-intro-step="2" v-intro="'Select the state, district, taluka and Panchayat of the farmer from the dropdown'">
          <v-flex md6>
            <v-flex md10>
              <v-select :items="state_select" :rules="[() => !!selected_state || 'This field is required']" v-model="selected_state" label="Select the state" required></v-select>
              Selected state: <span  class="highlight-input">  {{selected_state}} </span> <br><br>
            </v-flex>
          </v-flex>

          <v-flex md6>
            <v-flex md10>
              <v-select :items="district_select" :rules="[() => !!selected_district || 'This field is required']" v-model="selected_district" label="Select the district" required></v-select>
              Selected district: <span  class="highlight-input">  {{selected_district}} </span> <br><br>
            </v-flex>
          </v-flex>
          </v-layout>

          <v-layout row  v-intro-step="2" v-intro="'Select the state, district, taluka and Panchayat of the farmer from the dropdown'">
          <v-flex md6>
            <v-flex md10>
              <v-select :items="taluka_select" :rules="[() => !!selected_taluka || 'This field is required']" v-model="selected_taluka" label="Select the taluka" required></v-select>
              Selected taluka: <span  class="highlight-input">  {{selected_taluka}} </span> <br><br>
            </v-flex>
          </v-flex>

          <v-flex md6>
            <v-flex md10>
              <v-select :items="panchayat_select" :rules="[() => !!selected_panchayat || 'This field is required']" v-model="selected_panchayat" label="Select the Panchayat Code" required></v-select>
              Selected Panchayat: <span  class="highlight-input">  {{panchayat_code}}  - {{panchayat_name}}</span> <br><br>
            </v-flex>
          </v-flex>
        </v-layout>

          <v-layout row>
              <v-flex md6>
                <div class="select-crop" v-intro-step="3" v-intro="'Select the crop name from this dropdown.'">
                  <v-flex md8>
                    <v-select :items="crop_select" :rules="[() => !!selected_crop || 'This field is required']" v-model="selected_crop" label="Select a crop" required></v-select>
                    Selected crop is <span  class="highlight-input">  {{selected_crop}} </span>
                  </v-flex>
                </div>
              </v-flex>

              <v-flex md6>
                <div class="select-irrigation-type" v-intro-step="4" v-intro="'Select whether the crop is being irrigated or rainfed using this dropdown.'">
                  <v-flex md8>
                    <v-select :items="irrigation_type_select" :rules="[() => !!selected_irrigation_type || 'This field is required']" v-model="selected_irrigation_type" label="Select an irrigation type code" required></v-select>
                    Selected irrigation type code is <span  class="highlight-input">  {{selected_irrigation_type}} </span>
                  </v-flex>
                </div>
              </v-flex>
          </v-layout>

          <v-layout row v-intro-step="5" v-intro="'Select the Variety of the crop from the dropdown. If the variety name is not available in dropdown, choose Other in dropdown and enter the variety name as input text.'">

              <v-flex md6>
                <v-flex md8>
                  <v-select :items="variety_list" :rules="[() => !!selected_variety || 'This field is required']" v-model="selected_variety" label="Select the variety" required></v-select>
                  Variety entered by you is <span  class="highlight-input"> {{variety_text}} </span> </p>

                </v-flex>
              </v-flex>

              <v-flex md6>
                <v-flex md8>
                  <div id="enable-text-box" v-if="selected_variety === 'Others'">
                    <v-text-field v-model.number="variety_text" label="Enter the variety of the crop" v-on:keyup="update_variety()"></v-text-field>
                  </div>
                  <br> <br>
                </v-flex>
              </v-flex>
          </v-layout>

          <v-layout row>
              <v-flex md6>
                <div class="farmer-ID" v-intro-step="6" v-intro="'Enter the farmer ID# for whom this query is being carried out'">
                  <v-flex md8>
                    Farmer ID: <br> <input type="text" v-model="taluka_code" size="1" readonly> - <input type="text" v-model="panchayat_code" size="1" readonly> -
                    <input id="farmer_ID" type="text" placeholder="000" v-model="farmer_ID_number" v-on:keyup="capture_farmer_details" size="1" maxlength="3"/> <br>
                    Farmer ID entered by you is <span  class="highlight-input">  {{farmer_ID}} </span>
                  </v-flex>
                </div>
              </v-flex>

              <v-flex md6>
                <v-flex md8 v-intro-step="7" v-intro="'Enter the area of the farmland in acres'">
                  Area in acres: <input id="area_acre" type="number" placeholder="0" v-model="area_acre" v-on:keyup="fertilizer_calc()" style="width:300px"/> <br>
                  Area of land entered by you is <span  class="highlight-input"> {{area_acre}} acre(s) </span>
                </v-flex>
              </v-flex>
          </v-layout>

          <v-layout row  v-intro-step="9" v-intro="'Enter the N,P,K values from the soil test results carried out in the farmland'">
              <v-flex md4>
                <v-flex md10>
                  Soil test results:
                  Nitrogen   (N): <input id="NPK_soil_test_result.N_soil_test_result" type="number" step= ".1" placeholder="0.0" v-model="NPK_soil_test_result.N_soil_test_result" v-on:keyup="update_N_deficit" style="width:75px"/> kg/ha &nbsp
                </v-flex>
              </v-flex>

              <v-flex md4>
                <v-flex md10>
                  Phosphorus (P): <input id="NPK_soil_test_result.P_soil_test_result" type="number" step=".1" placeholder="0.0" v-model="NPK_soil_test_result.P_soil_test_result" v-on:keyup="update_P_deficit" style="width:75px"/> kg/ha &nbsp
                </v-flex>
              </v-flex>

              <v-flex md4>
                <v-flex md10>
                  Potassium  (K): <input id="NPK_soil_test_result.K_soil_test_result" type="number" step=".1" placeholder="0.0" v-model="NPK_soil_test_result.K_soil_test_result" v-on:keyup="update_K_deficit" style="width:75px"/> kg/ha
                </v-flex>
              </v-flex>
          </v-layout>

          <br><br>

          <v-layout row>
              <v-flex md12  v-intro-step="10" v-intro="'Click this button to compute N,P,K deficit and optimized fertilizer '">
                <div class="text-md-center">
                  <a href="#n-p-k-calc">
                    <v-btn round justify-center color="primary" @click.native="process_inputs()" :disabled="disable_button_inputs"><v-icon> pie_chart </v-icon>   Generate N,P,K statistics </v-btn>
                  </a>
                </div>
              </v-flex>
          </v-layout>

        <br>
      </div>

      <h2 class="text-md-center"> N,P,K CALCULATION </h2>

      <div id="n-p-k-calc" class="n-p-k-calc-section"> <br>
          <p> Fertilizer requirement for crop/irrigation type selected per acre
              N: <span  class="highlight-input"> {{ NPK_kg_per_acre.n_kg_per_acre}} </span> &nbsp kg/acre &nbsp &nbsp
              P: <span  class="highlight-input"> {{ NPK_kg_per_acre.p_kg_per_acre}} </span> &nbsp kg/acre &nbsp &nbsp
              K: <span  class="highlight-input"> {{ NPK_kg_per_acre.k_kg_per_acre}} </span> &nbsp kg/acre
          </p>

          <v-layout row wrap >
            <v-flex md6>
              <v-card style="background-color:#bcbec0;color:#B11117">
                Total Fertilizer requirement for crop/irrigation type selected for <span class="highlight-input"> {{area_acre}} acre(s) </span> <br>
                N: <span  class="highlight-input"> {{ NPK_total.N_total}} </span> &nbsp kg/acre &nbsp &nbsp
                P: <span  class="highlight-input"> {{ NPK_total.P_total}} </span>  &nbsp kg/acre &nbsp &nbsp
                K: <span  class="highlight-input"> {{ NPK_total.K_total}} </span>  &nbsp kg/acre <br>
              </v-card>
            </v-flex>

            <v-flex md6>
              <v-card style="background-color:#bcbec0;color:#B11117">
                N,P,K fertilization further required for your soil based on your soil test result: <br>
                N: <span  class="highlight-input"> {{ NPK_deficit.N_deficit  }} </span> &nbsp kg  &nbsp
                P: <span  class="highlight-input"> {{ NPK_deficit.P_deficit }} </span> &nbsp kg  &nbsp
                K: <span  class="highlight-input"> {{ NPK_deficit.K_deficit }} </span> <br>
              </v-card>
            </v-flex>
          </v-layout>
      </div>

      <div class="text-md-center">
          <v-btn round justify-center :to="{name: 'FertilizerOptimizer'}" :disabled="disable_button_next"> NEXT </v-btn>
      </div> <br>
    </div>
</template>

<script>
import 'intro.js/introjs.css';
import _ from 'lodash';
import API from '../reducers/API'

  export default {
    name: 'FOEnglish',
    data () {
      return {
        language:'',
        // Fields entered or selected in the App
        selected_crop:'',
        selected_irrigation_type:'',
        selected_variety:'',
        variety_text:'',
        farmer_ID:0,
        farmer_ID_number:0,
        area_acre:0,
        taluka_code:0,
        selected_state:'',
        selected_district:'',
        selected_taluka:'',
        selected_panchayat:0,
        panchayat_name:'',
        panchayat_code:'',
        gp_name_list:[],
        gp_code_list:[],
        NPK_soil_test_result:{
          N_soil_test_result:0.0,
          P_soil_test_result:0.0,
          K_soil_test_result:0.0
        },
        // API result
        region_dtl_json:{},
        nutrient_dtl_json:{},
        nutrient_dtl_dump:{},
        // Temporary variables
        variety_list:[],
        disable_button_inputs:true,
        disable_button_next:true,
        NPK_kg_per_acre:{
          n_kg_per_acre:0,
          p_kg_per_acre:0,
          k_kg_per_acre:0
        },
        NPK_total:{
          N_total:0,
          P_total:0,
          K_total:0
        },
        NPK_deficit:{
          N_deficit:0,
          P_deficit:0,
          K_deficit:0
        }
      }
    },

    created : function () {

    this.language = this.$store.selected_language;

    // Call the API to fetch the nutrient details from the DB
      API.fetchNutrientData()
       .then(nutrient_info => {
         this.nutrient_dtl_dump = nutrient_info.nutrient
        })
       .catch(error => {
         console.error(error);
        })

      // Call the API to fetch the state, district and taluka details
      API.fetchRegionData()
         .then(region_info => {
            this.region_dtl_json = region_info.region_dtl
          })
         .catch(error => {
            console.error(error);
          })

      // Call the API to fetch the nutrient details from the DB
      API.fetchGPData()
           .then(gp_info => {
              this.gp_dtl_json = gp_info.GP
            })
            .catch(error => {
              console.error(error);
            })
      this.$store.api.region_dtl_json = this.region_dtl_json;
      this.$store.api.nutrient_dtl_json = this.nutrient_dtl_dump;
      },

      mounted : function(){
        // Set total NPK, deficit NPK, crop NPK to default
        this.$store.selects.NPK_total = {}
        this.$store.selects.NPK_deficit = {}
        this.$store.selects.NPK_kg_per_acre = {}
        this.$store.selects.NPK_soil_test_result = {}
      },
    methods:{
      help_guide(){
        this.$intro().start();
      },
      update_variety(){
        if (this.selected_variety == 'Others'){
            this.$store.selects.variety = this.variety_text;
        } else{
            this.variety_text = this.selected_variety;
            this.$store.selects.variety = this.variety_text;
        }
      },
      fertilizer_calc(){
        if (this.area_acre > 0){
          // var g = this.$store.api.nutrient_dtl_json;
          var o = _.filter(this.nutrient_dtl_json,{"crop_name": this.$store.selects.crop_name,
                              "irrigation_type_code": this.$store.selects.irrigation_type_code,
                              "taluka_code":this.taluka_code
                            });

          this.NPK_kg_per_acre.n_kg_per_acre = o[0].n_kg_per_acre;
          this.NPK_kg_per_acre.p_kg_per_acre = o[0].p_kg_per_acre;
          this.NPK_kg_per_acre.k_kg_per_acre = o[0].k_kg_per_acre;

          this.$store.selects.area_acre = this.area_acre;
          this.$store.selects.NPK_total.N_total = this.area_acre * o[0].n_kg_per_acre;
          this.$store.selects.NPK_total.P_total = this.area_acre * o[0].p_kg_per_acre;
          this.$store.selects.NPK_total.K_total = this.area_acre * o[0].k_kg_per_acre;
          this.NPK_total = this.$store.selects.NPK_total
          this.validate_inputs()
          }
      },
      capture_farmer_details(){
        this.farmer_ID_number = Number(this.farmer_ID_number)
        if (isNaN(this.farmer_ID_number)){
          alert("Please verify the farmer ID input - It should be numeric")
        } else {
          this.farmer_ID = Number("" + this.taluka_code + this.panchayat_code + this.farmer_ID_number);
          this.$store.selects.farmer_ID = this.farmer_ID
        }

      },
      update_N_deficit(){
        this.NPK_deficit.N_deficit = this.NPK_total.N_total - (this.NPK_soil_test_result.N_soil_test_result * 0.4047);
        if (this.NPK_deficit.N_deficit < 0){
          this.NPK_deficit.N_deficit = 0
        }
        this.$store.selects.NPK_soil_test_result = this.NPK_soil_test_result
        this.$store.selects.NPK_deficit.N_deficit = this.NPK_deficit.N_deficit
      },
      update_P_deficit(){
        this.NPK_deficit.P_deficit = this.NPK_total.P_total - (this.NPK_soil_test_result.P_soil_test_result  * 0.4047);
        if (this.NPK_deficit.P_deficit < 0){
          this.NPK_deficit.P_deficit = 0
        }
        this.$store.selects.NPK_deficit.P_deficit = this.NPK_deficit.P_deficit
      },
      update_K_deficit(){
        this.NPK_deficit.K_deficit = this.NPK_total.K_total - (this.NPK_soil_test_result.K_soil_test_result  * 0.4047);
        if (this.NPK_deficit.K_deficit < 0){
          this.NPK_deficit.K_deficit = 0
        }
        this.$store.selects.NPK_deficit.K_deficit = this.NPK_deficit.K_deficit
      },
      validate_inputs(){
      if (!(this.selected_taluka)|| !(this.panchayat_code) || (this.area_acre <= 0) ||
      !(this.selected_irrigation_type) || !(this.variety_text) || (this.farmer_ID <= 101001)){
            this.disable_button_inputs = true;
          } else{
            this.disable_button_inputs = false;
          }
      },
      process_inputs(){
        if (this.NPK_soil_test_result.N_soil_test_result == 0 || this.NPK_soil_test_result.N_soil_test_result == null) {
          this.$store.selects.NPK_soil_test_result.N_soil_test_result = this.NPK_soil_test_result.N_soil_test_result = 0
          this.update_N_deficit()
        }
        if (this.NPK_soil_test_result.P_soil_test_result == 0 || this.NPK_soil_test_result.P_soil_test_result == null) {
          this.$store.selects.NPK_soil_test_result.P_soil_test_result = this.NPK_soil_test_result.P_soil_test_result = 0
          this.update_P_deficit()
        }
        if (this.NPK_soil_test_result.K_soil_test_result == 0 || this.NPK_soil_test_result.K_soil_test_result == null) {
          this.$store.selects.NPK_soil_test_result.K_soil_test_result = this.NPK_soil_test_result.K_soil_test_result = 0
          this.update_K_deficit()
        }

        if ((this.NPK_deficit.N_deficit <= 0 )
        && (this.NPK_deficit.P_deficit <= 0 )
        && (this.NPK_deficit.K_deficit <= 0)){
          this.disable_button_next = true;
        } else{
          this.disable_button_next = false;
        }
      }
    },

    computed: {
      crop_select: function(){
        var crop_name_list = []
        for (var i=0;i<this.nutrient_dtl_json.length;i++){
          crop_name_list.push(this.nutrient_dtl_json[i].crop_name)
          }
        return Array.from(new Set(crop_name_list))
      },
      irrigation_type_select: function(){
        //get the irrigation type for the given crop name
        var o = _.filter(this.nutrient_dtl_json,{'crop_name': this.$store.selects.crop_name});
        var irrigation_type_list = _.map(o,'irrigation_type_code')
        for (var i=0;i< irrigation_type_list.length;i++){
          if(irrigation_type_list[i] == 'I'){
            irrigation_type_list[i] = "Irrigated"
          }
          if(irrigation_type_list[i] == 'R'){
            irrigation_type_list[i] = "Rainfed"
          }
        }
        return irrigation_type_list
      },
      state_select: function(){
        var state_list = []
        for (var i=0;i<this.region_dtl_json.length;i++){
          state_list.push(this.region_dtl_json[i].state_name)
          }
        return Array.from(new Set(state_list))
      },
      district_select: function(){
        //get the irrigation type for the given crop name
        var o = _.filter(this.region_dtl_json,{'state_name': this.selected_state});
        var district_list = _.map(o,'district_name')
        return district_list
      },
      taluka_select: function(){
        //get the irrigation type for the given crop name
        var o = _.filter(this.region_dtl_json,{'state_name': this.selected_state,'district_name':this.selected_district});
        var taluka_list = _.map(o,'taluka_name')
        return taluka_list
      },
      panchayat_select: function(){
        //get the Panchayat for the selected taluka
        var o = _.filter(this.gp_dtl_json,{'taluka_code': this.taluka_code});
        this.gp_name_list = _.map(o,'gp_name')
        this.gp_code_list = _.map(o,'gp_code')
        return this.gp_code_list
      },
      zero_pad:function(val){
        var num = val + "";
        num = "0" + num;
        return num
      }
    },
    watch:{
      selected_crop: function(val){
        this.$store.selects.crop_name = val
        var args = {"crop_name":val}

        API.fetchVariety(args)
        .then(variety_list => {this.variety_list = variety_list})
        .catch(error => {
        console.error(error);
        })

        this.validate_inputs()
        },
      selected_irrigation_type: function(val){
        this.$store.selects.irrigation_type_code = val.substr(0,1)
        this.validate_inputs()
      },
      selected_variety: function(val){
        if (val != 'Others'){
        this.$store.selects.variety = val
        this.variety_text = val
        this.validate_inputs()
      }
      },
      selected_taluka: function(val){
        var o = _.filter(this.region_dtl_json,{'state_name': this.selected_state,'district_name':this.selected_district,'taluka_name':val});
        var g = _.map(o,'taluka_code')
        this.$store.selects.taluka_name = val;
        this.$store.selects.taluka_code = this.taluka_code = g[0];
        this.nutrient_dtl_json = _.filter(this.nutrient_dtl_dump,{'taluka_code':this.taluka_code})
        this.validate_inputs()
      },
      selected_panchayat: function(val){
        //this.$store.selects.taluka_name = val;
        var index = this.gp_code_list.indexOf(val);
        this.panchayat_name = this.gp_name_list[index]
        var g = val + "";
        if (g.length < 2){
          this.panchayat_code = "0" + g
        } else {
          this.panchayat_code = val
        }
        this.validate_inputs()
        }
      }
    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

@import '../stylesheet/stylesheet.css'

</style>
