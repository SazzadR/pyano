const mix = require('laravel-mix');

mix.copyDirectory('node_modules/open-iconic/font/fonts', 'resources/static/fonts');

mix.styles([
    'node_modules/bootstrap/dist/css/bootstrap.css',
    'node_modules/open-iconic/font/css/open-iconic-bootstrap.css',
], 'resources/static/css/vendors.css');

mix.styles([
    'resources/assets/css/app.css'
], 'resources/static/css/app.css');

mix.scripts([
    'node_modules/jquery/dist/jquery.js',
    'node_modules/bootstrap/dist/js/bootstrap.js'
], 'resources/static/js/vendors.js');
