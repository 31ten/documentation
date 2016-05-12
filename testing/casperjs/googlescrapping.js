var casper = require('casper').create();
var links;

function getLinks() {
  var links = document.querySelectorAll('h3.r a');
  return Array.prototype.map.call(links, function(e) {
    return e.getAttribute('href')
  });
}

casper.start('https://google.com/', function() {
  // search for 'casperjs' from google form
  this.fill('form[action="/search"]', { q: 'casperjs' }, true);
});

casper.then(function() {
  // aggregate results for the 'casperjs' search
  links = this.evaluate(getLinks);
});

casper.run(function() {
  for ( var i in links ) {
    console.log(links[i]);
  }
  casper.done();
});