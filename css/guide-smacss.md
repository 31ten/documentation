

## Organization

Categorization helps us develop patterns that can define better practices around each of these patterns.
These categorizations help us ask ourselves two questions:
* how are we ging to code things? 
* why we are going to code it this way

Repition results in less code and makes it easier to maintain with greater consistency in UI

Naming convention is beneficial for understanding which category a style belongs to and it's role within the scope of the page.


There are 5 categories that our CSS will live in:

## 1. Base
+ This is the Default category, and is used exculsively for single element selectors
+ Can include, attribute, pseudo, child, and sibling selectors
+ Should ask ourselves: "whatever this element is on the page, it should look like this"
    ex: html, body, form{margin: 0; padding: 0;}
    input[type=text]}{}
    a:hover{}
    
+ These do not include any classes or id selectors
+ Defining default styling for how that element should look in all occurrences on the page.
+ Includes: settings, heading-sizes, default link styles, default-font styles, body backgrounds.
+ There should never be an !important in the base category
+ CSS reset = base style designed to reset the default margin, paddings, and other properties, builds consistent foundation across browsers to build the site on.


## 2. Layout
+ Divides the page into sections, 
+ Layouts hold one or more modules together
+ Positioning and Placement
+ nameing: -l or  -layout or  grid-
+ ex: .l-inline
        
+ There are major and minor components of a page
+ Minor = callout, login form, navagation item
+ If minor = Module
+ Major = header footer
+ If major = Layout
+ Usually styled with ID's
+ ex: #header #article #footer
+ Major components can also include minor sub-layouts
+ Minor Layout style's will use class names instead of id's so it can be used multiple times on the page
+ usually only a single id or class
    
+ Layouts will be the only primary category to use ID selectors, can also use namespacing if you desire


## 3. Module
+ Reusable, modular parts of our design. callouts, sidebar sections, product lists ect....
+ This will be the bulk of any project
+ Naming: due to the large number of modules we will face, name the modules the name of the module itself
+ Related elements will use the base name as prefix
+ If it is a variation of another module use base name as a prefix
+ ex: .example | .callout | .field

+ These are navagation bars, carousels, dialogs, widgets, the meat of the page.
+ Modules sit inside layout componenets, and can sometime sit within other modules
+ Should be designed to exist as a standalone componenet
+ Can be easily moved to different parts of the layout without breaking it
+ Avoid using id and element selectors, use only class names. 
+ A module will likely contain a great deal of elements and we are not likely to use descendent or child selectors

+ Only include a selector that includes semantics (ex: span or div hold none, heading has some, class of an element has plenty)
+ If an element selector must be used, it should be within one level of a class selector,(should be in a position to use child selectors)
+ These should not confuse elements with other elements
+ Allows us to better understand where contact changes are likely to occur.

+ Subclassing the module will allow the module to be moved to other sections of the site more easily
+ Thus allowing us to avoid increasing the specificity of our elements
+ If changing the look of a module for useage elsewhere on the page or site, subclass-modules are used


## 4. State
+ Ways to describe how our modules or layouts will look when in a particular state. 
+ Is it hidden or expanded, is it active or inactive? 
+ Describes how a module or layout looks on screens that are smaller or bigger
+ Describes how a module might look in different views like the home page or the inside page
+ Naming: .is- | .is-hidden | .is-collapsed |  .callout.is-collapsed

+ A state is something that augments and overrides all other styles
+ Example: an accoridan may be in collapsed or expanded state
+ Generally applied to the same element as a layout rule or applied to the same element as a base module class

+ State and submodule are similar in that they modify the existing look of an element but differ in two ways:
- State styles can apply to a layout &/or module styles, 
- Indicate a Javascript dependency
- Sub-modules are only applied at render and never again
    
+ !important can only be used in state styles but caution must be used and we tend to keep it as a last resort

+ Sometimes a state is very specific to a particular module where styling is very unique
+ If used, state name should include the module name in it

+ State rules should also reside with the module rules and not the rest of the global state rules
+ If doing in-time loading of CSS, generic states should be considered part of the base & global styles & loaded on initial page load

####Changing States
+ Various components are needed to be represented in various states: a default state and alternate state
+ Class name: happens w/ JS via some interacting, moving mouse around, hitting keyboard, or an element receives a new class and then the appearance changes
+ Pseduo-class: done via any number of pseudo-classes, JS not needed
+ Media-query: viewport sizes (iphone4, 5 6, android,  samsung, ..)

+ These three represent a change in state
+ Parent and sibling states are problematic

+ Attribute selectors can be used to handle state change
+ We can use data- prefix to make up attribute names, now we do not need to add classes
+ jQuery also makes it helpful

+ CSS animations: css=style JS=behavior
+ CSS = visual state
+ JS = switches state
    
# Media queries should no longer be placed in it's own place, instead put media queries around the module states,
# Keeping module information together allows for isolated testing of the module 

## 5. Theme
+ Similar to state rules in that they describe how modules or layout might look
+ Most sites won't require this

+ Themes define colors and images that give the app or site it's look and feel. 
+ Necessary when alternate looks or cosmetic alterations are needed

+ Different colours for different sections or even different countries

+ Themes can affect any of the primary types
+ Depends on how large a theme is needed, 
+ Can be kept to theme specific classes or if more intense using theme- prefix so it can be extended to more elements

+ Defining specific rules to isolate font styles makes it easier to change font size across mulptiple componenets.
+ Font rules normally affect base, module and state styles

+ It is common to mix styles within each category, being aware of patterns helps us avoid complexitiy that comes from intertwining these rules.

+ We should not rely heavily on defined html structure
+ Depth of html with selectors ahould not be too deep

+ Depth of applicability is the number of generations that are affected by a given rul
+ ex: body.article > #main > #content >#intro > p > b  = depth of applicability of 6 generations 
+ even: .article #intro b = 6

+ Too much depth enforces greater dependecy on particular html structure
+ Which makes it not as easy to move around components of a page

+ Shallow depth give us the ability to more readily convert modules into templates for dynamic content

+ We don't want or need classes on everything


## How does CSS get evaluated

+ Browsers handle documents like a stream, receive documents from the server and renders documents before it has completely downlaoded.
+ Each node is evaluated and rendered to the viewport as it is received

+ Get's evaluated from right to left
+ 4 ineffficient rules: descendant selectors, child or adjacent selectors, over qualified secletos, apply :hover to non link elements

+ Three simple guidlines to limit the number of elements that need to be evaluated
+ Child-selectors, avoid tag selectors for common elements, 
+ Use class names as the right most selector

+ Increase semantics and decrease reliance on specific html


## Prototyping
+ Patterns establis familiarity and encourage re-use
+ Assits in viewing components in part or in whole and allow the codification of the design language into building blocks. 
+ Goals:
 - show states
 - default-collapsed, error, visulaize  before building
 - use mock data if needed 
 - review localization, if needed to support multiple locales, test layouts
 - isolate dependencies
            


## Preprocessors  
+ Sass and less are the two most commonly used 

+ Allows us to use variables, these will keep site-wide information in one place 
+ aka set color once and reuse variable operations, 

+ Mixins allows us to group styles that can be re-used throughout your css
+ Can take parameters, handles vendor prefixes and reptitive css rules

+ Nesting allows for a cleaner grouping of styles

+ Functions give us the ability to calculate values inside our CSS 

+ Interpolation, file, importing, extending
+ Extend one module with properties of another


+ Minimize deep nesting 
+ In SMACSS nesting only happens when needing to target element selectors in a part of the module
+ Avoid unneccessary extending, do not extend across disparate modules

+ Sass {state based media queries with nesting, belongs with the module ,embed media queris inside other media queries

+ Sass encourages the seperation of concerns that SMACSS recommends
+ Place all base rule into own file
+ Depend on type of layout you have , place all into single file or major layout into speerate files
+ Each module deserves own file
+ Place sub-modules into their own file
+ Global states into own file
+ Layout and module states, including media queries that affect those layouts and modules, into the module file
+ Makes for easier prototyping

+ When you're ready to launch, create a compressed verision of your css for deplooyment

+ Some elements that are not used often despite thinking they may be singular and never changing should not be placed in the base 

+ button = module
+ table = becomes a module
+ input = module
+ icon module = make a module ico

+ Complicated inheritance
+ !important does not override inheritance just specificity

+ There is not a perfect solution to inheritance 

+ Formatting
 - Multiple line
 - Space after colon
 - Four spaces befroe declaration (no tabs)
 - Properties are group by type
 - Opening brack on the same line as rule set
 - Color declaration use the short form

+ Group:
 - Box = any properties that affects the display and posiion, affects flow
 - Border
 - Background =  things like gradients
 - Text
 - Other

+ Most important we must be consistent in our naming conventions and design patterns
    




