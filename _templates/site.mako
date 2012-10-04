<%inherit file="base.mako" />

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html dir='ltr' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
	<head>
		<meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
		<link href="/favicon.ico" rel="icon" type="image/x-icon" />
		<link rel="alternate" type="application/atom+xml" title="${bf.config.blog.name} - Atom" href="${bf.config.blog.path}/feed/atom/index.xml" />
		<link rel="alternate" type="application/rss+xml" title="${bf.config.blog.name} - RSS" href="${bf.config.blog.path}/feed/index.xml" />

		<title>${bf.config.blog.name}</title>
		<link type="text/css" rel="stylesheet" href="/css/site.css"/>
		<link href='http://fonts.googleapis.com/css?family=Squada+One|Marmelad' rel='stylesheet' type='text/css'>
		<%block name="head"/>
		
		<!-- Google analytics -->
		<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-33722666-1']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
		</script>
	</head>
	<body>

<div id='wrapper'>
	<div id='header'>
		<img src="/logo.jpg"/>
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

<script type="text/javascript">
	/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
	var disqus_shortname = '${bf.config.blog.disqus.name}';

	/* * * DON'T EDIT BELOW THIS LINE * * */
	(function () {
		var s = document.createElement('script'); s.async = true;
		s.type = 'text/javascript';
		s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
		(document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
	}());
</script>

	</body>
</html>
