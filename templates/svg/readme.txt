The reason why SVGs file are saved here is because we need to include the SVG as if it's part of the HTML code and not
just merely reference it in an image tag. To embed SVG as part of html code we need to use %include tag. However %include
tags are not meant for referencing static files like svg files, they are meant to include templates in the html. Therefore
a work around is to store the svg file in the templates folder and %include it like you would do to any html base file, in
the html file where you intend to show the svg image.