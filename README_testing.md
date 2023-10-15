# Testing & Validation Report

*Content*
  - Responsivness Testing
  - Browser Compatibility Testing
  - User Stories Testing
  - Features Testing (Manual Testing)
  - Code Validation
  - Automated Testing
  - Lighthouse testing outcomes
  - Bug resolved and unresolved


## Code Validation
The webpage was validated from several perspectives:
- the markup validity, see [HTML](#html).
- the css properties, see [CSS](#css).
- the web accessibility, see [Accessibility](#accessibility).
- the coding rules of the JavaScript source code, see [JavaScript]
(#javascript).
- the coding rules of Python source code, see [Python](#pep8).

### HTML 
The [Nu Html Checker](https://validator.w3.org/nu/) web-based tool by W3 was used to validate the pages of the webpage. The Checker did not reveal any errors. The detailed reports for each page are below:
- [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2F)
- [How It Works](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2Fhow)
- Account Pages
    - [Log In](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2Faccounts%2Flogin)
    - [Sing up](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Ffindme-readme-10d0bfb3ba28.herokuapp.com%2Faccounts%2Fsignup%2F)



### CSS
The [jigsaw](https://jigsaw.w3.org/css-validator/) web-based tool by W3 was used to validate the CSS of the webpage. The course `base.css` file was directly uploaded on [the webpage](https://jigsaw.w3.org/css-validator/#validate_by_upload). The detailed report did not reveal any errors and can be found [here](./docs/testing/css_validation.png).


### PEP8
To validate the Python code in terms of PEP8, the [CI Python Linter](https://pep8ci.herokuapp.com/#) was used.

| Module | Python file               | Report | Results   |
|--------|---------------------------|--------|-----------|
|`findmereadme` | `urls.py`          | | |
|`books`        | `admin.py`         | | |
|`books`        | `models.py`        | | |
|`books`        | `tests_models.py`  | | |
|`books`        | `views.py`         | | |
|`books`        | `urls.py`          | | |
|`home`         | `views.py`         | | |
|`home`         | `urls.py`          | | |
|`home`         | `tests.py`         | | |




### Accessibility
The [WAVE](https://wave.webaim.org/) web-based tool was considered for the evaluation of the web accessibility. The detailed reports are below:


## Lighthouse
The Lighthouse in Chrome DevTools evaluates the webpage for performance, accessibility, best practices, and SEO. The detailed reports can be viewed at:

- Desktop evaluation


- Mobile evaluation 


## Automated Testing
### Python
| Module            | Report | Total Coverage   |
|-------------------|--------|------------------|
| `home`            | <img src="./docs/testing/automated/python_home.png" alt="python_home" width="200"/>   | 100% |
|`findmereadme`     | <img src="./docs/testing/automated/python_books.png" alt="python_books" width="200"/> | 99% |