/** GLOBALS **/

/** INIT **/
var casper = require('casper').create({
    verbose: true,
    logLevel: "debug"
});

/** FUNCTIONS **/

// Start to check if the page exist by returning the Title
casper.start('http://139.196.242.67/contact-us', function(){
    this.echo(this.getTitle());
});

// Wait until the page is loaded then fill the form and finaly submit it
casper.waitForResource("http://139.196.242.67/contact-us", function() {
  this.fillSelectors('form[name="form-contact-us"]', {
      '#prenom': 'ROBOT_TEXT_TEST_FOR_NAME',
      '#nom': 'ROBOT_Surname',
      '#email': 'sofiane@31ten.network',
      '#message': 'Message text'
  }, true);
});

/** HANDLER **/

casper.run();
