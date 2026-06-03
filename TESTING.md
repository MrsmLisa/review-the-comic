# Review the comic - Testing

## Content

Validators
User Stories
Feature testing
Bugs

---
## Vadlidators

  * HTML
    - No errors found using (W3C Validator)[https://jigsaw.w3.org/css-validator/].
    - All pages have been tested but as they all have the same result I only show one.
   
      
  * CSS
    - No errors found using (W3C Validator)[https://jigsaw.w3.org/css-validator/]
   
      
  * Python
    - No errors found using (CI Python linter)[https://pep8ci.herokuapp.com/]
    - All pages have been tested but as they all have the same result I only show one.
   
      
  * Lighthouse
    - Score below


---
## User stories

### Admin

  * As an admin i can view, create, edit and delete all the material and have full control over the website.

### Navigation

  * As a user I can understand what the sites purpose is.
    - On the first page there is a "Welcome to Review the comic" that explains the purpose of the site.
      
<img width="316" height="145" alt="hero" src="https://github.com/user-attachments/assets/0fdee5d6-a2b2-4d67-a2e4-720fd0b4ae43" />
 
  * As a user I find the site easily navigated and understandable.
    - There is a navbar that always stays at the top of the page on every page.

<img width="319" height="189" alt="navbar" src="https://github.com/user-attachments/assets/73891b38-ed91-4394-95ae-0d4e41861332" />

  * As a site user, I can view a paginated list of posts so that I can select which post I want to view.
  * As a user I can click on a review and see the full text of the review post.  
    - The page shows six reviews per page, over that and the paginationbuttons appear.

<img width="400" height="227" alt="cards" src="https://github.com/user-attachments/assets/bda68b22-3eac-42f7-b448-94a16bd96f81" />

   - When the card is clicked it brings the user to the review-detail that shows the full text.

<img width="200" height="305" alt="review detail" src="https://github.com/user-attachments/assets/28a69e2b-2ec8-435b-94a4-383c768a7799" />

      
  * As a logged in user I can save a draft post to finish later.  

### Reviews 

  * As a user I can create my own reviews so others can view them.  
  * As a user I can fully edit my own posts, change the texts and images.  
  * As a user I can delete a review if I need it.
    - A logged in user can create their own reviews.

<img width="300" height="296" alt="create-review" src="https://github.com/user-attachments/assets/4f7c0908-6df4-4a40-a2f7-3773e52f05ca" />

   - The user that made the review can edit and delete their own posts.

<img width="285" height="71" alt="edit-delete" src="https://github.com/user-attachments/assets/ed8a17f0-c18a-4c43-bdf4-cea77aed9d28" />

   - When the user create, edit or delete their post they get a success message.

<img width="360" height="125" alt="success-create" src="https://github.com/user-attachments/assets/633d5359-19be-4f6c-b086-0edbf183a5ae" />


### Interactions

  * As a user I can like and unlike other reviews.   
  * As a user I can leave a comment for the other users.  
  * As a user I can see other users comments and likes.
    - Under the review there is a like button so logged in users can like and unlike.
    - Under the review there is a comment section so logged in users can make a comment.

<img width="250" height="284" alt="comment-like" src="https://github.com/user-attachments/assets/5496dbb9-9d73-4414-9f8c-d57e0c923a2b" />

   - Other users can see all the likes and comments.

<img width="250" height="134" alt="comment-view" src="https://github.com/user-attachments/assets/f29ee9e1-a116-4580-9ab3-9d7672477dc9" />

   - After they comment they get a success message.

<img width="361" height="108" alt="comment-success" src="https://github.com/user-attachments/assets/e78d05e7-e380-4e90-adde-b6cadef038f7" />


### Account

  * As a user I can easily register an account.
  * As a user I can easily sign in and log out.
  * As a user I can easily delete my account.
    - The navbar contains "Create acoount", "Sign up", "Sign in" and "Log out" so its easy to find.

<img width="319" height="189" alt="navbar" src="https://github.com/user-attachments/assets/13ca204e-6d40-4b8b-a16a-c9b181bcaf86" />



Feature testing

Bugs
