<%page args="post"/>
<div class='post'>
	<a name="${post.slug}"></a>
	<h1 class='post-title'><a href="${post.permapath()}">${post.title}</a></h1>
	<div class="post-prose">${self.post_prose(post)}</div>
</div>
<div class='post-footer'>
	<div class='post-timestamp'>
		Posted by stevearm at
		<abbr class='published' title='${post.date.strftime("%Y-%m-%dT%H:%M:%S-%Z")}'>
			${post.date.strftime("%I:%M %p")}
		</abbr>
	</div>

<%
	category_links = []
	for category in post.categories:
		if post.draft:
			#For drafts, we don't write to the category dirs, so just write the categories as text
			category_links.append(category.name)
		else:
			category_links.append("<a href='%s' rel='tag'>%s</a>" % (category.path, category.name))
%>
	<div class='post-labels'>
		Labels: ${", ".join(category_links)}
	</div>
</div>

<%def name="post_prose(post)">
	${post.content}
</%def>
