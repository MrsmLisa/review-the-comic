# Review the comic

## Project Goals
Review the Comic is a community platform for comic book enthusiasts to share their thoughts on graphic novels. Users can create reviews, comment on others' posts, and like their favourite reads. The site is designed to be clean, accessible, and easy to navigate on both mobile and desktop.
---
## User stories

### Admin

  * As an admin i can view, create, edit and delete all the material and have full control over the website.

### Navigation

  * As a user I can understand what the sites purpose is.  
  * As a user I find the site easily navigated and understandable.  
  * As a site user, I can view a paginated list of posts so that I can select which post I want to view.  
  * As a user I can click on a review and see the full text of the review post.  
  * As a user I can comment on the reviews and like the posts.  
  * As a logged in user I can save a draft post to finish later.  

### Reviews 

  * As a user I can create my own reviews so others can view them.  
  * As a user I can fully edit my own posts, change the texts and images.  
  * As a user I can delete a review if I need it.  

### Interactions

  * As a user I can like and unlike other reviews.   
  * As a user I can leave a comment for the other users.  
  * As a user I can see other users comments and likes.  

### Account

  * As a user I can easily register an account.
  * As a user I can easily delete my account.

## Planning:

### Agile Methodology
  * I have used project planning in GitHub for this project.

### Design
I viewed many different review websites, both book and comic reviews, and found most of them plain with few colors. I decided to use the way a comic page look when you read it with squares in a grid. 

### Colourscheme
To continue with the comic book page theme I have only used black and white for the the website. Just having it black and white makes the book covers stand out more with pops of color.

### Typography
For the headlines I used Luckiest guy and for the plain text and smaller headlines I used SN Pro.

### Imagery
The logo was made by me with the speech bubble taken from Freepik. I used the same font as the headlines for the site.
There are no images on the site exept for the cover images that users put in. For this site I have used images taken from [Sci-Fi bokhandeln](https://www.sfbok.se/). They get their images from the pubishing companies. 


### Wireframe
As i wanted to make the site look like a comic page I wanted the review …. to be square and built it after that. 
I used whimsical to build the mockup.

### Database Diagram
I used ….. to build the schema and is as follows.
---

## Features:

### Home page:

 * Nav bar
   - The navbar stays at the top of the page so the user can easily navigate where ever they are on the site.
   - The logo at the top takes you back to the 'home' page.
   - I only have a toggle for a cleaner look. To reach the 'create review' you have to use the toggle.

 <img width="633" height="70" alt="nav" src="https://github.com/user-attachments/assets/29c79572-81ae-4e7b-8fcf-48362708404a" />


 * Hero
   - The first thing the user sees is 'Welcome to review the comic' so the user knows directly what the site is about.
   - The hero is only present on the 'home' page. On the other pages the user only sees the navbar.

<img width="757" height="215" alt="hero" src="https://github.com/user-attachments/assets/f48835f4-b38e-466b-8928-f1841bbacbf4" />

   
 * Cards
   - Every card contains a picture of the cover, the book title, the authors name, an exerpt of the book and the date the review was created.

<img width="794" height="228" alt="cards" src="https://github.com/user-attachments/assets/74c4782e-df16-4851-aaf0-8208025e1bb3" />


 * Review page
   - When the user clicks the card they are moved to the review page that shows the longer review.

<img width="318" height="738" alt="review" src="https://github.com/user-attachments/assets/fccdc0ae-8e27-4662-8ca6-3643bd96735c" />


 * Footer

### Interactivity:
For all these activities the user have to be logged in

 * Make a review
   - The user can make their own review.

<img width="310" height="727" alt="leave-review" src="https://github.com/user-attachments/assets/90818d25-3b53-4753-9d3b-ebd2b1dde047" />


 * Comment on a review
   - The user can comment on any of the reviews.
   - When there is no review there is a text prompting to leave one.

   <img width="351" height="322" alt="comment" src="https://github.com/user-attachments/assets/a7c7df70-4644-4657-821f-77fcba13d3a3" />

<img width="370" height="156" alt="comment-made" src="https://github.com/user-attachments/assets/12cc8e97-f97f-45a9-a226-be7a09f6a712" />


   <img width="373" height="78" alt="no-comment" src="https://github.com/user-attachments/assets/a6cca04a-5179-4081-a0de-31a8c10fc5ff" />

 
 * Edit/ delete
   - The user can both edit and delete their reviews.
   - If they delete there is a message to make sure they meant to delete.

<img width="295" height="124" alt="edit_delete" src="https://github.com/user-attachments/assets/a30ff457-e01c-4515-ad01-9a2aeb00599d" />

     
 * Success messages
   - There is a success message when .....
 
<img width="600" height="203" alt="Namnlöst-1" src="https://github.com/user-attachments/assets/5ca19d51-222b-46d6-a82c-76e6bcc1dd2a" />

     
 * Like or unlike a review
   - The user can like or unlike a review.
   - There is a counter to show how many likes a review has.
     
 <img width="92" height="85" alt="no-like" src="https://github.com/user-attachments/assets/fd6dc813-a7a1-4586-9151-b25405842355" />
<img width="92" height="85" alt="like" src="https://github.com/user-attachments/assets/7e270bd2-63a4-4594-8285-3efe2c9e2297" />


### Accounts:

 * Sign up

<img width="346" height="312" alt="sign-up" src="https://github.com/user-attachments/assets/1224cd83-edbd-4463-8573-f93d0790aa80" />

   
 * Sign in
   
<img width="332" height="275" alt="sign-in" src="https://github.com/user-attachments/assets/cabd8550-78a1-4def-b6d9-e08d8de2733d" />

   
 * Log out

<img width="307" height="228" alt="log-out" src="https://github.com/user-attachments/assets/709709ca-ce28-4615-a246-7170774513f7" />


### Future implements
 * A rating system where the reviewer can mark on a scale their view of the comic.  
 * Make a user profile page where they have more control over their interactions.  
 * Have a Comic of the week as a special feature.  
 * Put in more categories in the review-detail. For example genre, publisher and ISBN.  
 * Send out a email verification upon sign up.
 * A chat between members.

---
## Technologies:

### Language used
HTML  
CSS  
Python  

###Library and programs used

Git - for version control.  
GitHub - for storing code and deploying site.  
VS Code - to build the project  
Django - a python based framework to develop this project.  
Bootstrap - for HTML design templates  
Cloudinary - to store images  
Whimsical - to make the mockup design  
Heroku - for deploying the project  
SQL - database through Heroku  
W3C - for validation of HTML and CSS  
Pythontester - for validation of Python  
Summernote - for usage in the admin panel  

---
## Testing:

Validators
User stories testing
Feature testing
bugs
Gunicorn and Heroku
Not showing comments
CSS not updating
Wloudinary would not work		

---
## Deployment:

This website is deployed to Heroku from a GitHub repository, the following steps were taken:  

### Creating Repository on GitHub

1. First make sure you are signed into Github and go to the code institutes template, which can be found here.
2. Then click on use this template and select Create a new repository from the drop-down. Enter the name for the repository and click Create repository from template.
3. Once the repository was created, I clicked the green gitpod button to create a workspace in gitpod so that I could write the code for the site.

### Deploying through Heroku

1. Log in to [Heroku](https://www.heroku.com/)
2. From the main Heroku dashboard select 'new', and 'create new app'
3. Name your project, and select a suitable region. After this press 'create app'. (The name you choose must be unique)
4. Previous step creates the app in Heroku and will bring you to the deploy tab. From the menu at the top you want to navigate to the resources tab. 
5. After this you want to add the database to the app, you do this by going to the add-ons section and search for 'Heroku Postgres', select the package that appears and add it to the database. 
6. Navigat3e to the settings, inside config vars you want to add the DATABASE_URL to the clipboard for the Django config. 
7. Create a new file in GitPod called env.py and inside set your environment table for the DATABASE_URL and paste in the copied address from Heroku. 
8. I created a secret key by adding SECRET_KEY in my env.py file, and in heroku. To get the secret key i typed 'openssl rand -base64 16' in my terminal. One time for a secret key to Heroku and a second time for a secret key to add in GitPod. 
9. Create an account in Cloudinary, or log in if you already have an account. The url is found on your dashboard in your account. Copy this and add to your env.py file. 
10. Paste it also into your Heroku config vars. 
11. You now need to add 'KEY - DISABLE_COLLECTSTATIC' with the value of 1 to the config vars in Heroku, this line must be removed before final deployment of the project. 
12. In GitPod you now have to add the cloudinary libraries to the list of installed apps in the settings file. The order here is important, 'cloudinary_storage' must go above 'django.contrib.staticfiles' and then 'cloudinary' goes below. 
13. For your settings.py file you must also add the STATIC files, the url, storage path, directory path, root path, media url and the default file storage path. 
14. You link this to the templates directory in Heroku with 'TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')'
15. You also need to add new folders in GitPod. Create media, static and template folders and a file at the top level namned Procfile (the P has to be capital - important!)
16. Inside the Procfile you need to add following: web: guincorn bakemeacake.wsgi.
17. After adding these files, commit and push these changes to GitHub.
18. In Heroku, go to the deployment tab and deploy this branch manually. This will lead to Heroku building this app for you, and you will be able to follow the build process in the window. 
19. When successful, you will be displayed with following: "Your app was successfully deployed".

---
## Credits:

### Code 
There are a few instances where I have used code where I struggled.  

For [Like and Unlike](https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg) as well as [Edit and Delete](https://dev.to/rishav_upadhaya/day-9-adding-edit-delete-features-to-my-blog-project-li6) I used code from dev.to to get it to work. I found his code easier to understand for me then the schools code.  

I had some problem with getting my success messages to work and used the [Django documentation](https://docs.djangoproject.com/en/1.11/ref/contrib/messages/ ).  

My site moved from side to side and [stackflow](https://stackoverflow.com/questions/44667161/page-moving-left-and-right-while-in-mobile-browser) provided the CSS code.  

### Content
For all the text and cover images in the reviews I have used text from [Sci-Fi Bokhandeln](https://www.sfbok.se/). They get the text (blurb) and images from the pubishing companies.

---
## Acknoledgements	
Marko
Jessica and Stephen Duffy   
Discord community


