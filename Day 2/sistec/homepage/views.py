from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    page = """
    <body style="text-align:center; font-family:math; margin: 10px 50px;">
    <style>.course{
    color:green; text-align:left; margin-left:0px;}
    </style>
<h1 style="color:blue;">Sagar Group of Institutions</h1>
<p>Sagar Group of Institutions which was established in the year 2007 under the aegis of Shri Agrawal Educational & Welfare Society with the main objective of imparting quality education.</p>

<p>Sagar Group of Institutions have emerged as a group of Best Private Colleges in Bhopal with its state-of-the-art facility and its expertise in Engineering, Pharmacy, and MBA education. Three institutional campuses rich in infrastructure and amenities proudly flourish under the aegis of the brand Sagar Group of Institutions.</p>

<p>The brand has a strong motivation towards innovation in curriculum implementation with its unique industry-oriented pedagogy. It further aspires to be a part of an educational revolution in technical education, impacting advanced futuristic technologies in the national and international framework, and aims to be one of the finest providers of technical education in India.</p>

<h2 style="color:red;">Spotlight</h2>

<h3 style="color:blue; text-align:left;">Engineering</h4>
<p>The B.Tech. Engineering Program at Sagar Group of Institutions is developed from an industrial point of view, with a great focus on modern technologies employed in the industries. Engineers are the focal point in our economy to design, test, and develop the next generation of products and services for the betterment of society. In this regard, the pedagogy is designed based on industry-oriented training modules a level extra than the standard university curriculum. Similarly, the MTech Engineering Program is developed from a research point of view to inculcate the spirit of innovation and development in Science & Technology.
</p>
<h3 style="text-align:left;">B.Tech.</h3>
<ul>
<li><h4 class="course">Civil Engineering</h4></li>
<li><h4 class="course">Computer Science & Engineering</h4></li>
<li><h4 class="course">Computer Science & Information Technology</h4>
<li><h4 class="course">CSE with Artificial Intelligence and Data Science</h4></li>
<li><h4 class="course">CSE with Artificial Intelligence and Machine Learning</h4></li>
<li><h4 class="course">CSE with Internet of Things</h4></li>
<li><h4 class="course">CSE with Cyber Security</h4></li>
<li><h4 class="course">Electrical & Electronics Engineering</li></h4>
<li><h4 class="course">Electrical Engineering</h4></li>
<li><h4 class="course">Electronics & Communication Engineering</h4></li>
<li><h4 class="course">Mechanical Engineering</h4></li>
</ul>
</body>
"""

    return HttpResponse(page)