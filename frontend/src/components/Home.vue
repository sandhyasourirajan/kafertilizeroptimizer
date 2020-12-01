<template>
  <div class="home">

  <fo-english v-if="!(kannada_switch)">
  </fo-english>

  <fo-kannada v-if="kannada_switch"> 
  </fo-kannada>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name:'Home',
  //props: {
  //  value: false
  //},
  data() {
  return{
    english_switch:false,
    kannada_switch:false,
    selected_language:'',
  }
  },
  created:function(){
  if (this.$store.selected_language == 'English'){
    this.english_switch = true
  }
  if (this.$store.selected_language == 'Kannada'){
    this.kannada_switch = true
  }
  },
  computed:{
  // ...mapGetters({
  // // map `this.doneCount` to `this.$store.getters.doneTodosCount`
  // selected_language: 'selected_language'
// })
  },
 watch:{
   selected_language: function(val){
     console.log(val)
    //  if(this.selected_language == "English"){
    //    this.english_switch = true
    //  } else {
    //  this.english_switch = false
    //  }
  if (this.$store.selected_language == 'English'){
    this.english_switch = true
  }
  if (this.$store.selected_language == 'Kannada'){
    this.kannada_switch = true
     }
   }
}
}
</script>
