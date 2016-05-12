var page = require('webpage').create();
page.open('http://puwei-property.cn/', function() {
		page.render('github.png');
		phantom.exit();
		});
