# -*- coding: utf-8 -*-

site.url = "http://horsefire.com"
site.author = "Steve Armstrong"

#### Blog Settings ####
blog = plugins.blog
blog.enabled = True
blog.path = "/blog"
blog.name = "horsefire"
blog.template_path = "_templates/blog"
blog.description = "Put it out. PUT IT OUT!"
blog.timezone  = "US/Pacific"
blog.posts_per_page = 10

blog.disqus.enabled = True
blog.disqus.name = "horsefire"
blog.disqus.debug = False
