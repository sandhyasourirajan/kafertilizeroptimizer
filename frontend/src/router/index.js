import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import FertilizerOptimizer from '@/components/FertilizerOptimizer'
import FertilizerOptimizerKannada from '@/components/FertilizerOptimizerKannada'
import AddFertilizer from '@/components/AddFertilizer'
import AddNutrient from '@/components/AddNutrient'
//import AddRaitamitra from '@/components/AddRaitamitra'
import contact from '@/components/contact'
import Callback from '@/components/Callback'

Vue.use(Router)

export default new Router({

  mode:'history',
  routes: [
    {
      path:'/page0',
      name:'Home',
      component: Home
    },
    {
      path: '/optimize',
      name: 'FertilizerOptimizer',
      component: FertilizerOptimizer
    },
    {
      path: '/optimize-kannada',
      name: 'FertilizerOptimizerKannada',
      component: FertilizerOptimizerKannada
    },
    {
      path: '/page1',
      name: 'AddNutrient',
      component: AddNutrient
    },
    {
      path: '/page2',
      name: 'AddFertilizer',
      component: AddFertilizer
    },
/*    {
      path: '/page3',
      name: 'AddRaitamitra',
      component: AddRaitamitra
    }, */
    {
      path: '/contact',
      name: 'contact',
      component: contact
    },
    {
      path: '/Callback',
      name: 'Callback',
      component: Callback
    }
  ]
})

/*
// very basic "setup" of a global guard
router.beforeEach((to, from, next) => {
  if(to.name == 'Callback') { // check if "to"-route is "callback" and allow access
    next()
  } else if (router.app.$auth.isAuthenticated()) { // if authenticated allow access
    next()
  } else { // trigger auth0 login
    router.app.$auth.login()
  }
})
// Redirect to the home route if any routes are unmatched
// Router.redirect({
//   '*': '/page0'
// })

// export default index */
