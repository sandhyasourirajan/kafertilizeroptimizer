const getters = {
getMyState: state => state.selected_language
}

export default {
    api: {
        fertilizer_dtl_json:{},
        user_dtl_json:{},
        region_dtl_json:{},
        optimized_output:{}
      },
    selects:{
      crop_name:'',
      irrigation_type_code:'',
      variety:'',
      farmer_ID:0,
      area_acre:0,
      taluka_name:'',
      region_code:0,
      NPK_kg_per_acre:{
        N_kg_per_acre:0,
        P_kg_per_acre:0,
        K_kg_per_acre:0
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
      },
      NPK_soil_test_result:{
        N_soil_test_result:0,
        P_soil_test_result:0,
        K_soil_test_result:0
        }
      },
    userProfile:{},
    super_user_access:false,
    appState:{
      state:null
    },
    // state: {
    //   language: [
    //     { id: 1, text: 'English', selection: true },
    //     { id: 2, text: 'Kannada', selection: false }
    //     ]
    //   },
    getters: {
      selected_language: ''
        }
      }
