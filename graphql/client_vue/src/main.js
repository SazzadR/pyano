import Vue from 'vue';
import VueRouter from 'vue-router';
import ApolloClient from 'apollo-boost';
import VueApollo from 'vue-apollo';
import App from './App.vue';
import Home from './components/Home';
import Books from './components/Books';
import BookDetails from './components/BookDetails';
import Authors from './components/Authors';
import AuthorDetails from './components/AuthorDetails';

Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(VueApollo);

const apolloClient = new ApolloClient({
    uri: 'http://127.0.0.1:8000/graphql/'
});

const apolloProvider = new VueApollo({
    defaultClient: apolloClient
});

const routes = [
    {path: '', component: Home},
    {path: '/books/', component: Books},
    {path: '/book/:id', component: BookDetails},
    {path: '/authors/', component: Authors},
    {path: '/author/:id', component: AuthorDetails}
];

const router = new VueRouter({routes});

new Vue({
    router,
    apolloProvider,
    render: h => h(App),
}).$mount('#app');
