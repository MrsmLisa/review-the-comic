# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| reviews | [confirm_delete.html](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/templates/reviews/confirm_delete.html) | [confirm-delete test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fdelete_review%2Fheadlopper%2F) | ![screenshot](documentation/validation/reviews/confirm_delete.png) |  |
| reviews | [index.html](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/templates/reviews/index.html) | [Index-test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2F#textarea) | ![screenshot](documentation/validation/reviews/index.png) |  |
| reviews | [review_detail.html](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/templates/reviews/review_detail.html) | [review_detail test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Freview%2Fheadlopper%2F) | ![screenshot](documentation/validation/reviews/review_detail.png) |  |
| reviews | [review_form.html](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/templates/reviews/review_form.html) | [review_form test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Freview_create%2F) | ![screenshot](documentation/validation//reviews/review_form.png) |  |
| reviews | [confirm_delete_comment.html](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/templates/reviews/confirm_delete_coment.html) | [confirm_delete_comment test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Freview%2Fheadlopper%2Fdelete_comment%2F10%2F) | ![screenshot](documentation/validation//reviews/delete-comment.png) |  |
| reviews | [edit_comment.html](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/templates/reviews/edit_comment.html) | [edit_comment test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Freview%2Fheadlopper%2Fedit_comment%2F10%2F) | ![screenshot](documentation/validation//reviews/edit-comment.png) |  |
| templates | [base.html] |  |  | As the base.html is on every page it is note tested on its own. |
| templates | [login.html](https://github.com/MrsmLisa/review-the-comic/blob/main/templates/account/login.html) | [login test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/templates/login.png) |  |
| templates | [logout.html](https://github.com/MrsmLisa/review-the-comic/blob/main/templates/account/logout.html) |  [logout test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2F) | ![screenshot](documentation/validation/templates/logout.png) |  |
| templates | [signup.html](https://github.com/MrsmLisa/review-the-comic/blob/main/templates/account/signup.html) | [signup-test](https://validator.w3.org/nu/?doc=https%3A%2F%2Freview-the-comic-ac6c1ec7e7bf.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/templates/signup.png) |  |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/MrsmLisa/review-the-comic/blob/main/static/css/style.css) |  | ![screenshot](documentation/validation/css/css.png) |  |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [manage.py](https://github.com/MrsmLisa/review-the-comic/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/manage.py) | ![screenshot](documentation/validation/python/manage-py.png) |  |
| review_the_comic | [settings.py](https://github.com/MrsmLisa/review-the-comic/blob/main/review_the_comic/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/review_the_comic/settings.py) | ![screenshot](documentation/validation/python/settings-py.png) |  |
| review_the_comic | [urls.py](https://github.com/MrsmLisa/review-the-comic/blob/main/review_the_comic/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/review_the_comic/urls.py) | ![screenshot](documentation/validation/python/url-review-the-comic.png) |  |
| reviews | [admin.py](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/reviews/admin.py) | ![screenshot](documentation/validation/python/admin-py.png) |  |
| reviews | [forms.py](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/reviews/forms.py) | ![screenshot](documentation/validation/python/forms-py.png) |  |
| reviews | [models.py](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/reviews/models.py) | ![screenshot](documentation/validation/python/models-py.png) |  |
| reviews | [tests.py](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/reviews/tests.py) | ![screenshot](documentation/validation/python/test-py.png) |  |
| reviews | [urls.py](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/reviews/urls.py) | ![screenshot](documentation/validation/python/url-py-review.png) |  |
| reviews | [views.py](https://github.com/MrsmLisa/review-the-comic/blob/main/reviews/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MrsmLisa/review-the-comic/main/reviews/views.py) | ![screenshot](documentation/validation/python/views-py.png) |  |

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Add Blog | ![screenshot](documentation/responsiveness/mobile-add-blog.png) | ![screenshot](documentation/responsiveness/tablet-add-blog.png) | ![screenshot](documentation/responsiveness/desktop-add-blog.png) | Works as expected |
| Edit Blog | ![screenshot](documentation/responsiveness/mobile-edit-blog.png) | ![screenshot](documentation/responsiveness/tablet-edit-blog.png) | ![screenshot](documentation/responsiveness/desktop-edit-blog.png) | Works as expected |
| Blog Post | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Add Blog | ![screenshot](documentation/browsers/chrome-add-blog.png) | ![screenshot](documentation/browsers/firefox-add-blog.png) | ![screenshot](documentation/browsers/safari-add-blog.png) | Works as expected |
| Edit Blog | ![screenshot](documentation/browsers/chrome-edit-blog.png) | ![screenshot](documentation/browsers/firefox-edit-blog.png) | ![screenshot](documentation/browsers/safari-edit-post.png) | Works as expected |
| Blog Post | ![screenshot](documentation/browsers/chrome-blog-post.png) | ![screenshot](documentation/browsers/firefox-blog-post.png) | ![screenshot](documentation/browsers/safari-blog-post.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Add Blog | ![screenshot](documentation/lighthouse/mobile-add-blog.png) | ![screenshot](documentation/lighthouse/desktop-add-blog.png) |
| Edit Blog | ![screenshot](documentation/lighthouse/mobile-edit-blog.png) | ![screenshot](documentation/lighthouse/desktop-edit-blog.png) |
| Blog Post | ![screenshot](documentation/lighthouse/mobile-blog-post.png) | ![screenshot](documentation/lighthouse/desktop-blog-post.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Blog Management | Feature is expected to allow the blog owner to create new posts with a title, featured image, and content. | Created a new post with valid title, image, and content data. | Post was created successfully and displayed correctly in the blog. | ![screenshot](documentation/defensive/create-post.png) |
| | Feature is expected to allow the blog owner to update existing posts. | Edited the content of an existing blog post. | Post was updated successfully with the new content. | ![screenshot](documentation/defensive/update-post.png) |
| | Feature is expected to allow the blog owner to delete blog posts. | Attempted to delete a blog post, confirming the action before proceeding. | Blog post was deleted successfully. | ![screenshot](documentation/defensive/delete-post.png) ![image2](documentation/defensive/delete-post2.png) |
| | Feature is expected to retrieve a list of all published posts. | Accessed the blog owner dashboard to view all published posts. | All published posts were displayed in a list view. | ![screenshot](documentation/defensive/published-posts.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png) ![image2](documentation/defensive/login2.png)|
| | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | ![screenshot](documentation/defensive/register.png) ![image2](documentation/defensive/register2.png) |
| | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | ![screenshot](documentation/defensive/logout.png) ![screenshot](documentation/defensive/logout2.png) |
| User Comments | Feature is expected to allow registered users to leave comments on blog posts. | Logged in and added comments to a blog post. | Comments were successfully added. | ![screenshot](documentation/defensive/add-comment.png) |
| | Feature is expected to allow users to edit their own comments. | Edited personal comments. | Comments were updated as expected. | ![screenshot](documentation/defensive/edit-delete-comments.png) |
| | Feature is expected to allow users to delete their own comments. | Deleted personal comments. | Comments were removed as expected. | ![screenshot](documentation/defensive/delete-user-comments.png) |
| Guest Features | Feature is expected to allow guest users to read blog posts without registering. | Opened blog posts as a guest user. | Blog posts were fully accessible without logging in. | ![screenshot](documentation/defensive/view-post-guest.png) |
| | Feature is expected to display the names of other commenters on posts. | Checked the names of commenters on posts as a guest user. | Commenter names were displayed as expected. | ![screenshot](documentation/defensive/comenter-names.png) |
| | Feature is expected to block standard users from brute-forcing admin pages. | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access. | ![screenshot](documentation/defensive/brute-force.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a blog owner | I would like to create new blog posts with a title, featured image, and content | so that I can share my experiences with my audience. | ![screenshot](documentation/features/add-review.png) |
| As a blog owner | I would like to update existing blog posts | so that I can correct or add new information to my previous stories. | ![screenshot](documentation/features/edit-review.png) |
| As a blog owner | I would like to delete blog posts | so that I can remove outdated or irrelevant content from my blog. | ![screenshot](documentation/features/delete-reviews.png) |
| As a blog owner | I would like to retrieve a list of all my published blog posts | so that I can manage them from a central dashboard. | ![screenshot](documentation/features/blog-dash.png) |
| As a blog owner | I would like to approve or reject comments from users | so that I can maintain control over the discussion on my posts. | ![screenshot](documentation/features/delete-comments.png) |
| As a blog owner | I would like to edit or delete user comments | so that I can clean up or remove inappropriate responses after they've been posted. | See above |
| As a registered user | I would like to log in to the site | so that I can leave comments on blog posts. | ![screenshot](documentation/features/login.png) |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with the blog. | ![screenshot](documentation/features/signup.png) |
| As a registered user | I would like to leave a comment on a blog post | so that I can share my thoughts or ask questions about the owner's experiences. | ![screenshot](documentation/features/add-comment.png) |
| As a registered user | I would like my comment to show my name and the timestamp | so that others can see who I am and when I left the comment. | ![screenshot](documentation/features/comment-made.png) |
| As a registered user | I would like to edit or delete my own comments | so that I can fix mistakes or retract my statement. | ![screenshot](documentation/features/edit-delete-comments.png) |
| As a guest user | I would like to read blog posts without registering | so that I can enjoy the content without needing to log in. | ![screenshot](documentation/features/view-post-guest.png) |
| As a guest user | I would like to browse past posts | so that I can explore the blog's full content history. | ![screenshot](documentation/features/content-history.png) |
| As a guest user | I would like to register for an account | so that I can participate in the community by leaving comments on posts. | ![screenshot](documentation/features/register.png) |
| As a guest user | I would like to see the names of other commenters on posts | so that I can get a sense of community interaction before registering. | ![screenshot](documentation/features/comenter-names.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/404.png) |


## Bugs

### Fixed Bugs
Unfortunatly I forgot to take screenshots for most of my 

| Bug | Fix |
|---|---|
| Could not connect to Heroku. | Had to add the "127.0.0.1" and had misspelt Heroku.|
| Recived an Gunicorn error saying 'Haltserver, worker failed to boot" | Forgotten to put DATABASE_URL in Heroku Config Vars. |
| Was not allowecd to migrate. | There was no 0001 in the migrations folder. Had to reinstall Django. |
| `os.environ.setdefault` split across two lines in `manage.py` causing `No Django settings specified` error on Heroku | Moved both arguments onto the same line |
| `instance=review` in `review_create` view causing `UnboundLocalError` | Removed `instance=review` as it only belongs in the edit view |
| Cloudinary `Invalid Signature` error | Found hidden character in API secret using `repr()` in Django shell |
| Navbar content overlapping page on mobile | Added `padding-top` to body to account for fixed navbar height |
| Page shifting horizontally on PC due to scrollbar | Added `scrollbar-gutter: stable` to HTML element |
| `excerpt` and `date` merged as one field name in `forms.py` | Added missing comma between the two field names |
| `{% load static %}` missing from child templates causing `TemplateSyntaxError` | Added `{% load static %}` to each template that uses static files |
| `approved` field referenced in view but not in Comment model | Removed filter from view to match the model |

### Unfixed Bugs

- No unfixed bugs remaining.

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. |  |
| The Lighthouse score is low in some places because the images are not uploaded from https. There is also a problem with Bootstrap CSS that is not used, if it was a real site I would have used the PurgeCSS.  | ![screenshot](documentation/lighthouse/desktop-blog-post.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.