---
permalink: /
title: ""
excerpt: "Research"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I obtained my Ph.D. in Computer Science from [Shandong University](https://en.sdu.edu.cn), jointly supervised by Prof. [Baoquan Chen](https://cfcs.pku.edu.cn/baoquan/) at [Peking University](https://www.pku.edu.cn). I received my B.S. from [Taishan College](https://www.tsxt.sdu.edu.cn) (an elite program for fundamental sciences), Shandong University.

My research interests lie in 3D computer vision, neural rendering, generative AI, and multimodal large models.


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
