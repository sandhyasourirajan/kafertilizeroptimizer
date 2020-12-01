<template>

  <div class="page-header"> <br> <br> 
<!--    <div class="page-header-title">
      <h1>
        <v-btn color="grey" dark @click.stop="drawer = !drawer"> <v-icon> add_box </v-icon> </v-btn>
      FERTILIZER OPTIMIZER
      <v-btn color="grey" style="float:right" @click="logout_function" > Log Out  </v-btn>
      <v-switch :label="`ಕನ್ನಡ`" v-model="Kannada_select_switch"> Kannada </v-switch>
      <p> Getter's language: {{getterLanguage}}</p>
      </h1>
    </div> -->

    <v-toolbar color="grey" fixed app :clipped-left="clipped">
    <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    <v-toolbar-title> FERTILIZER OPTIMIZER </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-switch :label="`ಕನ್ನಡ`" v-model="Kannada_select_switch"> Kannada </v-switch>
          <v-btn color="grey" style="float:right" @click="logout_function" > Log Out  </v-btn>
        </v-toolbar>

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <!-- <v-list class="pa-1">
        <v-list-tile v-if="mini" @click.stop="mini = !mini">
          <v-list-tile-action>
            <v-icon>chevron_right</v-icon>
          </v-list-tile-action>
        </v-list-tile>

        <v-list-tile avatar tag="div">
          <v-list-tile-avatar>
            <img src="https://randomuser.me/api/portraits/men/85.jpg">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>John Leider</v-list-tile-title>
          </v-list-tile-content>

          <v-list-tile-action>
            <v-btn icon @click.stop="mini = !mini">
              <v-icon>chevron_left</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
      </v-list> -->

      <v-list class="pt-0" dense>
        <v-divider light></v-divider>

        <v-list-tile
          v-for="item in items"
          :key="item.title"
          :to="{path:item.path}"
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

  </div>

</template>

<script>
import API from '../reducers/API'
import { logout , getProfile }  from '../auth0-service'

export default {

  name: 'PageHeader',
  data: function () {
    return {
    language_list:['English','Kannada'],
    Kannada_select_switch:'',
    selected_language:'Kannada',
    user_dtl_json:{},
    drawer: null,
    clipped: false,
    mini:false,
    items: [
      { title: 'Fertilizer Optimizer', icon: 'dashboard',path:'/page0' },
      { title: 'Add Nutrient', icon: 'note_add',path:'/page1'  },
      { title: 'Add Fertilizer', icon: 'note_add' ,path:'/page2' },
      { title: 'Contact', icon: 'contact_mail',path:'/contact' },
      ]
      }
  },
  methods: {
    logout_function(){
    logout();
    }
    },
    created: function(){
    // Call the API to fetch the nutrient details from the DB
    API.fetchUserAccessInfo()
       .then(user_info => {
         this.$store.user_dtl_json = user_info.user_access
        })
       .catch(error => {
         console.error(error);
        })

    getProfile()
    },
    computed:{
    },

    watch:{
      Kannada_select_switch: function(val){
        console.log('I have clicked language switch')
        if(this.Kannada_select_switch == true){
        this.$store.getters.selected_language = 'Kannada'
        console.log("kannada")
        } else {
        this.$store.getters.selected_language = 'English'
        console.log("english")
        }
        },
      }
      }
</script>

<style scoped>
@import '../stylesheet/stylesheet.css'
</style>
