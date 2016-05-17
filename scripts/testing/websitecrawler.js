var links;
// 1st version
// casper.start('http://139.196.242.67/');
//
// casper.then(function getLinks(){
//      links = this.evaluate(function(){
//         var links = document.getElementsByTagName('a');
//         links = Array.prototype.map.call(links,function(link){
//             return link.getAttribute('href');
//         });
//         return links;
//     });
// });
// casper.then(function(){
//     this.each(links,function(self,link){
//         self.thenOpen(link,function(self, a){
//           //this.echo(this.getCurrentUrl());
//             //this.echo(this.getTitle());
//             self.thenOpen(link, function(self, a) {
//               this.echo(this.getTitle());
//             });
//         });
//     });
// });
//
//
// casper.run(function(){
//     this.exit();
// });


// 2nd version with test assert
// casper.test.begin('Checking PVI website http code', 1, function(test) {
//     casper.start('http://139.196.242.67/').then(function getLinks(){
//          links = this.evaluate(function(){
//             var links = document.getElementsByTagName('a');
//             links = Array.prototype.map.call(links,function(link){
//                 return link.getAttribute('href');
//             });
//             return links;
//         });
//     }).then(function(){
//         this.each(links,function(self,link){
//             self.thenOpen(link,function(self, a){
//               this.echo(this.getCurrentUrl());
//               this.echo(this.getTitle());
//               test.assertHttpStatus(200);
//             });
//         });
//     }).run(function() {
//         test.done();
//         this.exit();
//     });
// });


var links;
casper.test.begin('Checking PVI website http code', 1, function(test) {
    casper.start('http://139.196.242.67/').then(function getLinks(){
         links = this.evaluate(function(){
            var links = document.getElementsByTagName('a');
            links = Array.prototype.map.call(links,function(link){
                return link.getAttribute('href');
            });
            return links;
        });
    }).then(function(){
        this.each(links,function(self,link){
            self.thenOpen(link,function(self, a){
              this.waitForResource(link, function() {
                this.echo(this.getTitle());
                this.echo(this.getCurrentUrl());

                test.assertHttpStatus(200);
              });
            });
        });
    }).run(function() {
        test.done();
        this.exit();
    });
});
