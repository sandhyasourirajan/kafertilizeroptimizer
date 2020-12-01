<template>
  <div class="add-edit-fertilizer">
    <fertilizer v-if="super_user_access">
    </fertilizer>

    <restricted v-if="!(super_user_access)">
    </restricted>

  </div>
</template>

    </div>
  </div>
</template>

<script>
  export default {
    name: 'AddFertilizer',
    data() {
    return{
      super_user_access:false,
    }
    },
    created:function(){

    this.super_user_access = this.$store.super_user_access
    },
    mounted : function(){
      },
    methods:{
      },
    computed: {
      },
      watch:{
    }
  }
</script>

<style scoped>

@import '../stylesheet/stylesheet.css'

</style>
