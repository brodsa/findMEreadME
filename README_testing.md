# Testing & Validation Report

*Content*
  - [Responsivness Testing](#responsivness-testing)
  - [Browser Compatibility Testing](#browser-compatibility-testing)
  - [User Stories Testing](#user-stories-testing)
  - [Features Testing (Manual Testing)](#feature-testing)
  - [Code Validation](#code-validation)
  - [Automated Testing](#automated-testing)
  - [Bug resolved and unresolved](#bug-resolved-and-unresolved)


## Responsivness Testing

## Browser Compatibility Testing

## User Stories Testing

## Feature Testing

## Code Validation
The webpage was validated from several perspectives:
- the markup validity, see [HTML](#html).
- the css properties, see [CSS](#css).
- the web accessibility, see [Accessibility](#accessibility).
- the coding rules of the JavaScript source code, see [JavaScript](#javascript).
- the coding rules of Python source code, see [Python](#pep8).
- the more general quality of the webpage, see [Lighthouse](#lighthouse)

### HTML 
The [Nu Html Checker](https://validator.w3.org/nu/) web-based tool by W3 was used to validate the pages of the webpage. The Checker did not reveal any errors. The source code of pages requiring login was checked directly via text input. Other pages were tested via provided page URL. The detailed reports for each page are below:
- [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2F)
- [How It Works](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2Fhow)
- Account Pages
    - [Log In](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2Faccounts%2Flogin)
    - [Sing up](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2Faccounts%2Fsignup%2F)
    - [Logout](./docs/testing/html/html_logout.png)
- Book Pages
    - [Register Book](./docs/testing/html/html_register_book.png)
    - [Book Key](./docs/testing/html/html_book_key.png)
    - [Latest Books](./docs/testing/html/html_books.png)
    - [Book Detail](./docs/testing/html/html_book_detail.png)
    - [Book Deletion](./docs/testing/html/html_book_delete.png)
    - [Book Editing](./docs/testing/html/html_book_edit.png)
    - [Add Contribution](./docs/testing/html/html_book_add_contribution.png)



### CSS
The [jigsaw](https://jigsaw.w3.org/css-validator/) web-based tool by W3 was used to validate the CSS of the webpage. The course `base.css` file was directly uploaded on [the webpage](https://jigsaw.w3.org/css-validator/#validate_by_upload). The detailed report did not reveal any errors and can be found [here](./docs/testing/css_validation.png).


### PEP8
To validate the Python code in terms of PEP8, the [CI Python Linter](https://pep8ci.herokuapp.com/#) was used.

| Module | Python file               | Report | Results   |
|--------|---------------------------|--------|-----------|
|`findmereadme` | `urls.py`          | | |
|`findmereadme` | `settings.py`      | | |
|`books`        | `admin.py`         | | |
|`books`        | `models.py`        | | |
|`books`        | `tests_models.py`  | | |
|`books`        | `tests_forms.py`   | | |
|`books`        | `tests_views .py`  | | |
|`books`        | `views.py`         | | |
|`books`        | `urls.py`          | | |
|`home`         | `views.py`         | | |
|`home`         | `urls.py`          | | |
|`home`         | `tests.py`         | | |




### Accessibility
The [WAVE](https://wave.webaim.org/) web-based tool was considered for the evaluation of the web accessibility. The detailed reports are below:


### Lighthouse
The Lighthouse in Chrome DevTools evaluates the webpage for performance, accessibility, best practices, and SEO. The detailed reports can be viewed at:

- Desktop evaluation


- Mobile evaluation 


## Automated Testing
### Python
| Module            | Report | Total Coverage   |
|-------------------|--------|------------------|
| `home`            | <img src="./docs/testing/automated/python_home.png" alt="python_home" width="200"/>   | 100% |
|`books`     | <img src="./docs/testing/automated/python_books.png" alt="python_books" width="200"/> | 92% |


Question: Testing 
- form_valid()  of CreateView
- book key: redirected pages

Todo: Testing
- Contribution: Model
- Contribution: Form
- Contribution: view


# Bugs & Issus

Using two databases for dev and prod led to missing up debugging mode and creating a super user. Two superusers were created, one for prod and one for dev. In addition a debug config variable was created, this can be switch on/off in both production and dev environment.

The slug field was prepopulated only for admin panel. The slug field consists of user and title. In the method `form_valid()` of `RegisterBook` class add the slug creation. `form.instance.slug = slugify(f"{self.request.POST.get('title')} {self.request.user}")`, hint from [StackOverflow](https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django) 

clean method of BookForm does not work - possible solution look at the model and add min and max value

WHile testing the form, an error occurred related to clean method of the form class, which I was not able to solve. Error message can be viewed here. To test the rest of the code, this method was temporally remove. Therefore, the coverage report must be taken with caution. 

All books in Latest Books Page can be viewed by logged in and not logged in user. 






