---
permalink: /
title: ""
excerpt: "Research"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a researcher at [Vivix AI](https://vivix.ai/), focusing on training and accelerating multimodal video generation models. I was responsible for research and development in supervised fine-tuning and few-step generation for [Vivix-A1](https://vivix.ai/tech-report-vivix-a1) and [Vivix-W1](https://vivix.ai/tech-report-vivix-w1). I also have experience in 3D computer vision, neural rendering, and multimodal large models.

I obtained my Ph.D. in Computer Science from [Shandong University](https://en.sdu.edu.cn), jointly supervised by Prof. [Baoquan Chen](https://cfcs.pku.edu.cn/baoquan/) at [Peking University](https://www.pku.edu.cn). I received my B.S. from [Taishan College](https://www.tsxt.sdu.edu.cn), Shandong University.

We are recruiting research interns specializing in multimodal generative models. Please feel free to [email me](mailto:gaoqingzhe97@gmail.com) for further details.


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
