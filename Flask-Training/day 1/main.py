from flask import Flask

app = Flask(__name__)


@app.route('/')
def Welcome():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SISTec - Excellence in Education</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

.logo h1 {
    font-size: 2rem;
    display: inline;
}

nav ul {
    list-style: none;
    float: right;
}

nav ul li {
    display: inline;
    margin-left: 20px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

.hero {
    background: url('/static/sistec.jpeg') no-repeat center center/cover;
    height: 400px;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.hero h2 {
    font-size: 3rem;
    margin-bottom: 10px;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 20px;
}

.hero .btn {
    background-color: #f04c4c;
    padding: 10px 20px;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}

.about, .courses, .events {
    padding: 50px 0;
}

.about h2, .courses h2, .events h2 {
    text-align: center;
    margin-bottom: 30px;
}

.course-grid, .event-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.course-item, .event-item {
    background: #f4f4f4;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
}

footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

footer p {
    margin: 0;
}
</style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <div class="logo">
                <h1>SISTec</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Courses</a></li>
                    <li><a href="#">Admissions</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Welcome to SISTec</h2>
            <p>Shaping the Future of Engineering & Technology</p>
            <a href="#" class="btn">Explore Courses</a>
        </div>
    </section>

    <!-- About Section -->
    <section class="about">
        <div class="container">
            <h2>About SISTec</h2>
            <p>SISTec is a leading institution providing excellence in engineering and technology education. We are committed to developing the next generation of engineers with innovative teaching methods and modern infrastructure.</p>
        </div>
    </section>

    <!-- Courses Section -->
    <section class="courses">
        <div class="container">
            <h2>Our Courses</h2>
            <div class="course-grid">
                <div class="course-item">
                    <h3>Computer Science & Engineering</h3>
                    <p>Learn cutting-edge technologies like AI, ML, and Cloud Computing.</p>
                </div>
                <div class="course-item">
                    <h3>Mechanical Engineering</h3>
                    <p>Explore mechanical systems and the future of automation.</p>
                </div>
                <div class="course-item">
                    <h3>Electrical Engineering</h3>
                    <p>Master electrical systems and smart grids for the modern world.</p>
                </div>
                <div class="course-item">
                    <h3>Civil Engineering</h3>
                    <p>Build a strong foundation in construction and structural engineering.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Events Section -->
    <section class="events">
        <div class="container">
            <h2>Upcoming Events</h2>
            <div class="event-grid">
                <div class="event-item">
                    <h3>Tech Fest 2024</h3>
                    <p>Join us for a celebration of innovation and technology.</p>
                </div>
                <div class="event-item">
                    <h3>Annual Sports Meet</h3>
                    <p>Get ready for an action-packed day of sports and fun.</p>
                </div>
                <div class="event-item">
                    <h3>Alumni Meet</h3>
                    <p>Reconnect with our proud graduates and share experiences.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2024 SISTec. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/home/')
def home():
    return '<h1>Welcome to SISTec Bhopal</h1>'

@app.route('/api/')
def api():
    return {'status': 'ok', 'title': 'this is an api'}


if __name__ == '__main__':
    app.run(debug=True)