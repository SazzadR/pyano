const mix = require('laravel-mix');

mix.styles([
    'node_modules/bootstrap/dist/css/bootstrap.css'
], 'resources/static/css/vendors.css');

mix.styles([
    'resources/assets/css/app.css'
], 'resources/static/css/app.css');
