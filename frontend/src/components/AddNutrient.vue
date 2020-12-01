<template>
  <div class="add-edit-nutrient">

  <nutrient v-if="super_user_access">
  </nutrient>

  <restricted v-if="!(super_user_access)">
  </restricted>

  </div>
</template>

<script>
export default {
  name:'AddNutrient',
  //props: {
  //  value: false
  //},
  data() {
  return{
    super_user_access:false,
  }
  },
  created:function(){
  this.super_user_access = this.$store.super_user_access
  },
}
</script>
