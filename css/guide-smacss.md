

## Organization

Categorization helps us develop patterns that can define better practices. The more organized we are in CSS the more maintainable our code will be. This means we do not just want to blindly create CSS we want to have a plan and we want to structure our CSS in a way that allows us to know exactly what this is going to do in this project. 

In order to keep ourselves organized SMACSS recommends 5 categories to place your CSS code in.


These categorizations help us ask ourselves two questions:
* How are we ging to code things? 
* Why we are going to code it this way

When coding CSS we can to write as little code as possible while still meeting the project requirements, to do this we need to find patterns we can repeat, if we can do this it will make it easier to maintain our CSS and it will provide us with greater consistency in UI.

In SMACSS he has developed a naming convention which is beneficial for understanding which category a style belongs to and it's role within the scope of the page. This helps us think about the role our CSS is going to have in this project. It makes sure we are thinking about things first and coding second. The last thing you want when writing CSS is to have an element that needs to be different in one section only to find that overwriting that element is more tedious then expected, or even worse, having to go back and change things you previously coded to make the new style go into effect, all of this wastes times and is not an effective way to code. Therefore by following these 5 categories 1)Base, 2)Layout, 3) Module, 4) State, 5) Theme we can make our code better organized.

Depending on the size of the project the naming convention we choose to use will help a great deal in finding what we are looking for faster. If working on a large project, it is recommended to break up our CSS into multiple files. We can also use a prefix to help us better organize our code. Our naming convention must stay the same and not divert throughout the project, which can be hard if working with a large team. For example if we start using .l- we should only use that from there on out and not change midway to .layout- this makes it confusing and does not follow the repititve schema the author has told us to follow. When naming Modules we should not use a prefix since this will be the bulk of the project, instead the module should be the name of the module itself. Releated elements in the module should use the base name as the prefix, this will help us know where this CSS is being used.



## 1. Base
+ This is the Default category, and is used exclusively for single element selectors
+ They can also include, attribute-selectors, pseudo-class selectors, child-selectors, and sibling selectors
+ When using the Base category we should ask ourselves this question before coding: "whatever this element is on the page, it should look like this"    
+ The Base category does not include any classes or id selectors.
+ The base is used for defining default styling, or another way to think of it is this is how that element should look in all occurrences on the page by default, if I need to change it later I will put that in another section of my CSS code.
+ Base Style Examples: heading-sizes, default link styles, default-font styles, body backgrounds.
+ He also recommends specify the body background to ensure color schema does not break later on in the project.
+ There should never be an !important in the base category
+ CSS reset = base style designed to reset the default margins, paddings, and other properties, this helps us build consistent foundation across browsers to build the site on.
+ There are many CSS reset frameworks such as normalize.css but there are pro's and con's to using these frameworks. Some can be too aggressive and can create more problems then intended.


## 2. Layout
+ Layous help divides the page into sections by creating the Major components of the site such as a header or footer. 
+ Layouts hold one or more modules together, for example a login form, or navigation item sit inside the scope of the major component header or footer. Therefore we call these major components the layout and those that fit inside the major components, modules or minor components.
+SMACSS reommends we use ID selectors, but it is also ok to use classes if the project calls for it.
+ We can use classes when there are common styling across components of the page
+ It is important to note that Layouts will be the ONLY primary category to use ID selectors, we can also use namespacing if project size is big enough.
+ When creating Layouts all we care about is how each item relates to each other, we do not need to worry about design of modules or the context the layouts sits within.


## 3. Module
+ Modules are the reusable, modular parts of our design such as the navigation bars, our callouts, sidebar sections, product lists carousels, dialogs, widgets and so on.
+ Modules will be the bulk of any project.
+ As mentioned in the Layout section, Modules sit inside layout componenets, and can sometime sit within other modules
+ However, Modules should be designed to exist as a standalone componenet so they can be easily moved to different parts of the layout without breaking it
+ We need to avoid using id and element selectors, and try to use only class names. 
+Modules allows us to better understand where context changes are likely to occur throughout our project.
+ A module will likely contain a great deal of elements so we are likely to use descendent or child selectors.
+ If an element selector must be used, it should be within one level of a class selector,(should be in a position to use child selectors)
+ Modules should not confuse elements with other elements
+ Allows us to better understand where contact changes are likely to occur.
If we have the same module in different sections we should subclass it and style it accordingly, when we subclass it should look like this in our CSS: .moduleName-subclassName
+ Subclassing the module will allow the module to be moved to other sections of the site more easily. This is especially useful if we want to change the look of a module that is found in other locations on the page or site.
+ Thus allowing us to avoid increasing the specificity of our elements
+ If changing the look of a module for useage elsewhere on the page or site, subclass-modules are used


## 4. State
+ The State is a ways to describe how our modules or layouts will look when in a particular 'state'. 
+ Such as, is it hidden or expanded, is it active or inactive? Each of these show the element being displayed in a specific way.
+ States can also describe how a module or layout should look on screens that are smaller or bigger via Media Queries
+ Stats can also describes how a module might look in different views like the home page or the inside page
+ When we name states we should use the prefix is, for example: .is- | .is-hidden | .is-collapsed |  .callout.is-collapsed
+ A state is something that augments and overrides all other styles
+ Think of an accoridan being in either a collapsed or expanded state.
+ States are generally applied to the same element as a layout rule or applied to the same element as a base module class.

+ State and submodule are similar in that they modify the existing look of an element but differ in two ways:
- State styles can apply to a layout &/or module styles, 
- Indicate a Javascript dependency
- Sub-modules are only applied at render and never again whereas State styles are applid to elements to show a change in state while the page is still running.
+ !important can only be used in state styles but caution must be used and we tend to keep it as a last resort
+ Sometimes a state is very specific to a particular module where styling is very unique, if used in a module then the state name should include the module name in it
+ State rules should also reside with the module rules and not the rest of the global state rules
+ If doing 'in-time' loading of CSS, generic states should be considered part of the base & global styles & loaded on initial page load, this allows the CSS for a particular module to load only when the module is needed

####Changing States
+ When dealing with States various components are needed to be represented in various states such as a default state and an alternate state. There are three ways we can represent these changes.
- 1) Class name: This will happen with JS via some interaction, such as moving the mouse around, hitting thekeyboard, or an element receives a new class thus making the appearance change.
- 2) Pseduo-class: This is done via any number of pseudo-classes, JS not needed
- 3) Media-query: viewport sizes (iphone4, 5 6, android,  samsung, ..)
+ These three represent a change in state
+ When creating State styles keep in mind that creating Parent and/or sibling states are problematic try to avoid doing this as much as possible.
+ Instead of creating classes we can also use Attribute selectors can be used to handle state changes
+ For example, We can use the data- prefix to make up attribute names, now we do not need to add classes
+ jQuery also makes it helpful
+There are three ways we can create State Changes:
- 1) CSS animations: css=style JS=behavior
- 2) CSS = visual state
- 3) JS = switches state
    
+ Media queries should no longer be placed in it's own place, instead put media queries around the module states.
+ Keeping module information together allows for isolated testing of the module 

## 5. Theme
+ Themes are similar to state rules in that they describe how modules or a layout might look, but differ in that Themes are more about the look and feel of the site in general and not a specific element changing based on a user's action.
+ Themes are not always used and most sites won't require this.
+ Themes help us define colors and images that give the app or site it's look and feel. This is necessary when alternate looks or cosmetic alterations are needed.
+ This allows us to seperate the theme out into its own set of styles which make it easier to redfine for alternate themes
+ Themes for example can be different colours for different sections or even different countries.
+ Themes can affect any of the primary types and can override base styles.
+ Themes can also change module elements such as colors or borders and can affect layout with different arrangements.
+ Themes can also alter how states look.
+ Can be kept to theme specific classes or if the project is more intense it can use a theme- prefix so it can be extended to more elements.
+Themes are also good at helping us define out fonts
+ Defining specific rules to isolate font styles makes it easier to change font size across multiple componenets.
+ Font rules normally affect base, module and state styles and are not normally specificed at the layout level.


## Tips 
+ It is common to mix styles within each category, being aware of patterns helps us avoid complexitiy that comes from intertwining these rules.
+ We should not rely heavily on a defined html structure
+ Depth of html with selectors ahould not be too deep
+ We don't want or need classes on everything

#Depth of Applicability
+ Depth of Applicability is the number of generations that are affected by a given rul
- ex CSS: body.article > #main > #content >#intro > p > b  = depth of applicability of 6 generations 
- Using the same example of above and shortening it to : .article #intro b = still equals a depth of applicability of 6 generations.
+ Too much depth enforces greater dependecy on a particular html structure, which makes it not as easy to move around components of a page
+ Shallow depth give us the ability to more readily convert modules into templates for dynamic content


## How does CSS get evaluated
+ Browsers handle documents like a stream, receive documents from the server and renders documents before it has completely downlaoded.
+ Each node is evaluated and rendered to the viewport as it is received
+ Get's evaluated from right to left
+ CSS has 4 rules they consider inefficient: 
-1)descendant selectors = #content h3
-2) child or adjacent selectors = #content > h3
-3) over qualified secletors, = div#content > h3
-4) apply :hover to non link elements = div#content:hover
+ These recommendations should not be taken too seriously because if we follow this verbatim then any evaluation more than a single element is considered inefficient.
+ To make a better guideline try using these four simple guidlines to limit the number of elements that need to be evaluated
- 1) Use Child-selectors
- 2) avoid tag selectors for common elements, 
- 3) Use class names as the right most selector
- 4) Increase semantics and decrease reliance on specific html
+ All in all we should consider selector performance but not waste too much time on it


## Prototyping
+ When we are creating our CSS we need to first find patterns because they will help us establish familiarity and encourage re-use throughout our project.
+ This will assist us while viewing components in part or in whole and allow the codification of the design language to be placed into building blocks. 
+ Prototyping Goals Should include:
 - what will our default styles be for this project
 - how will we show our states for this project
 - what mock data do we need to include so we can visulaize our CSS designs without having to have a finished product
 - do we need to review localization to support multiple locales
 - will we need to create any test layouts
 - Lastly we need to isolate dependencies, meaning what CSS and JS are required to render this module correctly.
            

## Preprocessors  
+ Sass and less are the two most commonly used preprocessors on the market
+ These preprocessors allow us to use variables, which will keep site-wide information in one place allowing re-use 
- such as setting a base color once and then reusing the variable whenever needed 
- They also allow us to use Mixins, which allow us to group specific CSS styles together that can then be re-used throughout our CSS.
- Can take parameters, which handle vendor prefixes and reptitive CSS rules
- These preprocessors also allow us to use Nesting for a cleaner grouping of styles
- They also come with Functions that give us the ability to calculate values inside our CSS 
- Interpolation 
- File importing
- Extending one module with properties of another
+ We want to Minimize deep nesting as much as possible
-In SMACSS nesting only happens when needing to target element selectors in a part of the module
+ Avoid unneccessary extending, do not extend across different modules
+ When using Sass we will place state based media queries within our nesting, these will belong with the module category, and we should also embed media queries inside other media queries
+ Sass encourages the seperation of concerns that SMACSS recommends
- Place all base rule into own file
- Depending on the type of layout you have, if a small project then we should place all into single file, or if a larger project then we should place each cateogry into speerate files
- Each module deserves own file
- Place sub-modules into their own file
- Global states into own file
- When dealing with States, for Layout and module states, including media queries that affect those layouts and modules, should be placed into the module file
+ This will make it easier for prototyping.
+ When you're ready to launch, create a compressed version of your CSS for deployment

## Final Advice
+ Some elements that are not used often despite thinking they may be singular and never changing should not be placed in the base 
+ Avoid complicated inheritance
+ !important does not override inheritance just specificity
+ There is not a perfect solution to inheritance 
+ The best way to format our CSS
 - Multiple lines
 - A Space after the colon
 - Four spaces before declaration (no tabs)
 - Properties are group by type
 - Opening bracket on the same line as the rule set
 - Color declarations should use the short form

+ Not important but we can also group by properties which are the most important to the least important
+ SMACSS recommends organizing in the following order
 - 1) Box = any property that affects the display and posiion of the box. Such as display, float, position, height, width. This is most important because it affects the flow of the document
 - 2) Border = the border-radius or border-images
 - 3) Background =  things like gradients,
 - 4) Text = font-family, font-size, text-transform
 - 5) Other = anything that does not fall into the above 4 gets placed in other and should be included at the end.
+ No matter if we follow all of these rules verbatim the most important thing we need to take from our design is that we must be consistent in our naming conventions and design patterns. This consistency will allow us to code faster and more efficiently. 
    




