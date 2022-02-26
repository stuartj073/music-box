# Testing

## Manual Testing

Throughout the project I maintained a steady and constant method of testing the sites functionality. From responsiveness to all javascript and python functions, I was always ensuring that links, buttons and pages were behaving as expected.

Each page had specific functionality I wanted enacted throughout them and the following pages were tested and ensured that everything was working as was up to date for the project.

#### Home Page
- The link to the products page was working as expected.
- All navbar elements were rendering subsequent pages as expected.
- When logged out/unregistered the `Log in & Register` links were displayed in the top right of the navbar.
- When logged in the `Basket` feature will be displayed in the top right of the navbar (dependent on whether the basket was populated with goods or not) as was the `Profile icon`.
- The `Back to top` link in the footer was working and prompted me to return to the top of the screen whenever executed.

#### Log in page
- Returning visitors that have checked the `remember me` button for logging in will avail of the auto-fill feature for signing in.
- The respective sign in and remember me links prompt the user to be logged in or to submit a request to change their password.

#### Products page
- The products page displayed all relevant products along with their respective links to the individual product details page along with the category name which will render all products associated with that category to the products page.
- All category headings were working.
- The sort products button worked as expected
- The search bar effectively returned any product associated with the search as well as returning a `No products matched your query` response for empty search results.
- When the admin was logged in the add product button will be rendered on the page.

#### Checkout page
- A users details will be auto-filled when filling out the form if they have already provided information on the site for previous orders or if they have successully saved their shipping information on their profile page.

#### Individual product page
- When logged in, the user will have the option of adding the product to the basket through the input form (as well as choosing the quantity of each item).
- If logged in as super user the edit and delete buttons associated with the product will too appear along with the modal for the delete button to add extra protection against accidentally removing an item.
- If not logged in, the `sign in` option will display for visitors.

#### Add products page
- When all relevant fields were filled out and the form was submitted a success message will appear as well as the product being entered to the site.
- The cancel button also worked in bringing the user back to the products page.

#### Edit product
- Edit product page is only accessible if logged in as super user, which was reflected in the results.
- After successfully editing a product a success message will appear signalling the product had been successfully updated.
- The cancel button also worked in bringing the user back to the products page.

#### Product Reviews
- All users have access to the product reviews page.
- Reviews will render on the page with working links to their respective individual review pages. If there were no reviews associated with a product then an empty search will be rendered, as was reflected in the results. 
- If logged in as super user the delete modal will appear with the option to either go through with the deletion of the review or to cancel and drop down the modal.

#### Add Review 
- When all relevant fields were filled out and the form was submitted a success message will appear as well as the review being entered to the site.
- The cancel button also worked in bringing the user back to the products page.

#### Blogs
- All blogs were rendering as expected on the site.
- If logged in, the `add blog` button will appear for the user as well as the link to sign in if a visitor wished to create a blog entry.
- The links to the individual blog entries were working as expected.


#### Individual blog page
- If not logged in the user will only be able to see the blog entry along with the comments associated with the said entry. A link will also be displayed prompting the user to the login page if they wished to comment on a blog entry post.
- If logged in a form will be displayed underneat the blog entry and comments allowing the user to freely respond to the blog entry in question.

#### Profiles page
- If logged in the user will have access to their own personal profile page accessible in the top right of the nav element.
- All past order details and reviews associated with the user will display on the page as well as their own shipping details which they can update whenever they please.

#### Edit Review

### User Stories

- To see the products and/or categories available to me for purchase.

- See a written backdrop to the site and the see the main ethos of the site.

Upon landing on the home screen of the music box site an about section will be situated just underneath the landing page image. This will fully explain the what it is the site is all about

 ![Ethos](/docs/readme/readme-images/ethos.png)

- Have the option of signing up/ registering.

All visitors to music box will have the option (on every page) to log in/ register from the navigation panel at the top of the page. When certain features of the site require authentication, links will be provided to send the user to the designated page for loggin in/registering also.

![Login](/docs/readme/readme-images/login.png)

- To scroll/navigate the site with ease.

To allow users can scroll each page with ease I have ensured that each page doesn't fall victim to information overload and that each page only required one dial down on a mouse to get to the bottom and vice versa for the top. I have also implemented a 'back to top' button which is located in the footer of each page.

![Scroll with ease](/docs/readme/readme-images/back-to-top.png)

- I want to be able to sign in easily and have my details remembered.

When a returning visitor is logging back into their account, auto-fill will be enabled so that their details will be remembered each time they enter the page allowing for a stress free log in process. 
This action will be enabled upon clicking the 'remember me' button.

![Remember me](/docs/readme/readme-images/remember-me.png)

- To be able to interact with the site's basket feature.

User's to the site wishing to purchase items can interact freely with the basket feature choosing not only to add an item to the basket but also choosing what quantity, size and can remove/specify each item in the basket to their desired need.

![Basket](/docs/readme/readme-images/remember-me.png)

- I want to have access to my own profile page.

When a user is logged in they will be given access to their individual profile page. The profile icon, located in the top right of the navbar element will direct the user to their own page which will also provide them with their order history and record of their site interactions (i.e blog entries, reviews).

![Profile](/docs/readme/readme-images/profile.png)

- I want to be able to perform CRUD operations on any feature of the site where appropriate.

For products, blog entries, comments and reviews users will be able to perform all CRUD operations for pieces of data they have created themselves. Admin will also have access to these privelleges.

![CRUD](/docs/readme/readme-images/crud.png)

- I want to have/see feedback for every action I perform on the site.

Using the in-built django 'toasts' feature I have created by own custom toast message that will appear and disapear after a few seconds. The message will appear for every edit/delete and upload a user makes.

![Toasts](/docs/readme/readme-images/toasts.png)

- To upload items/reviews/blog posts onto the site.

Located on each relevant page will include the option for a user to contribute with their own data. Below is an example of how a user can upload a blog to the site.

![Blog](/docs/readme/readme-images/blogs.png)

- I want to have control over all user's actions on the site.
- I want to ensure all information provided on the site is just and correct.

Admin privelleges include the overall control of all content created and uploaded to the site. Each page that has any data of any kind is available to be edited and deleted by admin.

![Admin](/docs/readme/readme-images/admin.png)


## Automated Testing

### W3C Validator

I utlised the W3C validator to ensure every page on the site was up to standard and that there was no html errors left unturned.

1. Home page
![Home](/docs/readme/testing/home-page.png)

- The home page encompassed a few errors upon being passed into the validator.
Firstly, the href attribute for the categories page under the products nav link was throwing an error due to a space in the href. This was fixed by changing the href links to be that of the 'friendly_name' of the categories.
The 'i' closing tag was removed from the Register link. 
The button element was removed from the 'see our products' link leaving only the anchor tag along with it's styling.
The type attribute from the script tags were also removed.

2. Products/shop page
![Products](/docs/readme/testing/home-page.png)

- The products page displayed the same javascript 'type' attribute error as the home page. This was removed and the error was then eradicated.

3. Add product page
![Add product](/docs/readme/testing/add-product.png)

4. Product details page
![Product details](/docs/readme/testing/product-details.png)

5. Edit product page
![Edit product](/docs/readme/testing/edit-product.png)

6. Product reviews
![Product reviews](/docs/readme/testing/product-reviews.png)
- The 'h2' heading was removed for the empty heading warning.
The extra closing 'section' tag was removed.

7. Individual Review
![Ind review](/docs/readme/testing/ind-review.png)

8. Edit review
![Edit review](/docs/readme/testing/edit-review.png)

9. Blogs
![Blogs](/docs/readme/testing/blogs.png)

10. Update Blog
![update blog](/docs/readme/testing/update-blog.png)

10. Basket
![Basket](/docs/readme/testing/basket.png)

11. Checkout
![Checkout](/docs/readme/testing/checkout.png)

12. Checkout success
![Checkout success](/docs/readme/testing/checkout-success.png)
- This error was in relation to a heading I had copied over from another template in reference to a product object which had not been defined in the checkout success view and thus rendered an empty h6 heading. The heading was removed.

### JSHint Validator

- Base.js
![Base js](/docs/readme/testing/stripejs1.png)

The '$' warnings was ignored as these are required to write jQuery functions.

- Stripe.js

![Stripe js 1](/docs/readme/testing/stripejs1.png)
![Stripe js 2](/docs/readme/testing/stripejs2.png)

The same steps were taken as base.js and the 'Stripe' variable warning was ignored as this is required by stripe to authorize paymetns.

The 'template literal syntax' issue was fixed as I included the snippet '/*jshint esversion: 6 */'
at the top of the file. This was to allow JSHitn to recognise ECMAScript 6 features it otherwise wouldn't.

- Basket.js

![Basket](/docs/readme/testing/stripejs2.png)

The missing semi-colons were added.

- Quantity selector script

![Quantity](/docs/readme/testing/quantityjs.png)

The console.log statements were removed from the file. 



