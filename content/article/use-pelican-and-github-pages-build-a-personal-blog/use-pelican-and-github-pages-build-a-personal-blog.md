Title: Use Pelican and Github Pages Build a Personal Blog
Date: 2018-03-30 22:42
Category: Python
Tags: python, web, markdown
Status: draft

## Installation
[Pelican](https://blog.getpelican.com) is a static site generator, written by Python. Because Pelican is a python package at pypi ([link](https://pypi.python.org/pypi/pelican/)), we can easily use `pip` to install it.
```shell
pip3 install pelican
```

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
Pelican will ask some questions about the site you want to create and generate needed structure of the site. The questions may like this:
```
Welcome to pelican-quickstart v3.7.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Test site
> Who will be the author of this web site? username
> What will be the default language of this web site? [English]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
> What is your URL prefix? (see above example; no trailing slash) https://username.github.io
> Do you want to enable article pagination? (Y/n) n
> What is your time zone? [Europe/Paris]
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /Users/thorough/Thorough/developments/Projects/blog-src/test
```
And the files structure may like this:
```
.
|-- Makefile
|-- content/
|-- develop_server.sh
|-- fabfile.py
|-- output/
|-- pelicanconf.py
`-- publishconf.py
```
where `content` contains markdown files which you want to post and `output` is the root folder for your site. The `develop_server.sh` script can start/stop a temporary web server for development. The main configuration file is `pelicanconf.py`.

## Write blog article
You can write down your blog using `markdown` or `rst`. If you use `rst`, you need not do any thing. But if you use `markdown` like me, you need install related python package first.
```
pip3 install markdown
```
Then you can write down your first blog. Create a `markdown` file called `my-frist-post.md` in `content` folder.
```
touch content/my-first-post.md
```
We need write the first few lines under a special format, because Pelican will read these lines to set metadata of the article. The file head may seems like
```
Title: My First Post
Date: 2018-04-06 23:09
Category: Web
Tags: python, web, markdown
```
Following these lines, you can write the content of your blog article. When you finish your blog article, you can generate the `html` files of your website using
```
make html
```
And you can also use the `develop_server.sh` script to start/stop a temporary http server. 

## Use themes
