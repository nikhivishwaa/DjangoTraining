from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    something = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz & News Hub</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,600,700&display=swap" rel="stylesheet">
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Global Styles */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f2f5;
            color: #333;
            overflow-x: hidden;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        /* Navbar Styles */
        .navbar {
            width: 100%;
            background-color: #4a90e2;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .navbar .logo {
            font-size: 24px;
            font-weight: 700;
            color: #fff;
            letter-spacing: 2px;
        }

        .navbar ul {
            list-style: none;
            display: flex;
            gap: 30px;
        }

        .navbar ul li {
            position: relative;
        }

        .navbar ul li a {
            font-size: 16px;
            color: #fff;
            padding: 5px 0;
            transition: color 0.3s;
        }

        .navbar ul li a:hover {
            color: #d1e8ff;
        }

        /* Hero Section Styles */
        .hero {
            width: 100%;
            height: 100vh;
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1557682224-5b8590cd9ec5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80') center/cover no-repeat;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: #fff;
            padding-top: 80px;
        }

        .hero h1 {
            font-size: 60px;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease-in-out;
        }

        .hero p {
            font-size: 24px;
            margin-bottom: 40px;
            animation: fadeInUp 1s ease-in-out;
        }

        .hero .btn {
            padding: 15px 30px;
            background-color: #ff5a5f;
            border: none;
            border-radius: 30px;
            font-size: 18px;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            animation: fadeInUp 1s ease-in-out;
        }

        .hero .btn:hover {
            background-color: #e14e4e;
            transform: translateY(-5px);
        }

        /* Features Section */
        .features {
            padding: 100px 50px;
            background-color: #fff;
            display: flex;
            justify-content: space-around;
            align-items: center;
            gap: 50px;
            flex-wrap: wrap;
        }

        .feature-card {
            background-color: #f9f9f9;
            width: 300px;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-10px);
        }

        .feature-card i {
            font-size: 50px;
            color: #4a90e2;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }

        .feature-card h3 {
            font-size: 22px;
            margin-bottom: 15px;
        }

        .feature-card p {
            font-size: 16px;
            color: #555;
        }

        /* News Section */
        .news {
            padding: 100px 50px;
            background-color: #f0f2f5;
        }

        .news h2 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 60px;
            position: relative;
        }

        .news h2::after {
            content: '';
            width: 80px;
            height: 4px;
            background-color: #4a90e2;
            position: absolute;
            left: 50%;
            bottom: -10px;
            transform: translateX(-50%);
        }

        .news-container {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }

        .news-card {
            background-color: #fff;
            width: 350px;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .news-card:hover {
            transform: translateY(-10px);
        }

        .news-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            transition: transform 0.5s;
        }

        .news-card:hover img {
            transform: scale(1.1);
        }

        .news-card-content {
            padding: 20px;
        }

        .news-card-content h3 {
            font-size: 20px;
            margin-bottom: 10px;
            color: #333;
        }

        .news-card-content p {
            font-size: 16px;
            color: #666;
            margin-bottom: 15px;
        }

        .news-card-content a {
            font-size: 16px;
            color: #4a90e2;
            font-weight: 600;
            transition: color 0.3s;
        }

        .news-card-content a:hover {
            color: #2d6ebd;
        }

        /* Footer Styles */
        .footer {
            background-color: #333;
            color: #fff;
            padding: 50px;
            text-align: center;
        }

        .footer p {
            margin-bottom: 10px;
            font-size: 16px;
        }

        .footer .social-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }

        .footer .social-icons a {
            color: #fff;
            font-size: 20px;
            transition: color 0.3s;
        }

        .footer .social-icons a:hover {
            color: #4a90e2;
        }

        /* Keyframes for Animations */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-15px);
            }
            60% {
                transform: translateY(-7px);
            }
        }

        /* Responsive Styles */
        @media (max-width: 768px) {
            .navbar {
                padding: 15px 30px;
            }

            .hero h1 {
                font-size: 40px;
            }

            .hero p {
                font-size: 18px;
            }

            .features {
                flex-direction: column;
                align-items: center;
            }

            .news-container {
                flex-direction: column;
                align-items: center;
            }

            .news-card {
                width: 100%;
                max-width: 500px;
            }
        }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar">
        <div class="logo">QuizNews</div>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/exam/">Quizzes</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
            <li><a href="/help/">Help</a></li>
        </ul>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div>
            <h1>Welcome to QuizNews</h1>
            <p>Your ultimate destination for fun quizzes and latest news updates.</p>
            <button class="btn">Get Started</button>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features">
        <div class="feature-card">
            <i class="fas fa-question-circle"></i>
            <h3>Challenging Quizzes</h3>
            <p>Test your knowledge with our wide range of interactive quizzes across various topics.</p>
        </div>
        <div class="feature-card">
            <i class="fas fa-newspaper"></i>
            <h3>Latest News</h3>
            <p>Stay updated with the most recent and trending news from around the world.</p>
        </div>
        <div class="feature-card">
            <i class="fas fa-users"></i>
            <h3>Community Engagement</h3>
            <p>Join our community to share insights, discuss topics, and connect with like-minded individuals.</p>
        </div>
    </section>

    <!-- News Section -->
    <section class="news">
        <h2>Latest News</h2>
        <div class="news-container">
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60" alt="News Image">
                <div class="news-card-content">
                    <h3>Tech Innovations in 2024</h3>
                    <p>Explore the groundbreaking technological advancements expected to shape the future in 2024.</p>
                    <a href="#">Read More</a>
                </div>
            </div>
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60" alt="News Image">
                <div class="news-card-content">
                    <h3>Global Economic Outlook</h3>
                    <p>An in-depth analysis of the current economic trends and forecasts for the coming year.</p>
                    <a href="#">Read More</a>
                </div>
            </div>
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60" alt="News Image">
                <div class="news-card-content">
                    <h3>Health and Wellness Tips</h3>
                    <p>Discover effective strategies and tips to maintain a healthy and balanced lifestyle.</p>
                    <a href="#">Read More</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2024 QuizNews. All rights reserved.</p>
        <div class="social-icons">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
        </div>
    </footer>

</body>
</html>
"""
    return HttpResponse(something)

def contact(request):
    something = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - QuizNews</title>
    <style>
        /* General Styles */
        body, html {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            background-color: #f0f2f5;
        }

        header {
            background-color: #ffffff;
            padding: 20px 40px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            animation: slideDown 0.5s ease-out;
        box-sizing:border-box;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #28a745;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: flex-end;
        }

        nav ul li {
            margin-left: 20px;
        }

        nav ul li a {
            font-size: 16px;
            color: #333;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: #28a745;
        }

        @keyframes slideDown {
            from { top: -100px; }
            to { top: 0; }
        }

        /* Contact Section */
        .contact-section {
            padding: 120px 20px 60px;
            background-color: #fff;
            text-align: center;
        }

        .contact-section h2 {
            font-size: 32px;
            color: #28a745;
            margin-bottom: 40px;
        }

        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background-color: #f8f9fa;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            animation: fadeIn 1s ease-out;
        }

        .contact-form label {
            font-size: 16px;
            color: #333;
            display: block;
            margin-bottom: 10px;
            text-align: left;
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 16px;
            color: #333;
            outline: none;
            transition: border-color 0.3s ease;
        }

        .contact-form input:focus,
        .contact-form textarea:focus {
            border-color: #28a745;
        }

        .contact-form button {
            background-color: #28a745;
            color: #fff;
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 50px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .contact-form button:hover {
            background-color: #218838;
            transform: translateY(-3px);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Footer */
        footer {
            background-color: #333;
            color: #fff;
            padding: 30px 20px;
            text-align: center;
            margin-top: 60px;
        }

        .social-links a {
            margin: 0 10px;
            color: #fff;
            font-size: 20px;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: #28a745;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 10px 0;
            }

            .contact-form {
                padding: 20px;
            }
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <nav class="navbar">
        <div class="logo">QuizNews</div>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/exam/">Quizzes</a></li>
            <li><a href="/about/">About</a></li>
            <li><a href="/contact/">Contact</a></li>
            <li><a href="/help/">Help</a></li>
        </ul>
    </nav>
    </header>

    <!-- Contact Section -->
    <section class="contact-section">
        <h2>Contact Us</h2>
        <div class="contact-form">
            <form action="#" method="POST">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message</label>
                <textarea id="message" name="message" rows="6" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 QuizNews. All rights reserved.</p>
        <div class="social-links">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
        </div>
    </footer>

</body>
</html>
"""
    return HttpResponse(something)

def about(request):
    something = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - QuizNews</title>
    <style>
        /* General Styles */
        body, html {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            background-color: #f0f2f5;
        }

        header {
            background-color: #ffffff;
            padding: 20px 40px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            animation: slideDown 0.5s ease-out;
        box-sizing:border-box;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #28a745;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: flex-end;
        }

        nav ul li {
            margin-left: 20px;
        }

        nav ul li a {
            font-size: 16px;
            color: #333;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: #28a745;
        }

        @keyframes slideDown {
            from { top: -100px; }
            to { top: 0; }
        }

        /* About Section */
        .about-section {
            padding: 120px 20px 60px;
            background-color: #fff;
            text-align: center;
        }

        .about-section h2 {
            font-size: 32px;
            color: #28a745;
            margin-bottom: 40px;
        }

        .about-content {
            max-width: 800px;
            margin: 0 auto;
            background-color: #f8f9fa;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            animation: fadeIn 1s ease-out;
        }

        .about-content p {
            font-size: 16px;
            color: #666;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .about-content h3 {
            font-size: 20px;
            margin-top: 20px;
            color: #28a745;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Footer */
        footer {
            background-color: #333;
            color: #fff;
            padding: 30px 20px;
            text-align: center;
            margin-top: 60px;
        }

        .social-links a {
            margin: 0 10px;
            color: #fff;
            font-size: 20px;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: #28a745;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 10px 0;
            }
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="logo">QuizNews</div>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/exam/">Quiz</a></li>
                <li><a href="/about/">About</a></li>
                <li><a href="/contact/">Contact</a></li>
                <li><a href="/help/">Help</a></li>
            </ul>
        </nav>
    </header>

    <!-- About Section -->
    <section class="about-section">
        <h2>About Us</h2>
        <div class="about-content">
            <p>Welcome to QuizNews, where your curiosity meets the latest news! We are a platform dedicated to delivering engaging quizzes and up-to-date news articles on a wide range of topics. Our goal is to make learning fun and staying informed an enjoyable experience.</p>
            <h3>Our Mission</h3>
            <p>Our mission is to combine the thrill of quizzes with the need to stay informed. Whether you're a trivia enthusiast or a news junkie, we've got something for you. We believe that staying updated on current events doesn't have to be boring—it can be interactive and rewarding!</p>
            <h3>Our Team</h3>
            <p>QuizNews is brought to you by a passionate team of content creators, quiz designers, and tech enthusiasts. We work hard to bring you the best content and a seamless user experience. We are always looking for ways to improve, so feel free to reach out to us with your feedback!</p>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 QuizNews. All rights reserved.</p>
        <div class="social-links">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
        </div>
    </footer>

</body>
</html>
"""
    return HttpResponse(something)

def help(request):
    something = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Help - QuizNews</title>
    <style>
        /* General Styles */
        body, html {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            background-color: #f0f2f5;
        }

        header {
            background-color: #ffffff;
            padding: 20px 40px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            animation: slideDown 0.5s ease-out;
        box-sizing:border-box;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #28a745;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: flex-end;
        }

        nav ul li {
            margin-left: 20px;
        }

        nav ul li a {
            font-size: 16px;
            color: #333;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        nav ul li a:hover {
            color: #28a745;
        }

        @keyframes slideDown {
            from { top: -100px; }
            to { top: 0; }
        }

        /* Help Section */
        .help-section {
            padding: 120px 20px 60px;
            background-color: #fff;
            text-align: center;
        }

        .help-section h2 {
            font-size: 32px;
            color: #28a745;
            margin-bottom: 40px;
        }

        .faq-item {
            background-color: #f8f9fa;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            animation: fadeIn 1s ease-out;
        }

        .faq-item h3 {
            font-size: 20px;
            margin-bottom: 10px;
        }

        .faq-item p {
            font-size: 16px;
            color: #666;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Footer */
        footer {
            background-color: #333;
            color: #fff;
            padding: 30px 20px;
            text-align: center;
            margin-top: 60px;
        }

        .social-links a {
            margin: 0 10px;
            color: #fff;
            font-size: 20px;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: #28a745;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 10px 0;
            }
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="logo">QuizNews</div>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/exam/">Quiz</a></li>
                <li><a href="/about/">About</a></li>
                <li><a href="/contact/">Contact</a></li>
                <li><a href="/help/">Help</a></li>
            </ul>
        </nav>
    </header>

    <!-- Help Section -->
    <section class="help-section">
        <h2>Help & FAQ</h2>
        <div class="faq-item">
            <h3>How do I take a quiz?</h3>
            <p>You can take a quiz by visiting the Quiz section of our website, selecting a quiz topic, and starting the quiz. Each quiz consists of multiple-choice questions, and you can submit your answers for instant feedback.</p>
        </div>
        <div class="faq-item">
            <h3>How often is the news updated?</h3>
            <p>We update our news section daily with the latest headlines and in-depth articles on a variety of topics. You can subscribe to our newsletter for regular updates.</p>
        </div>
        <div class="faq-item">
            <h3>Can I submit my own quizzes?</h3>
            <p>Currently, we do not offer a feature for users to submit their own quizzes, but we are working on adding this functionality soon. Stay tuned!</p>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 QuizNews. All rights reserved.</p>
        <div class="social-links">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
        </div>
    </footer>

</body>
</html>
"""
    return HttpResponse(something)