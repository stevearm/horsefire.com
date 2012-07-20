import urlparse
from blogofile.cache import bf
import re
from PIL import Image

blog = bf.config.controllers.blog


def run():
    write_permapages()


def write_permapages():
    "Write blog posts to their permalink locations"
    site_re = re.compile(bf.config.site.url, re.IGNORECASE)
    num_posts = len(blog.posts)
    
    for i, post in enumerate(blog.posts):
        if post.permalink:
            path = site_re.sub("", post.permalink)
            blog.logger.info(u"Writing permapage for post: {0}".format(path))
        else:
            #Permalinks MUST be specified. No permalink, no page.
            blog.logger.info(u"Post has no permalink: {0}".format(post.title))
            continue

        images = fix_image_links(post, path)

        env = {
            "post": post,
            "posts": blog.posts
        }

        #Find the next and previous posts chronologically
        if i < num_posts - 1:
            env['prev_post'] = blog.posts[i + 1]
        if i > 0:
            env['next_post'] = blog.posts[i - 1]
        
        bf.writer.materialize_template(
                "permapage.mako", bf.util.path_join(path, "index.html"), env)
        
        copy_images(images)

def fix_image_links(post, path):
	image_re = re.compile('<img src="([^"/]+)" class="post-image-(small|medium|large)">')
	found = image_re.search(post.content)
	images = []
	while found:
		image = {}
		image['size'] = found.group(2)
		image['source'] = found.group(1)
		(file_part, tmp, extension) = image['source'].partition(".")
		if not extension:
			blog.logger.warning('Cannot parse file from %s' % found.group(0))
			continue
		dest_filename = '%s-%s.%s' % (file_part, image['size'], extension)
		image['dest'] = '%s/%s' % (path, dest_filename)
		images.append(image)
		new_img_html = '<img src="%s/%s">' % (post.permapath(), dest_filename)
		post.content = re.sub(found.group(0), new_img_html, post.content)
		found = image_re.search(post.content)
	return images

def copy_images(images):
	for image in images:
		if image['size'] == 'small':
			max_size = 100
		elif image['size'] == 'medium':
			max_size = 300
		elif image['size'] == 'large':
			max_size = 600
		else:
			blog.logger.warning('Unknown size so skipping: %s' % (repr(image)))
			continue
		size = max_size, max_size
		im = Image.open("_posts/" + image['source'])
		im.thumbnail(size, Image.ANTIALIAS)
		im.save("_site/" + image['dest'])
	return
