Title: Use Pelican and Github Pages Build a Personal Blog
Data: 2018-03-30 22:42
Category: Python, Web
Tags: python, web, markdown

## Installation
[Pelican](https://blog.getpelican.com) is a static site generator, written in Python. Because Pelican is a python package at pypi ([link](https://pypi.python.org/pypi/pelican/)), we can easily use `pip` to install it.
```shell
pip3 install pelican markdown
```
Here we installed `markdown` at the same time. If you use `rst`, you can ignore the markdown.

## Create github pages
[GitHub Pages](https://pages.github.com) lets you create static site for you or your project. GitHub will hosts the site and you can avoid constructing your own server. It is suitable for someone does not have enough time to maintain the web server and lets you focus on the content. It is easy to create a GitHub pages by creating a new repository named as `user-name.github.io`. Here `user-name` is the user name for your GitHub's account. My GitHub user name is `sun-rongyang`, so my GitHub pages url is `sun-rongyang.github.io`.

## Initialize the blog site
First, create the root path of the project:
```
mkdir blog-src
```
Then go into the path and run `pelican-quickstart` to create a site quickly.
```
cd blog-src && pelican-quickstart
```
Pelican will ask some question about the site you want to create and generate needed structure of the site.
