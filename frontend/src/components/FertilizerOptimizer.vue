<template>
  <div class="optimize">
      <v-container grid-list-xl class="text-md-center" style="min-width:100%">

        <h2 style="text-transform:uppercase"> FERTILIZER LIST IN {{selected_taluka}} TALUKA </h2>

          <!-- Section to select the fertilizers with vue data table -->

          <v-data-table :rows-per-page-items=[25] :headers="headers" :items="fertilizer_list" :search="search"
          v-model="selected_fertilizer" item-key="fertilizer_name" select-all class="elevation-1">

            <template slot="headerCell" slot-scope="props">
              <v-tooltip bottom>
                <span slot="activator"> {{ props.header.text }} </span>
                <span> {{ props.header.text }} </span>
              </v-tooltip>
            </template>

            <template slot="items" slot-scope="props">
              <td> <v-checkbox v-model="props.selected" primary hide-details></v-checkbox> </td>
              <td class="justify-center">{{ props.item.fertilizer_name }}</td>
              <td class="justify-center">{{ props.item.bag_weight_kg }}</td>
              <td class="justify-center">{{ props.item.bag_cost_INR }}</td>
              <td class="justify-center layout px-0">
                <!-- <v-btn icon class="mx-0" @click="editItem(props.item)">
                  <v-icon color="primary">edit</v-icon>
                </v-btn> -->
                <v-btn icon class="mx-0" @click="deleteItem(props.item)">
                  <v-icon color="primary">delete</v-icon>
                </v-btn>
              </td>

            </template>
          </v-data-table>

          <h4>
          <v-btn round class="mx-0" :to = "{'name':'AddFertilizer'}"> Add/Edit Fertilizer </v-btn>
          <v-btn round class="mx-0" @click="refresh"> Refresh Fertilizer list </v-btn>
          <a href="#fertilizer-dtl-section">
          <v-btn round class="mx-0" @click="optimize"> Submit Fertilizer </v-btn>
        </a>
        </h4>


       <h2> FERTILIZER OPTIMIZER </h2>

       <!-- Section to display the N,P,K and cost for optimial fertilizer combination  -->

       <div id="fertilizer-dtl-section">
         <v-btn round class="mx-0" @click="display_result">
           <v-icon color="primary">show_chart</v-icon>  Run Fertilizer Optimizer
         </v-btn>
         <br><br>

         <v-layout>
           <v-text-field :readonly=true v-model="NPK_deficit.N_deficit" label="Deficit Nitrogen (kg)" style="width:50px"></v-text-field>
           <v-text-field :readonly=true v-model="optimized_output.optimized_N_qty" label="Estimated Nitrogen (kg)" style="width:50px"></v-text-field>
         </v-layout>

         <v-layout>
           <v-text-field :readonly=true v-model="NPK_deficit.P_deficit" label="Deficit Phosphorus (kg)" style="width:50px"></v-text-field>
           <v-text-field :readonly=true v-model="optimized_output.optimized_P_qty" label="Estimated Phosphorus (kg)" style="width:50px"></v-text-field>
         </v-layout>

         <v-layout>
           <v-text-field :readonly=true v-model="NPK_deficit.K_deficit" label="Deficit Potassium (kg)" style="width:50px"></v-text-field>
           <v-text-field :readonly=true v-model="optimized_output.optimized_K_qty" label="Estimated Potassium (kg)" style="width:50px"></v-text-field>
         </v-layout>

         <v-layout>
           <v-text-field :readonly=true v-model="optimized_output.total_cost" align="center" label="Total Cost (INR)" style="width:50px"></v-text-field>
         </v-layout>

       </div>

       <h3> FERTILIZER SUGGESTION </h3>

       <!-- Section to display the optimial fertilizer combination  -->

       <v-data-table :headers="optimized_headers" :items="optimized_fertilizer_list" hide-actions class="elevation-1">
         <template slot="items" slot-scope="props">
           <td class="justify-center">{{ props.item.fertilizer_name }}</td>
           <td class="justify-center">{{ props.item.fertilizer_bag_weight }}</td>
           <td class="justify-center">{{ props.item.fertilizer_quantity_kg }}</td>
           <td class="justify-center">{{ props.item.fertilizer_bag_required }}</td>
         </template>
       </v-data-table>

       <v-btn  round color="primary" :to="{'name':'Home'}"> New query
       </v-btn>
     </v-container>
     <br>

   </div>
</template>

<script>
import API from '../reducers/API'
import _ from 'lodash';

  export default {
    name: 'FertilizerOptimizer',
    data () {
      return {
        fertilizer_list:[],
        selected_taluka:'',
        optimized_fertilizer_name:[],
        optimized_fertilizer_bag_weight_kgs:[],
        optimized_fertilizer_qty_kgs:[],
        optimized_fertilizer_qty_bags:[],
        optimized_headers: [
          { text: 'Fertilizer name',align: 'center',value: 'fertilizer_name'},
          { text: 'Weight of one fertilizer bag (kg)', value: 'fertilizer_bag_weight',align:'center'},
          { text: 'Quantity of the fertilizer (kg)', value: 'fertilizer_quantity_kg',align:'center'},
          { text: 'Quantity of the fertilizer (bags)', value: 'fertilizer_bag_required',align:'center'}
        ],
        NPK_deficit:{
          N_deficit:0,
          P_deficit:0,
          K_deficit:0
        },
        search:'',
        selected_fertilizer:[],
        optimized_output:{},
        optimized_fertilizer_list :[],
        dialog: false,
        headers: [
          { text: 'Fertilizer name',align: 'center',value: 'fertilizer_name',textcolor:"primary"},
          { text: 'Weight of one fertilizer bag (kg)', align: 'center', value: 'bag_weight_kg' },
          { text: 'Cost of the bag (INR)', align: 'center',sortable: true, value: 'bag_cost_INR' },
          { text: 'Actions', value: 'name', align: 'center', sortable: false }
        ],
        }
      },

    created : function () {
      this.NPK_deficit = this.$store.selects.NPK_deficit
      this.selected_taluka = this.$store.selects.taluka_name
      this.load()
      },

      mounted : function () {
        this.selected_fertilizer = []
        this.optimized_output = {}
        this.optimized_fertilizer_list = []
        this.NPK_deficit = this.$store.selects.NPK_deficit
      },

      methods:{
        load(){
          var args = {"taluka_code":this.$store.selects.taluka_code}

          API.fetchFertilizer(args)
          .then(fertilizer_info => {
            this.fertilizer_list = fertilizer_info.fertilizer
          })
          .catch(error => {
          console.error(error);
        })
        },
        refresh(){
          this.load()
        },
        deleteItem (item) {
          const index = this.fertilizer_list.indexOf(item)
          confirm('Are you sure you want to delete this item?') && this.fertilizer_list.splice(index, 1)
        },
      optimize(){
        this.optimized_fertilizer_list = []
        var fertilizer_name_list  = _.map(this.selected_fertilizer, 'fertilizer_name');
        var fertilizer_bag_cost_list  = _.map(this.selected_fertilizer, 'bag_cost_INR');
        var args = {"N_deficit": this.$store.selects.NPK_deficit.N_deficit,
                  "P_deficit": this.$store.selects.NPK_deficit.P_deficit,
                  "K_deficit": this.$store.selects.NPK_deficit.K_deficit,
                  "fertilizer_name": fertilizer_name_list,
                  "taluka_code": this.$store.selects.taluka_code
                  // "fertilizer_bag_cost": fertilizer_bag_cost_list
                }
        this.$store.api.optimized_output = {}

        API.fetchOptimizedData(args)
            .then(optimized_response => {
              this.$store.api.optimized_output = optimized_response.optimized_output})
            .catch(error => {
              console.log(error);
            })

        },

      display_result(){
        this.optimized_output = this.$store.api.optimized_output

        var s = this.optimized_output.fertilizer_name

        for (var i=0;i < this.optimized_output.fertilizer_name.length; i++){

          if(this.optimized_output.fertilizer_bag_required[i]!=0){
            this.optimized_fertilizer_name.push(this.optimized_output.fertilizer_name[i])
            this.optimized_fertilizer_bag_weight_kgs.push(this.optimized_output.fertilizer_bag_weight[i])
            this.optimized_fertilizer_qty_kgs.push(this.optimized_output.fertilizer_quantity_kg[i])
            this.optimized_fertilizer_qty_bags.push(this.optimized_output.fertilizer_bag_required[i])

            this.optimized_fertilizer_list.push({"fertilizer_name": this.optimized_output.fertilizer_name[i],
                              "fertilizer_bag_required": this.optimized_output.fertilizer_bag_required[i],
                              "fertilizer_quantity_kg": this.optimized_output.fertilizer_quantity_kg[i],
                              "fertilizer_bag_weight": this.optimized_output.fertilizer_bag_weight[i]})
                            }

            }
      this.update_transaction_table()
    },
    update_transaction_table(){

      var parms = {	"crop_name": this.$store.selects.crop_name,
                    "irrigation_type_code":this.$store.selects.irrigation_type_code,
                    "variety": this.$store.selects.variety,
                    "farmer_ID": this.$store.selects.farmer_ID,
                    "area_acre": this.$store.selects.area_acre,
                    "n_soil_test":this.$store.selects.NPK_soil_test_result.N_soil_test_result,
                    "p_soil_test":this.$store.selects.NPK_soil_test_result.P_soil_test_result,
                    "k_soil_test":this.$store.selects.NPK_soil_test_result.K_soil_test_result,
                    "taluka_code":this.$store.selects.taluka_code,
                    "n_deficit": this.$store.selects.NPK_deficit.N_deficit,
                    "p_deficit": this.$store.selects.NPK_deficit.P_deficit,
                    "k_deficit": this.$store.selects.NPK_deficit.K_deficit,
                    "estimated_cost":this.optimized_output.total_cost,
                    "user_id":this.$store.userProfile.email,
                    "fertilizer_name": this.optimized_fertilizer_name,
                    "fertilizer_bag_weight":this.optimized_fertilizer_bag_weight_kgs,
                    "fertilizer_quantity_kg": this.optimized_fertilizer_qty_kgs,
                    "fertilizer_bag_required":this.optimized_fertilizer_qty_bags
                  }

      // this.$store.api.optimized_output = {}

      API.AddTransactionData(parms)
            .then(response_out => {
              alert(response_out) })
            .catch(error => {
              console.log(error);
            })

    }
      },

      watch:{
      },

  }

</script>

<style scoped>

  @import '../stylesheet/stylesheet.css'

</style>
