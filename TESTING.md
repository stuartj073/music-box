# Testing

## Manual Testing

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
![Remember me](/docs/readme/testing/home-page.png)

- The home page encompassed a few errors upon being passed into the validator.
Firstly, the href attribute for the categories page under the products nav link was throwing an error due to a space in the href. This was fixed by changing the href links to be that of the 'friendly_name' of the categories.
The 'i' closing tag was removed from the Register link. 
The button element was removed from the 'see our products' link leaving only the anchor tag along with it's styling.
The type attribute from the script tags were also removed.








