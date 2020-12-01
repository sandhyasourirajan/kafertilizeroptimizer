import { WebAuth } from 'auth0-js'
import axios from 'axios';
import Router from 'vue-router';
import decode from 'jwt-decode';
import store from './store/store'
import API from './reducers/API'

const ID_TOKEN_KEY = 'id_token';
const ACCESS_TOKEN_KEY = 'access_token';

export const webAuth = new WebAuth({
    domain: 'agrifertilizerapp.auth0.com',
    clientID: 'BNgRrUMRvEHWvrnp4ZSd8d6ufuqVRVr4',
    redirectUri: 'http://localhost:8080/callback',
    //redirectUri: 'http://35.200.155.144:8080/callback',
    audience: 'https://agrifertilizerapp.auth0.com/api/v2/',
    responseType: 'token id_token',
    scope: 'openid email profile'
  });

export function login() {
  webAuth.authorize();
}

var router = new Router({
  mode: 'history',
});

export function logout () {
  // Clear access token and ID token from local storage
  localStorage.removeItem('access_token')
  localStorage.removeItem('id_token')
  localStorage.removeItem('expires_at')
  // navigate to the home route
  router.go('home')
}

export function requireAuth(to, from, next) {
  if (!isLoggedIn()) {
    next({
      path: '/',
      query: { redirect: to.fullPath }
    });
  } else {
    next();
  }
}

export function getIdToken() {
  return localStorage.getItem(ID_TOKEN_KEY);
}

export function getAccessToken() {
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

function clearIdToken() {
  localStorage.removeItem(ID_TOKEN_KEY);
}

function clearAccessToken() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
}

// Helper function that will allow us to extract the access_token and id_token
function getParameterByName(name) {
  let match = RegExp('[#&]' + name + '=([^&]*)').exec(window.location.hash);
  return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

// Get and store access_token in local storage
export function setAccessToken() {
  let accessToken = getParameterByName('access_token');
  localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
}

// Get and store id_token in local storage
export function setIdToken() {
  let idToken = getParameterByName('id_token');
  localStorage.setItem(ID_TOKEN_KEY, idToken);
}

export function isLoggedIn() {
  const idToken = getIdToken();
  return !!idToken && !isTokenExpired(idToken);
}

function getTokenExpirationDate(encodedToken) {
  const token = decode(encodedToken);
  if (!token.exp) { return null; }

  const date = new Date(0);
  date.setUTCSeconds(token.exp);

  return date;
}

function isTokenExpired(token) {
  const expirationDate = getTokenExpirationDate(token);
  return expirationDate < new Date();
}


var userProfile;

export function getProfile() {
  if (!userProfile) {
    var accessToken = getAccessToken();
    if (!accessToken) {
      console.log('Access Token must exist to fetch profile');
    }
    webAuth.client.userInfo(accessToken, function(err, profile) {
      if (profile) {
        userProfile = profile;
        store.userProfile = userProfile;
//        var g = []
var g = []
var o = []

        // Call the API to fetch the nutrient details from the DB
        API.fetchUserAccessInfo()
           .then(user_info => {
             g = user_info.user_access
                          var o = _.filter(g,{'email_ID':userProfile.email})
             if (typeof(o[0]) != "undefined"){
               if (o[0].user_access == 'R' || o[0].user_access == 'C'|| o[0].user_access == 'A'){
                 store.super_user_access = true;

              }
             }
            })
           .catch(error => {
             console.error(error);
            })

        // else {
        //   store.super_user_access = false;
        // }
      }
    });
  } else {
    store.userProfile_email = profile.email;
  }
}
