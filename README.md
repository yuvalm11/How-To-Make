<br>

### Take a look at the website here: [Yuval makes (almost) anything](https://fab.cba.mit.edu/classes/863.22/EECS/people/Yuval/index.html)
<br>

# Overview

[How To Make (almost) Anything](https://fab.cba.mit.edu/classes/863.22/) is a unique class aiming to teach students from different backgrounds how to use digital fabrication tools to enhance their work. The class is taught by [Neil Gershenfeld](https://en.wikipedia.org/wiki/Neil_Gershenfeld) at the [MIT Center for Bits and Atoms](https://cba.mit.edu/) and cover a wide range of topics from computer controlled machining to electronics production and embedded programming.

As part of the class, I built a personal web app to document my progress and showcase my work. 

<br>

# This Repository

I used Flask framework to build a dynamic website that can be easily updated and maintained.

The website is a sort of a blog that was updated weekly with my progress in the class. Each week I added a new post with a detailed description of the work I did, and a gallery of images and videos. <br>
The website also contains a description of [my final project](https://fab.cba.mit.edu/classes/863.22/EECS/people/Yuval/final.html), that I especially proud of.


### Some challenges

Flask requires a WSGI server for deployment, but in my case (as a class requirement) the website was hosted on MIT's servers that could serve only static HTML files. <br>
I built a simple script that uses the built-in development server and compiles the flask app into static HTML files so it can be hosted on any server.

This repo contains a copy the source code of the website, as well as the static HTML files.

Enjoy!
