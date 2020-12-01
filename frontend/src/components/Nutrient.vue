<template>
  <div class="nutrient"> <br>
      <div class="intro" v-intro-step="1" v-intro="'Welcome to Nutrient detail Add/Edit Screen. Click Next for the Getting Started guide, else press Skip.'">

        <div class="add" v-intro-step="2" v-intro="'To add maximum allowable N-P-K detail for a crop-irrigation type combination which is not present in the DB, add the input details in Add Nutrient Detail Section. Provide the input crop name, select the irrigation type code from the dropdown and enter the allowable N-P-K values in kg/acre format'">

        <section style="{position: relative;width: 100%;border: 1px solid;}">
          <div style="float: right;">
            <v-btn @click="help_guide"> Click here for a self starter guide </v-btn>
          </div>
          <h2 style="{display: inline;}"> ADD NUTRIENT DETAIL </h2>
        </section>
        <div class="add-edit-section">
          <br>

          <v-layout row>
             <v-flex md6>
              <br>Crop Name: <input type="text" v-model="nutrient_dtl.crop_name" style="width:300px"/> <br>
            </v-flex>
            <v-flex md6>
              <v-select :items="irrigation_type_list" :rules="[() => !!selected_irrigation_type || 'This field is required']" v-model="selected_irrigation_type_code" label="Select an irrigation type code" required></v-select>
            </v-flex>
          </v-layout>

          <v-layout row class="access-enabled">
            <v-flex md4>
              <v-flex md10>
                <v-select :items="state_select" :rules="[() => !!selected_state || 'This field is required']" v-model="selected_state" label="Select the state" required></v-select>
              </v-flex>
            </v-flex>

            <v-flex md4>
              <v-flex md10>
                <v-select :items="district_select" :rules="[() => !!selected_district || 'This field is required']" v-model="selected_district" label="Select the district" required></v-select>
              </v-flex>
            </v-flex>

            <v-flex md4>
              <v-flex md10>
                <v-select :items="taluka_select" :rules="[() => !!selected_taluka || 'This field is required']" v-model="selected_taluka" label="Select the taluka" required></v-select>
              </v-flex>
            </v-flex>
          </v-layout>

          <v-layout row>
            <v-flex md4>
              <v-flex md10>
                Nitrogen requirement (kg/acre): <input type="number" placeholder="0" v-model="nutrient_dtl.n_kg_per_acre" style="width:300px"/> <br><br>
              </v-flex>
            </v-flex>

            <v-flex md4>
              <v-flex md10>
                Phosphorus requirement (kg/acre): <input type="number" placeholder="0" v-model="nutrient_dtl.p_kg_per_acre" style="width:300px"/> <br><br>
              </v-flex>
            </v-flex>

            <v-flex md4>
              <v-flex md10>
                Potassium requirement (kg/acre): <input type="number" placeholder="0" v-model="nutrient_dtl.k_kg_per_acre" style="width:300px"/> <br><br>
              </v-flex>
            </v-flex>
          </v-layout>

          <v-flex class="text-md-center">
            <v-btn round color="primary" @click="validate_inputs"> Add Nutrient detail </v-btn>
          </v-flex>
          <br>
        </div>
      </div>

      <div class="edit" v-intro-step="3" v-intro="'To edit maximum allowable N-P-K detail for a crop-irrigation type combination already existing in the DB, use the Edit Nutrient Detail Section.'">
        <h2  > EDIT NUTRIENT DETAIL </h2>

        <div class="add-edit-section">
          <br>
          <v-dialog v-model="edit_dialog" max-width="1000px">
            <v-card>
              <v-card-title>
                <span class="headline"> Edit Nutrient detail </span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 sm6 md4>
                      <v-text-field :readonly="true" v-model="editedItem.crop_name" label="Crop name"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field :readonly="true" v-model="editedItem.irrigation_type_code" label="Irrigation type code"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.n_kg_per_acre" label="Nitrogen requirement (kg/acre)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.p_kg_per_acre" label="Phosphorus requirement (kg/acre)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.k_kg_per_acre" label="Potassium requirement (kg/acre)"></v-text-field>
                    </v-flex>

                    <v-flex class="text-xxs-center">
                    * Crop name and Irrigation Type Code code cannot be edited. Please add a new nutrient detail for change in these two fields.
                  </v-flex>
                  </v-layout>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" flat @click.native="close">Cancel</v-btn>
                <v-btn color="primary" flat @click.native="save">Save</v-btn>
              </v-card-actions>
            </v-card>

          </v-dialog>

          <v-card>
            <v-card-title>
              <strong> Nutrient details for crop-Irrigation type code combination </strong> &nbsp &nbsp
              <v-btn round class="mx-0" @click="load"> Refresh list </v-btn> &nbsp &nbsp

              <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details v-intro-step="4" v-intro="'Search for the given crop name.After getting the desired crop row from the search, click on the edit icon to edit the N-P-K values. After the changes, click on Save button in the dialog box to update the changes in database.'">
              </v-text-field>
            </v-card-title>

            <v-data-table :headers="headers" :items="nutrient_dtl_list" :search="search">
              <template slot="items" slot-scope="props">
                <td class="justify-center">{{ props.item.crop_name }}</td>
                <td class="justify-center">{{ props.item.irrigation_type_code }}</td>
                <td class="justify-center">{{ props.item.n_kg_per_acre }}</td>
                <td class="justify-center">{{ props.item.p_kg_per_acre }}</td>
                <td class="justify-center">{{ props.item.k_kg_per_acre }}</td>
                <td class="justify-center">{{ props.item.taluka_code }}</td>
                <td class="justify-center">{{ props.item.taluka_name }}</td>

                <td class="justify-center layout px-0" v-intro-step="5" v-intro="'After getting the desired crop row from the search, click on the edit icon to edit the N-P-K values. After the changes, click on Save button in the dialog box to update the changes in database.'">
                  <v-btn icon class="mx-0" @click="edit_nutrient_dtl(props.item)">
                    <v-icon color="primary">edit</v-icon>
                  </v-btn>
                </td>
              </template>
              <v-alert slot="no-results" :value="true" color="error" icon="warning">
                Your search for "{{ search }}" found no results.
              </v-alert>
            </v-data-table>
          </v-card>
          <v-card>
            * Irrigation type code values :  <strong>I</strong> - Irrigated  / R - Rainfed

          </v-card>
          <br>
        </div>
      </div>
      </div>
  </div>
</div>
</template>

<script>
import API from '../reducers/API'
import 'intro.js/introjs.css';

  export default {
    name: 'Nutrient',
    data () {
      return {
        // Fields entered or selected in the App
        irrigation_type_list:['Irrigated','Rainfed'],
        nutrient_dtl:{
          crop_name:'',
          irrigation_type_code:'',
          taluka_code:0,
          n_kg_per_acre:0,
          p_kg_per_acre:0,
          k_kg_per_acre:0
        },
        selected_irrigation_type_code:'',
        selected_irrigation_type:'',
        selected_state:'',
        selected_district:'',
        selected_taluka:'',

        // API result
        nutrient_dtl_list:[],
        region_dtl_json:{},

        //Fields for edit dialog / data table
        search: '',
        headers: [
          { text: 'Crop name',align: 'left',sortable: true,value: 'crop_name',textcolor:"primary"},
          { text: 'Irrigation type code*', align: 'left',sortable: true, value: 'irrigation_type_code' },
          { text: 'Nitrogen requirement (kg/acre)', align: 'left',sortable: true, value: 'n_kg_per_acre' },
          { text: 'Phosphorus requirement (kg/acre)', align: 'left',sortable: true, value: 'p_kg_per_acre' },
          { text: 'Potassium requirement (kg/acre)', align: 'left',sortable: true, value: 'k_kg_per_acre' },
          { text: 'Region Code', align: 'left', value: 'taluka_code' },
          { text: 'Taluka', align: 'left', value: 'taluka_name' },
          { text: 'Actions', value: 'name', align: 'left', sortable: false }
        ],
        editedIndex: -1,
        editedItem: {
          crop_name:'',
          irrigation_type_code:'',
          taluka_code:0,
          n_kg_per_acre:0,
          p_kg_per_acre:0,
          k_kg_per_acre:0
        },
        defaultItem: {
          crop_name:'',
          irrigation_type_code:'',
          n_kg_per_acre:0,
          p_kg_per_acre:0,
          k_kg_per_acre:0
        },
        edit_dialog:false,
        }
    },

    created : function () {
    // Call the API to fetch the region details from the DB
    //this.region_dtl_json = this.$store.api.region_dtl_json
    // Call the API to fetch the state, district and taluka details
    API.fetchRegionData()
       .then(region_info => {
          this.region_dtl_json = region_info.region_dtl
        })
       .catch(error => {
          console.error(error);
        })

      this.load()
      },
    mounted:function(){
    },
    methods:{
      load(){
        //this.nutrient_dtl_list = this.$store.api.nutrient_dtl_json
        //this.nutrient_dtl_list = this.$store.api.nutrient_dtl_dump

        // Call the API to fetch the nutrient details from the DB
          API.fetchNutrientData()
           .then(nutrient_info => {
             this.nutrient_dtl_list = nutrient_info.nutrient
            })
           .catch(error => {
             console.error(error);
            })


      },
      help_guide(){
      this.$intro().start();
      },
      validate_inputs(){

        this.nutrient_dtl.irrigation_type_code = this.selected_irrigation_type_code.substring(0,1)

        if ((this.nutrient_dtl.n_kg_per_acre > 0  || this.nutrient_dtl.p_kg_per_acre > 0  || this.nutrient_dtl.k_kg_per_acre > 0 ) &&
            this.nutrient_dtl.crop_name.length > 0 &&
            this.nutrient_dtl.irrigation_type_code)
            {
              this.add_nutrient_dtl();
            }else{
              alert ("Validate the inputs and try again")
            }
      },

    add_nutrient_dtl(){

      var args = {"crop_name":this.nutrient_dtl.crop_name,
                  "irrigation_type_code":this.nutrient_dtl.irrigation_type_code,
                  "taluka_code":this.nutrient_dtl.taluka_code,
                  "n_kg_per_acre":this.nutrient_dtl.n_kg_per_acre,
                  "p_kg_per_acre":this.nutrient_dtl.p_kg_per_acre,
                  "k_kg_per_acre":this.nutrient_dtl.k_kg_per_acre,
                  "user_id": this.$store.userProfile.email
                  }


      // Call the API to fetch the complete nutrient data from the DB for edit

      API.AddNutrientData(args)
      .then(response_out => {
        alert(response_out) })
      .catch(error => {
        console.log(error);
      })
      this.load();
    },
    edit_nutrient_dtl (item) {
      this.editedIndex = this.nutrient_dtl_list.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.edit_dialog = true
      },
    close () {
      this.edit_dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
        }, 300)
      },
    save () {
      if (isNaN(this.editedItem.n_kg_per_acre) || isNaN(this.editedItem.p_kg_per_acre) || isNaN(this.editedItem.k_kg_per_acre))
      {
        alert('Verify the input N,P,K values. N,P,K values should be numeric')
      }
      else {
          if (this.editedItem.n_kg_per_acre > 0 || this.editedItem.p_kg_per_acre > 0 || this.editedItem.k_kg_per_acre > 0)
            {
              if (this.editedIndex > -1) {
                var s = this.editedIndex

                // Call the API to fetch the complete nutrient data from the DB for edit


                var args = {"crop_name":this.editedItem.crop_name,
                            "irrigation_type_code":this.editedItem.irrigation_type_code,
                            "taluka_code":this.editedItem.taluka_code,
                            "n_kg_per_acre":this.editedItem.n_kg_per_acre,
                            "p_kg_per_acre":this.editedItem.p_kg_per_acre,
                            "k_kg_per_acre":this.editedItem.k_kg_per_acre,
                            "user_id": this.$store.userProfile.email
                            }


                API.EditNutrientData(args)
                .then(response_out => {
                  alert(response_out)
                  Object.assign(this.nutrient_dtl_list[s], this.editedItem)
                  this.close()
                  this.load()
                    })
                    // .catch(error => {
                    //   alert("Insert not working. Please verify your inputs")
                    // })
                  } else {
                    alert("Please verify your inputs")
                  }
                } else{
            alert("N,P,K values cannot be all zeroes. Please verify your inputs")
          }
        }
      }
    },
    computed: {
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

      },

      watch:{
        edit_dialog (val) {
          val || this.close()
        },
        selected_taluka: function(val){
          var o = _.filter(this.region_dtl_json,{'state_name': this.selected_state,'district_name':this.selected_district,'taluka_name':val});
          var g = _.map(o,'taluka_code')
          this.nutrient_dtl.taluka_code = g[0]
        }

    }
  }
</script>

<style scoped>

@import '../stylesheet/stylesheet.css'

</style>
