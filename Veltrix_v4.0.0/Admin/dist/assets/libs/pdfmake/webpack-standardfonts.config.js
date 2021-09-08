<<<<<<< HEAD
var config = require("./webpack.config.js");

var rule = {enforce: 'post', test: /pdfkit[/\\]js[/\\]/, loader: "transform-loader?brfs"};

config.module.rules.push(rule);

=======
var config = require("./webpack.config.js");

var rule = {enforce: 'post', test: /pdfkit[/\\]js[/\\]/, loader: "transform-loader?brfs"};

config.module.rules.push(rule);

>>>>>>> b72c5ea86bf6885e302b926b7202718cf917849d
module.exports = config;