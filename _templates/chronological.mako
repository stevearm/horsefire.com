<%inherit file="site.mako" />
% for post in posts:
  <%include file="post.mako" args="post=post" />
% if bf.config.blog.disqus.enabled:
  <div class="post-footer"><a href="${post.permalink}#disqus_thread">Comments</a></div>
% endif
  <hr class="interblog" />
% endfor
% if prev_link:
 <a href="${prev_link}">« Previous Page</a>
% endif
% if prev_link and next_link:
  --  
% endif
% if next_link:
 <a href="${next_link}">Next Page »</a>
% endif
