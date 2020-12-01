// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from '@/router'
//import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import store from './store/store'
import VueStash from 'vue-stash';
import VueIntro from 'vue-introjs';
//import auth from '@/auth'

// App specific component pages

import PageHeader from './components/PageHeader.vue'
import PageFooter from './components/PageFooter.vue'

// Components specific to Fertilizer Optimizer Page - Different languages
import FertilizerOptimizer from './components/FertilizerOptimizer.vue'
import FertilizerOptimizerKannada from './components/FertilizerOptimizerKannada.vue'
import FOEnglish from './components/FOEnglish.vue'
import FOKannada from './components/FOKannada.vue'

// Components specific to Fertilizer add page
import AddFertilizer from './components/AddFertilizer.vue'
import Fertilizer from './components/Fertilizer.vue'

// Components specific to Nutrient add page
import AddNutrient from './components/AddNutrient.vue'
import Nutrient from './components/Nutrient.vue'

// Other miscellaneous pages
import AddRaitamitra from './components/AddRaitamitra.vue'
import contact from './components/contact.vue'
import restricted from './components/restricted.vue'

Vue.use(Vuetify, { theme: {
  primary: '#B11117',
  secondary: '#B11117',
  accent: '#B11117',
  error: '#B11117',
  info: '#B11117',
  success: '#B11117',
  warning: '#B11117'
}})

Vue.use(VueStash);
Vue.use(VueIntro);
//Vue.use(auth);

Vue.config.productionTip = false


Vue.component('page-header', PageHeader)
Vue.component('page-footer', PageFooter)

// Components specific to Fertilizer Optimizer Page - Different languages
Vue.component('optimize', FertilizerOptimizer)
Vue.component('optimize-kannada', FertilizerOptimizerKannada)
Vue.component('fo-english',FOEnglish)
Vue.component('fo-kannada',FOKannada)

// Components specific to Fertilizer add page
Vue.component('fertilizer',Fertilizer)
Vue.component('add-edit-fertilizer',AddFertilizer)

// Components specific to Nutrient add page
Vue.component('nutrient',Nutrient)
Vue.component('add-edit-nutrient',AddNutrient)

// Other miscellaneous pages
Vue.component('contact',contact)
Vue.component('restricted',restricted)
/* eslint-disable no-new */

new Vue({
  el: '#app',
  data:{store},
  router,
  render: h => h(App)
})
// .$mount('#app')
