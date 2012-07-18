#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Creates a directory with javascript staging versions of all posts, or extracts markdown from that folder back into the _posts folder

Arguments: mode [parameters]
Modes:	stage path/to/html/blog/post
		extract
Optional arguments:
		--post [javascript line to find the post element]
		--title [javascript line to find the title element]
		--date [javascript line to find the date element]
"""

import optparse
import os
import re

dir = "_posts"
markdown_pre_tag = '<div id="markdown" style="display: none"><!-- markdown pre tag -->'
markdown_post_tag = '</div><!-- markdown post tag -->'

def stage(template_file, options):
	if not os.path.isdir(dir):
		print "%s is not a folder" % dir
		return
	
	files = os.listdir(dir)
	markdown_files = {}
	for file in files:
		if file[-9:] == ".markdown":
			markdown_files['%s/%s' % (dir, file)] = '%s/%s.html' % (dir, file)
	
	template_header = []
	template_footer = []
	header = True
	template_marker = re.compile(".*</body>.*")
	i = open(template_file, 'r')
	template_line = i.read()
	while template_line:
		for line in template_line.splitlines():
			if header:
				if template_marker.match(line):
					header = False
					template_footer.append(line)
				else:
					template_header.append(line)
			else:
				template_footer.append(line)
		template_line = i.read()
	i.close()
	
	for markdown_file, staging_file in markdown_files.iteritems():
		print 'Created %s' % staging_file
		o = open(staging_file, 'w')
		for line in template_header:
			o.write('%s\n' % line)
		
		o.write('%s\n' % markdown_pre_tag)
		i = open(markdown_file, 'r')
		for line in i:
			o.write(line)
		i.close()
		o.write('\n%s\n' % markdown_post_tag)
		
		o.write('<script type="text/javascript" src="showdown.js"></script>\n')
		o.write('<script type="text/javascript" src="staging.js"></script>\n')
		o.write('<script type="text/javascript">\n')
		o.write('render(document.getElementById("markdown"), %s, %s, %s);\n' % (options.post, options.title, options.date))
		o.write('</script>\n')
		
		for line in template_footer:
			o.write('%s\n' % line)
		o.close()

def extract(options):
	if not os.path.isdir(dir):
		print "%s is not a folder" % dir
		return
	
	files = {}
	for file in os.listdir(dir):
		if file[-14:] == ".markdown.html":
			files['%s/%s' % (dir, file)] = '%s/%s' % (dir, file[:-5])
	
	for staging_file, markdown_file in files.iteritems():
		print 'Extracted %s' % markdown_file
		i = open(staging_file, 'r')
		line_number = 0
		current_line = i.read().splitlines()
		while True:
			if current_line[line_number] == markdown_pre_tag:
				break
			line_number = line_number + 1
			if line_number == len(current_line):
				current_line = i.read().splitlines()
				if len(current_line) == 0:
					print 'Failed to find the pre tag in %s' % staging_file
					return
				line_number = 0
		
		line_number = line_number + 1
		o = open(markdown_file, 'w')
		while True:
			if current_line[line_number] == markdown_post_tag:
				break
			o.write('%s\n' % current_line[line_number])
			line_number = line_number + 1
			if line_number == len(current_line):
				current_line = i.read().splitlines()
				if len(current_line) == 0:
					print 'Failed to find the pre tag in %s' % staging_file
					return
				line_number = 0
		
		o.close()
		i.close()

def main():
	p = optparse.OptionParser()
	p.add_option('--post', '-p')
	p.add_option('--title', '-t')
	p.add_option('--date', '-d')
	options, arguments = p.parse_args()
	
	if len(arguments) == 0:
		print 'Must specify mode as stage or extract'
		return
	mode = arguments[0]
	if mode == 'stage':
		if len(arguments) == 1:
			print 'Staging must specify a rendered permapage for a blog entry'
			return
		if not options.post:
			print 'Must specify a javascript selector using --post'
			return
		if not options.title:
			options.title = "null"
		if not options.date:
			options.date = "null"

		stage(arguments[1], options)
	elif mode == 'extract':
		extract(options)
	else:
		print 'Unknown mode: %s' % mode

if __name__ == '__main__':
	main()
