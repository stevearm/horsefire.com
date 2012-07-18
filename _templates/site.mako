<%inherit file="base.mako" />

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html dir='ltr' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
	<head>
		<meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
		<link href="data:image/x-icon;base64,AAABAAEAEBAQAAAAAAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAsb+GAP///wA0NYUAqKr/AGtu+QBOULoAT09PAOXtzABTVsIAra2tAM7bpwAAAAAAAAAAAAAAAAAAAAAAAAoiEREioAAAAbs7s7sQAAAzM0OUMzMAA0RTQ5Q1RDAAM1NTlTUzAAAGNVOVU2AAAGVTVVU1VgAAZVNVVTVWAABlu1VVu1YAAGt3tVt3tgAAa3e1W3e2AABou7VYu7YAAAaIVEWIYAAABlVERFVgAAAAZlVVZgAAAAAAZmYAAADgBwAA4AcAAMADAACAAQAAwAMAAOAHAADAAwAAwAMAAMADAADAAwAAwAMAAMADAADgBwAA4AcAAPAPAAD8PwAA" rel="icon" type="image/x-icon" />
		<link rel="alternate" type="application/atom+xml" title="${bf.config.blog.name} - Atom" href="/feed/atom/index.xml" />
		<link rel="alternate" type="application/rss+xml" title="${bf.config.blog.name} - RSS" href="/feed/index.xml" />

		<title>${bf.config.blog.name}</title>
		<link type="text/css" rel="stylesheet" href="/css/site.css"/>
		<%block name="head"/>
	</head>
	<body>

<div id='wrapper'>
	<div id='header'>
		<h1 class='title'>${bf.config.blog.name}</h1>
		<p class='description'>${bf.config.blog.description}</p>
	</div>
	<div id='navigation'>
		<div class='nav-section'>
			<h2 class='nav-title'>Site map</h2>
			<ul>
				<li id='current'><a href='${bf.util.site_path_helper()}'>Home</a></li>
				<li><a href='${bf.util.site_path_helper(bf.config.blog.path)}'>Blog</a></li>
				<li><a href='${bf.util.site_path_helper(bf.config.blog.path, 'feed')}'>Posts RSS</a></li>
				% if bf.config.blog.disqus.enabled:
				<li><a href='/some/disqus/url'>Comments RSS</a></li>
				% endif
			</ul>
		</div>
		<div class='nav-section'>
			<h2 class='nav-title'>Recent Posts</h2>
			<ul>
			% for post in bf.config.blog.posts[:3]:
				<li><span class="item-title"><a href="${post.path}">${post.title}</a></span></li>
			% endfor
			</ul>
		</div>
		<div class='nav-section'>
			<h2 class='nav-title'>Labels</h2>
			<ul>
			% for category, num_posts in bf.config.blog.all_categories:
				<li>
					<a dir='ltr' href='${category.path}'>${category}</a>
					<span dir='ltr'>(${num_posts})</span>
				</li>
			% endfor
			</ul>
		</div>
		<div class='nav-section'>
			<h2 class='nav-title'>Blog Archive</h2>
			<ul>
			% for link, name, num_posts in bf.config.blog.archive_links:
				<li>
					<a dir='ltr' href='${bf.util.site_path_helper(bf.config.blog.path,link)}/1'>
						${name}
					</a>
					<span dir='ltr'>(${num_posts})</span>
				</li>
			% endfor
			</ul>
		</div>
	</div>
	<div id='content'>
${next.body()}
	</div>
	<div class='clear' id='footer'></div>
</div>

	</body>
</html>
