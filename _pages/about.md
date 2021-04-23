---
permalink: /
title: ""
excerpt: "Research"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a phd candidate at [Shandong Unversity](https://en.sdu.edu.cn), my research interests are in computer vision, computer graphics and machine learning. Now I am working at [VCL\|PKU](http://vcl.pku.edu.cn/index.html). My supervisor is Prof.[Baoquan Chen](https://cfcs.pku.edu.cn/baoquan/).


Publications
------
<style style="text/css">
  	.hoverTable{
		width:85%; 
		border-collapse:collapse; 
		border: 0px;
	}
	.hoverTable td{ 
		padding:7px; border:#4e95f4 0px solid;
	}
	/* Define the default color for all the table rows */
	.hoverTable tr{
		background: #ffffff;
	}
	/* Define the hover highlight color for the table row */
    .hoverTable tr:hover {
          background-color: #f7f7f7;
    }
</style>

<table class="hoverTable">
  <col style="width:75%">
  <col style="width:25%">
  {% for post in site.publications reversed %}
    {% include archive-single-pub.html %}
  {% endfor %}
</table>
