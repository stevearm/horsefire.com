This is a pelican-powered blog hosted on [horsefire.com](http://horsefire.com).

### Local development

Build the site with `pelican` then:

    cd output
    python -m SimpleHTTPServer

### Deploying

Pushing to github triggers a `git pull` on my host, then a `pelican -s publishconf.py`
