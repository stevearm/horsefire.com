var render = function(markdownElement, postElement, titleElement, dateElement) {
	// First, clean up some things
	var nodes = document.getElementsByTagName('link');
	for (var i = 0; i < nodes.length; i++) {
		if (nodes[i].rel == "stylesheet") {
			var url = nodes[i].getAttribute("href");
			if (url.charAt(0) == "/") {
				var newUrl = ".." + url;
				nodes[i].setAttribute("href", newUrl);
				console.log("Fixing CSS link from " + url + " to " + newUrl);
			}
		}
	}
	var nodes = document.getElementsByTagName('img');
	for (var i = 0; i < nodes.length; i++) {
		var url = nodes[i].getAttribute("src");
		if (url.charAt(0) == "/") {
			var newUrl = ".." + url;
			nodes[i].setAttribute("src", newUrl);
			console.log("Fixing img src from " + url + " to " + newUrl);
		}
	}
	postElement.innerHTML = "post goes here";

	var markdown = markdownElement.innerText.split(/\n/);

	var stage=0;
	var metadata = {};
	var postlines = [];
	for (var i = 0; i < markdown.length; i++) {
		if(markdown[i] == "---"){
			if (stage == 0 || stage == 1) {
				stage++;
			}else{
				postlines.push(markdown[i]);
			}
		} else {
			if (stage == 0) {
				// Do nothing
			} else if (stage == 1) {
				var data = markdown[i].split(':');
				if (data.length != 2) {
					if (data[0] == "date") {
						data.splice(0, 1);
						data = ["date", data.join(':')];
					} else {
						alert("Metadata line must contain just one colon: " + markdown[i]);
						return;
					}
				}
				metadata[data[0]] = data[1].trim();
			} else {
				postlines.push(markdown[i]);
			}
		}
	}
	post = postlines.join('\n');
	postElement.innerHTML = new Showdown.converter().makeHtml(post);
	if (titleElement) {
		titleElement.innerHTML = metadata.title || "No title specified";
	}
	if (dateElement) {
		dateElement.innerHTML = metadata.date || "No date specified";
	}
};
