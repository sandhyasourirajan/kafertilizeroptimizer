th<template>
  <div class="add-raitamitra">
  <div class="placeholder"></div>

    <sidebar> </sidebar>
    <page-header> </page-header>
       <h2> ADD A RAITAMITRA </h2>
        <div class="add-edit-section">
          <br>
          <v-layout row>

            <v-flex md2>
              Raitamitra e-mail ID:
            </v-flex>
            <v-flex md4>
              <input type="email" v-model="raitamitra_dtl.email_id" style="width:300px"/> <br><br>
            </v-flex>

          </v-layout>

          <v-layout row>

            <v-flex md2>
              Raitamitra Name:
            </v-flex>
            <v-flex md4>
              <input type="text" v-model="raitamitra_dtl.name" style="width:300px"/> <br><br>
            </v-flex>

            <v-flex md2>
              Raitamitra Father's Name:
            </v-flex>
            <v-flex md4>
              <input type="text" v-model="raitamitra_dtl.father_name" style="width:300px"/> <br><br>
            </v-flex>


          </v-layout>

          <v-layout row>
            <v-flex md2>
              Farmer ID:
            </v-flex>
            <v-flex md4>
              <input type="number" placeholder="0" v-model="raitamitra_dtl.farmer_ID" style="width:300px" maxlength="3"/> <br><br>
            </v-flex>

            <v-flex md2>
              Mobile Number:
            </v-flex>
            <v-flex md4>
              <input type="text" placeholder="0" v-model="raitamitra_dtl.mobile_number" style="width:300px" maxlength="10" pattern="[1-9]{1}[0-9]{9}"/> <br><br>
            </v-flex>
          </v-layout>

        </v-layout>
        <v-layout row>
          <v-flex md4>
            <v-flex md10>
              <v-select :items="taluka_select" :rules="[() => !!raitamitra_dtl.taluka_code || 'This field is required']" v-model="raitamitra_dtl.taluka_code" label="Select the Taluka (1 - Navalagund taluka / 2 - Siruguppa taluk)" required></v-select>
            </v-flex>
          </v-flex>

          <v-flex md4>
            <v-flex md10>
              <v-select :items="gp_select" :rules="[() => !!raitamitra_dtl.gram_panchayat_code || 'This field is required']" v-model="raitamitra_dtl.gram_panchayat_code" label="Select the Gram Panchayat Code" required></v-select>
            </v-flex>
          </v-flex>

          <v-flex md4>
            <v-flex md10>
              <v-select :items="village_select" :rules="[() => !!raitamitra_dtl.village_code || 'This field is required']" v-model="raitamitra_dtl.village_code" label="Select the village code" required></v-select>
            </v-flex>
          </v-flex>
        </v-layout>


          <v-flex class="text-md-center">
            <v-btn round color="primary" @click="validate_inputs"> Add Raitamitra </v-btn>
          </v-flex>
          <br>
        </div>

        <page-footer></page-footer>

  </div>
</template>

<script>
import API from '../reducers/API'
import _ from 'lodash';


  export default {
    name: 'AddRaitamitra',
    data () {
      return {
        // Fields entered or selected in the App
        raitamitra_dtl:{
          name:'',
          father_name:'',
          email_id:'',
          farmer_ID:0,
          mobile_number:0,
          UID_no:0,
          village_code:0,
          gram_panchayat_code:0,
          taluka_code:0
        },

        // API result
        place_dtl_json:{},
        region_dtl_json:{},

        // gp_list:[],
        // village_list:[],
        selected_taluka:0,
        selected_gp_code:0,
        selected_village:0,

      }
    },

    created : function () {
      // this.NPK_deficit = this.$store.selects.NPK_deficit
      this.load()
      },

    methods:{
      load(){
        // Call the API to fetch the complete fertilizer data from the DB for edit

        API.fetchVillageCode()
        .then(region_info => {
           this.region_dtl_json = region_info.region_dtl
         })
        .catch(error => {
           console.error(error);
         })
      },
      validate_inputs(){

        if (this.raitamitra_dtl.email_id.length > 0
            && this.raitamitra_dtl.name.length > 0
            && this.raitamitra_dtl.father_name.length > 0
            && this.raitamitra_dtl.farmer_ID.length <= 3
            && this.raitamitra_dtl.mobile_number.length == 10
            && this.raitamitra_dtl.gram_panchayat_code > 0
            && this.raitamitra_dtl.village_code > 0
            && this.raitamitra_dtl.taluka_code > 0){
              this.add_raitamitra();
            } else{
              alert ("Please validate the inputs and try again")
            }
      },

    add_raitamitra(){
      var args = {"raitamitra_email":this.raitamitra_dtl.email_id,
                  "raitamitra_name":this.raitamitra_dtl.name,
                  "raitamitra_father_name":this.raitamitra_dtl.father_name,
                  "raitamitra_farmer_ID":this.raitamitra_dtl.farmer_ID,
                  "raitamitra_mobile_number":this.raitamitra_dtl.mobile_number,
                  "raitamitra_gram_panchayat_code":this.raitamitra_dtl.gram_panchayat_code,
                  "raitamitra_village_code":this.raitamitra_dtl.village_code,
                  "raitamitra_taluka_code":this.raitamitra_dtl.taluka_code,
                  }

      // Call the API to fetch the complete fertilizer data from the DB for edit

      API.AddRaitamitra(args)
      .then(response_out => {
        alert(response_out) })
      .catch(error => {
        console.log(error);
      })

    },
    // padLeft(nr, n, str){
    // return Array(n-String(nr).length+1).join(str||'0')+nr;
    // }
    },
    computed: {
      taluka_select: function(){
        var taluka_list = []
        for (var i=0;i<this.region_dtl_json.length;i++){
          taluka_list.push(this.region_dtl_json[i].taluka_code)
          }
        return Array.from(new Set(taluka_list))
      },
      gp_select: function(){
        //get the irrigation type for the given crop name
        var o = _.filter(this.region_dtl_json,{'taluka_code': this.raitamitra_dtl.taluka_code});
        var gp_list = _.map(o,'GP_code')
        return gp_list
      },
      village_select: function(){
        //get the irrigation type for the given crop name
        var o = _.filter(this.region_dtl_json,{'taluka_code': this.raitamitra_dtl.taluka_code,'GP_code':this.raitamitra_dtl.gram_panchayat_code});
        var village_list = _.map(o,'village_code')
        return village_list
      },
      },
    // watch:{
    //   raitamitra_dtl.village_code: function(val){
    //     // this.$store.selects.crop_name = val
    //     // var args = {"crop_name":val}
    //     var length = this.raitamitra_dtl.taluka_code.length()
    //     var padded_gp = padLeft()
    //     API.fetchVariety(args)
    //     .then(variety_list => {this.variety_list = variety_list})
    //     .catch(error => {
    //     console.error(error);
    //     })
    //     },
    //
    // }
  }
</script>

<style scoped>

@import '../stylesheet/stylesheet.css'

</style>
