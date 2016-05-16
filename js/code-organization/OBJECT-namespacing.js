/**
* Namespacing is a system to organize our js code within one single object.
* Advantages are various : 
*  - Easy debug (console.log(App) here), 
*  - Better code organization (we usually place all the variables and functions within the same file)
*  - Stable and simple variables and functions scope : everything can be called everywhere
*
* This is a coding organization standard at 31TEN
*/

/**
* 1) We declare here our namespacer and its different categories
*/

var App = {};
App._intro = "This is the Namespacer of the current App, you will find here the currently used var in the app, the different custom functions and events available and the content of the website";
App.functions = {};
App.vars = {};
App.content = {};
App.events = {};

/**
* 2) Function declaration example
*/

App.functions.sayHello = function (name){
  return "Hello "+ name;
}


/**
* 3) Variables declaration example
*/

  App.vars = {
        clientUserAgent : navigator.userAgent,
        environment : "development",
        compatibilityMode : "",
        forceCompatibilityMode : 0  ,
        urlParams : App.functions.getQueryString(),
        language : "",
        defaultLanguage : "zh",
        currentPage : "",
        pagesTransition : "css",
        firstPage : "login",
        prerollLoadingTime : 3000,
        splashscreenTime : 4000,
        postrollLoadingTime : 8000,
        errorDisplayTime : 2000,
        countryCodeDisplayTimeStartup : 3000,
        loadingTimeButton : 1000,
        leavingPageTime : 3000,
        leavingPageUrl : "http://www.shairport.com/",
        debugMode : 0,
        myName: "greg"
    };

/**
* 4) Easy debug 
*/
Console.log(App)

/**
* 5) Calling
*/

// A function
App.functions.sayHello("developer") // Output "Hello developer"

// A variable 
alert(App.vars.myName) // Create an alert with "greg" inside

// A function using a namespaced variable
App.functions.sayHello(App.vars.myName) // Output "Hello greg"
