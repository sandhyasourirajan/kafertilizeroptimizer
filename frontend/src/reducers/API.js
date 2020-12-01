import ezFetch from 'ez-fetch';

export default {

  // Call the API to fetch the nutrient details from DB
  fetchNutrientData(){
    var fertilizer_list = []
    //const API_URL = `http://35.200.155.144:8000/nutrient`
    const API_URL = `http://localhost:8000/nutrient`
    return ezFetch.get(API_URL)
  },

  // Call the API to fetch the fertilizer details from DB
  fetchFertilizerData(){
    //const API_URL = `http://35.200.155.144:8000/fertilizerdetail`
    const API_URL = `http://localhost:8000/fertilizerdetail`
    return ezFetch.get(API_URL)
  },

  // Call the API to fetch the fertilizer details for a given region code/ taluka from DB
  fetchFertilizer(args){
    //const API_URL = `http://35.200.155.144:8000/fertilizer`
    const API_URL = `http://localhost:8000/fertilizer`
    return ezFetch.post(API_URL,args)
  },

  // Call the API to fetch the variety details for a given crop from DB
  fetchVariety(args){
    //const API_URL = `http://35.200.155.144:8000/variety`
    const API_URL = `http://localhost:8000/variety`
    return ezFetch.post(API_URL,args)
  },

  // Call the API to fetch the state, district and taluka detail from the DB
  fetchRegionData(){
    //const API_URL = `http://35.200.155.144:8000/region`
    const API_URL = `http://localhost:8000/region`
    return ezFetch.get(API_URL)
  },

  // Call the API to fetch the gram panchayat detail from the DB
  fetchGPData(){
    //const API_URL = `http://35.200.155.144:8000/gp`
    const API_URL = `http://localhost:8000/gp`
    return ezFetch.get(API_URL)
  },

  // Call the API to fetch the gram panchayat detail from the DB
  fetchUserAccessInfo(){
    //const API_URL = `http://35.200.155.144:8000/useraccess`
    const API_URL = `http://localhost:8000/useraccess`
    return ezFetch.get(API_URL)
  },

  // Call the API to compute the fertilizer combination for an optimal cost
  fetchOptimizedData (args) {
    //const API_URL = `http://35.200.155.144:8000/optimize`
    const API_URL = `http://localhost:8000/optimize`
    return ezFetch.post(API_URL,args)
  },

  // Add a new fertilizer to DB
  AddFertilizerData (args) {
    //const API_URL = `http://35.200.155.144:8000/addfertilizer`
    const API_URL = `http://localhost:8000/addfertilizer`
    return ezFetch.post(API_URL,args)
  },

  // Edit an existing fertilizer in the DB
  EditFertilizerData (args) {
    //const API_URL = `http://35.200.155.144:8000/editfertilizer`
    const API_URL = `http://localhost:8000/editfertilizer`
    return ezFetch.post(API_URL,args)
  },

  // Add a new nutrient detail to DB
  AddNutrientData (args) {
    //const API_URL = `http://35.200.155.144:8000/addnutrient`
    const API_URL = `http://localhost:8000/addnutrient`
    return ezFetch.post(API_URL,args)
  },

  // Edit an existing fertilizer in the DB
  EditNutrientData (args) {
    //const API_URL = `http://35.200.155.144:8000/editnutrient`
    const API_URL = `http://localhost:8000/editnutrient`
    return ezFetch.post(API_URL,args)
  },

  // AddRaitamitra (args) {
  //   //const API_URL = `http://35.200.155.144:8000/addraitamitra`
  //   const API_URL = `http://localhost:8000/addraitamitra`
  //   return ezFetch.post(API_URL,args)
  // },
  //
  // Add a transaction detail to DB
  AddTransactionData (args) {
    //const API_URL = `http://35.200.155.144:8000/updatetransaction`
    const API_URL = `http://localhost:8000/updatetransaction`
    return ezFetch.post(API_URL,args)
  },
};
