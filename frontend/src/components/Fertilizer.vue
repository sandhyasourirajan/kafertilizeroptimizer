<template>
  <div class="fertilizer"> <br>

    <div class="intro" v-intro-step="1" v-intro="'Welcome to Fertilizer detail Add/Edit Screen. Click Next for the Getting Started guide, else press Skip.'">

    <div class="add" v-intro-step="2" v-intro="'To add fertilizer detials for a given taluka, add the input details in Add Fertilizer Detail Section. '">
    <section style="{position: relative;width: 100%;border: 1px solid;}">
      <div style="float: right;">
        <v-btn @click="help_guide"> Click here for a self starter guide </v-btn>
      </div>
      <h2 style="{display: inline;}"> FERTILIZER ADD SECTION </h2>
    </section>

    <div class="add-edit-section"> <br>

      <v-layout row>
        <v-flex md2>
          Fertilizer Name:
        </v-flex>

        <v-flex md4>
              <input type="text" v-model="fertilizer_dtl.fertilier_name" style="width:300px"/> <br><br>
        </v-flex>

      </v-layout>

      <v-layout row>
          <v-flex md2>
              Weight of a fertilizer bag (kg):
          </v-flex>

          <v-flex md4>
              <input type="number" placeholder="0" v-model="fertilizer_dtl.bag_weight_kg" style="width:300px"/> <br><br>
          </v-flex>

          <v-flex md2>
              Cost of a fertilizer bag (INR):
          </v-flex>

          <v-flex md4>
              <input type="number" placeholder="0" v-model="fertilizer_dtl.bag_cost_INR" style="width:300px"/> <br><br>
          </v-flex>

      </v-layout>

      <v-layout row>
          <v-flex md4>
            <v-flex md10>
                Quantity of Nitrogen in a fertilizer bag(kg): <input type="number" placeholder="0" v-model="fertilizer_dtl.n_per_bag_kg" style="width:300px"/> <br><br>
            </v-flex>
          </v-flex>

          <v-flex md4>
            <v-flex md10>
                Quantity of Phosphorus in a fertilizer bag (kg): <input type="number" placeholder="0" v-model="fertilizer_dtl.p_per_bag_kg" style="width:300px"/> <br><br>
            </v-flex>
          </v-flex>

          <v-flex md4>
            <v-flex md10>
                Quantity of Potassium in a fertilizer bag (kg): <input type="number" placeholder="0" v-model="fertilizer_dtl.k_per_bag_kg" style="width:300px"/> <br><br>
            </v-flex>
          </v-flex>
      </v-layout>

      <v-layout row>
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

      <v-flex class="text-md-center">
          <v-btn round color="primary" @click="validate_inputs"> Add Fertilizer </v-btn>
      </v-flex>

      <br>
      </div>
    </div>

    <div class="edit" v-intro-step="3" v-intro="'To edit the fertilizer detail for a given taluka/fertilizer name, search for the fertilizer name and click on edit icon in the row corresponding to the fertilizer and then save the changes.'">
        <h2> FERTILIZER EDIT SECTION </h2>

        <div class="add-edit-section">  <br>
          <v-dialog v-model="edit_dialog" max-width="1000px">
            <v-card>
              <v-card-title>
                <span class="headline"> Edit Fertilizer </span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 sm6 md4>
                      <v-text-field :readonly="true" v-model="editedItem.fertilizer_name" label="Fertilizer name"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.bag_weight_kg" label="Weight of the bag (kg)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.bag_cost_INR" label="Cost of the bag (INR)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.n_per_bag_kg" label="Nitrogen quantity per bag (kg)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.p_per_bag_kg" label="Phosphorus quantity per bag (kg)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field v-model="editedItem.k_per_bag_kg" label="Potassium quantity per bag (kg)"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field :readonly="true" v-model="editedItem.taluka_code" label="Region code"></v-text-field>
                    </v-flex>

                    <v-flex xs12 sm6 md4>
                      <v-text-field :readonly="true" v-model="editedItem.taluka_name" label="Taluka"></v-text-field>
                    </v-flex>

                    <v-flex class="text-xxs-center">
                    * Fertilizer name, Taluka & Region code cannot be edited. Please add a new fertilizer for change in these three fields.
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
              Fertilizer Details &nbsp &nbsp


                <v-btn round class="mx-0" @click="load"> Refresh list </v-btn> &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
                <v-spacer> </v-spacer>

              <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
            </v-card-title>

            <v-data-table :headers="headers" :items="fertilizer_list" :search="search">
              <template slot="items" slot-scope="props">
                <td class="justify-center">{{ props.item.fertilizer_name }}</td>
                <td class="justify-center">{{ props.item.bag_weight_kg }}</td>
                <td class="justify-center">{{ props.item.bag_cost_INR }}</td>
                <td class="justify-center">{{ props.item.n_per_bag_kg }}</td>
                <td class="justify-center">{{ props.item.p_per_bag_kg }}</td>
                <td class="justify-center">{{ props.item.k_per_bag_kg }}</td>
                <td class="justify-center">{{ props.item.taluka_code }}</td>
                <td class="justify-center">{{ props.item.taluka_name }}</td>
                <td class="justify-center layout px-0">
                  <v-btn icon class="mx-0" @click="edit_fertilizer(props.item)">
                    <v-icon color="primary">edit</v-icon>
                  </v-btn>
                  <v-btn icon class="mx-0" @click="delete_fertilizer(props.item)">
                    <v-icon color="primary">delete</v-icon>
                  </v-btn>
                </td>
              </template>
              <v-alert slot="no-results" :value="true" color="error" icon="warning">
                Your search for "{{ search }}" found no results.
              </v-alert>
            </v-data-table>
          </v-card>
          <br>
        </div>
      </div>
      <page-footer></page-footer>

    </div>
  </div>
</template>

<script>
import API from '../reducers/API'
import 'intro.js/introjs.css';

  export default {
    name: 'Fertilizer',
    data () {
      return {
        // Fields entered or selected in the App
        fertilizer_dtl:{
          fertilier_name:'',
          bag_weight_kg:0,
          bag_cost_INR:0,
          n_per_bag_kg:0,
          p_per_bag_kg:0,
          k_per_bag_kg:0,
          taluka_code:0
        },
        selected_state:'',
        selected_district:'',
        selected_taluka:'',

        // API result
        region_dtl_json:{},
        fertilizer_list:[],

        //Fields for edit dialog / data table
        search: '',
        headers: [
          { text: 'Fertilizer name',align: 'left',sortable: true,value: 'fertilizer_name',textcolor:"primary"},
          { text: 'Weight of a fertilizer bag (kg)', align: 'left',sortable: true, value: 'bag_weight_kg' },
          { text: 'Cost of the bag (INR)', align: 'left',sortable: true, value: 'bag_cost_INR' },
          { text: 'N qty per bag (kg)', align: 'left', value: 'n_per_bag_kg' },
          { text: 'P qty per bag (kg)', align: 'left', value: 'p_per_bag_kg' },
          { text: 'K qty per bag (kg)', align: 'left', value: 'k_per_bag_kg' },
          { text: 'Region Code', align: 'left', value: 'taluka_code' },
          { text: 'Taluka', align: 'left', value: 'taluka_name' },
          { text: 'Actions', value: 'name', align: 'left', sortable: false }
        ],
        editedIndex: -1,
        editedItem: {
          fertilizer_name: '',
          bag_weight_kg: 0,
          bag_cost: 0,
          n_per_bag_kg:0,
          p_per_bag_kg:0,
          k_per_bag_kg:0,
          taluka_code:0
        },
        defaultItem: {
          fertilizer_name: '',
          bag_weight_kg: 0,
          bag_cost: 0,
          n_per_bag_kg:0,
          p_per_bag_kg:0,
          k_per_bag_kg:0,
          taluka_code:0
        },
        edit_dialog:false,
        }
    },

    created : function () {
      this.load()
      //this.region_dtl_json = this.$store.api.region_dtl_json

      // Call the API to fetch the state, district and taluka details
      API.fetchRegionData()
         .then(region_info => {
            this.region_dtl_json = region_info.region_dtl
          })
         .catch(error => {
            console.error(error);
          })


      },
    mounted : function(){
      },

    methods:{
      load(){
        // Call the API to fetch the complete fertilizer data from the DB for edit

        API.fetchFertilizerData()
        .then(fertilizer_info => {
          this.fertilizer_list = fertilizer_info.fertilizer
        })
        .catch(error => {
        console.error(error);
        })
      },
      help_guide(){
      this.$intro().start();
      },
      validate_inputs(){
        //Check if inputs are added appropriately
        if ((this.fertilizer_dtl.fertilier_name.length > 0)
            && (this.fertilizer_dtl.taluka_code)
            && (this.fertilizer_dtl.n_per_bag_kg > 0  || this.fertilizer_dtl.p_per_bag_kg > 0  || this.fertilizer_dtl.k_per_bag_kg > 0 )
            && this.fertilizer_dtl.bag_cost_INR > 0
            && this.fertilizer_dtl.bag_weight_kg)
            {
              this.add_fertilizer();
            }else{
              alert ("Please validate the inputs and try again")
            }
      },
    add_fertilizer(){
      // Call API to add new fertilizer to database
      var args = {"fertilizer_name":this.fertilizer_dtl.fertilier_name,
                  "bag_weight_kg":this.fertilizer_dtl.bag_weight_kg,
                  "bag_cost_INR":this.fertilizer_dtl.bag_cost_INR,
                  "n_per_bag_kg":this.fertilizer_dtl.n_per_bag_kg,
                  "p_per_bag_kg":this.fertilizer_dtl.p_per_bag_kg,
                  "k_per_bag_kg":this.fertilizer_dtl.k_per_bag_kg,
                  "taluka_code":this.fertilizer_dtl.taluka_code,
                  "user_id":this.$store.userProfile.email

                  }

      // Call the API to fetch the complete fertilizer data from the DB for edit

      API.AddFertilizerData(args)
      .then(response_out => {
        alert(response_out) })
      .catch(error => {
        console.log(error);
      })

    },
    edit_fertilizer (item) {
      this.editedIndex = this.fertilizer_list.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.edit_dialog = true
      },
    // delete_fertilizer (item) {
    //   this.deletedIndex = this.fertilizer_list.indexOf(item)
    //   this.deleteItem = Object.assign({}, item)
    //   this.delete_dialog = true
    //   },
    close () {
      this.edit_dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
        }, 300)
      },
    save () {
      if (this.editedIndex > -1) {
        var s = this.editedIndex

        // Call the API to fetch the complete fertilizer data from the DB for edit

        this.editedItem.bag_cost_INR = parseFloat(this.editedItem.bag_cost_INR);
        this.editedItem.n_per_bag_kg = parseFloat(this.editedItem.n_per_bag_kg);
        this.editedItem.p_per_bag_kg = parseFloat(this.editedItem.p_per_bag_kg);
        this.editedItem.k_per_bag_kg = parseFloat(this.editedItem.k_per_bag_kg);

        var args = {"fertilizer_name":this.editedItem.fertilizer_name,
                    "bag_weight_kg":this.editedItem.bag_weight_kg,
                    "bag_cost_INR":this.editedItem.bag_cost_INR,
                    "n_per_bag_kg":this.editedItem.n_per_bag_kg,
                    "p_per_bag_kg":this.editedItem.p_per_bag_kg,
                    "k_per_bag_kg":this.editedItem.k_per_bag_kg,
                    "taluka_code":this.editedItem.taluka_code,
                    "user_id":this.$store.userProfile.email
                    }

        API.EditFertilizerData(args)
        .then(response_out => {
          alert(response_out)
          Object.assign(this.fertilizer_list[s], this.editedItem)
          this.load()
        })
        // .catch(error => {
        //   alert("Please verify your inputs")
        // })
        } else {
          alert("Please verify your inputs")
        }
      this.close()
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
          this.fertilizer_dtl.taluka_code = g[0]
        }
    }
  }
</script>

<style scoped>

@import '../stylesheet/stylesheet.css'

</style>
