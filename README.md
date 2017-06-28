# Movie Trailer Website
 Simple movie trailer website to exercise some programming foundations with Python


**Note:** This is a solution to project 1 of the [Udacity Full Stack Web Developer Nanodegree][1] based on the course [Programming Foundations with Python (ud036)][2].

Installing Development Pre-Requisites
-------------------------------------

+ Install [Python 3.5+][3]
+ Install [python-dotenv][4]

Installing The Project for Development / Testing on Linux
---------------------------------------------------------

+ Clone the repository:

    ```shell
    $ git clone git@github.com:rishi-ramawat/FSND_P1-Movie_Trailer_Website.git
    $ cd FSND_P1-Movie_Trailer_Website
    ```

+ Initialize the project:

    ```shell
    $ bin/init_project
    ```

    * This shell script will create a `.env` file for you.
    * It will also install/upgrade [python-dotenv][4].

+ Review `.env` and and configure any required variables.
    * You would need access to [OMDb API][5] if you want to test the app's interaction with it.
    * You can get the access by:
        - Becoming a Patron [here](https://www.patreon.com/bePatron?u=5038490).
        - Then, requesting [OMDb API][5] key access [here][6].
    * **Don't worry** if you don't have the [OMDb API Key][6] (The app would still work)
        - Just comment out `OMDB_API_KEY` in the `.env` using `#`.

Installing The Project for Development / Testing on Windows
-----------------------------------------------------------

+ Clone the repo
+ Visit the folder where you have cloned the repo
    * Make a copy `.env.example` and name it as `.env`
    * Make sure all the required variables are present & initialized in `.env`
+ Make sure you have [python-dotenv][4] installed

Running the project
-------------------

Run the following to generate `fresh_tomatoes.html`:

```shell
$ python entertainment_center.py
```

Project Screenshots
-------------------

_Simple home page where movies are laid out_
![Simple home page where movies are laid out](https://user-images.githubusercontent.com/13311878/27624619-28e3f91a-5bff-11e7-8aa3-3f0c0a7bccaa.png "Simple home page where movies are laid out")


_Page allows users to click on a movie image to watch its trailer_
![Page allows users to click on a movie image to watch its trailer](https://user-images.githubusercontent.com/13311878/27624906-4d5f0798-5c00-11e7-959a-3232a2b7363d.png "Page allows users to click on a movie image to watch its trailer")

[1]: https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004 "Udacity Nanodegree: Full Stack Web Developer"
[2]: https://www.udacity.com/course/programming-foundations-with-python--ud036-nd "Udacity Course: Programming Foundations with Python"
[3]: https://www.python.org/downloads/ "Download Python"
[4]: https://pypi.python.org/pypi/python-dotenv "python-dotenv"
[5]: http://www.omdbapi.com/ "OMDb API - The Open Movie Database"
[6]: (http://www.omdbapi.com/apikey.aspx) "OMDb API - The Open Movie Database"
