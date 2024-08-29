from django.shortcuts import render
from django.http import HttpResponse


def exam(request):
    something = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz - QuizNews</title>
    <style>
        /* General Styles */
        body,
        html {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            background-color: #f0f2f5;
        }

        header {
            background-color: #ffffff;
            padding: 20px 40px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            animation: slideDown 0.5s ease-out;
            box-sizing: border-box;
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
            from {
                top: -100px;
            }

            to {
                top: 0;
            }
        }

        /* Quiz Section */
        .quiz-section {
            padding: 120px 20px 60px;
            background-color: #fff;
            text-align: center;
        }

        .quiz-section h2 {
            font-size: 32px;
            color: #28a745;
            margin-bottom: 40px;
        }

        .quiz-box {
            max-width: 600px;
            margin: 0 auto;
            background-color: #f8f9fa;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            animation: fadeIn 1s ease-out;
        }

        .quiz-box h3 {
            font-size: 20px;
            color: #333;
            margin-bottom: 20px;
            text-align: left;
        }

        .quiz-box ul {
            list-style-type: none;
            padding: 0;
        }

        .quiz-box ul li {
            margin-bottom: 15px;
            text-align: left;
        }

        .quiz-box input[type="radio"] {
            margin-right: 10px;
        }

        .quiz-box button {
            background-color: #28a745;
            color: #fff;
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 50px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .quiz-box button:hover {
            background-color: #218838;
            transform: translateY(-3px);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
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

            .quiz-box {
                padding: 20px;
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

    <!-- Quiz Section -->
    <section class="quiz-section">
        <h2>Test Your Knowledge!</h2>
        <div class="quiz-box">
            <form id="quizForm">
                <h3>1. What is the capital of France?</h3>
                <ul>
                    <li><input type="radio" name="q1" value="a"> A) Berlin</li>
                    <li><input type="radio" name="q1" value="b"> B) Madrid</li>
                    <li><input type="radio" name="q1" value="c"> C) Paris</li>
                    <li><input type="radio" name="q1" value="d"> D) Rome</li>
                </ul>

                <h3>2. Which planet is known as the Red Planet?</h3>
                <ul>
                    <li><input type="radio" name="q2" value="a"> A) Earth</li>
                    <li><input type="radio" name="q2" value="b"> B) Mars</li>
                    <li><input type="radio" name="q2" value="c"> C) Jupiter</li>
                    <li><input type="radio" name="q2" value="d"> D) Venus</li>
                </ul>

                <h3>3. Who wrote "To Kill a Mockingbird"?</h3>
                <ul>
                    <li><input type="radio" name="q3" value="a"> A) Harper Lee</li>
                    <li><input type="radio" name="q3" value="b"> B) Mark Twain</li>
                    <li><input type="radio" name="q3" value="c"> C) Jane Austen</li>
                    <li><input type="radio" name="q3" value="d"> D) F. Scott Fitzgerald</li>
                </ul>

                <h3>4. What is the largest ocean on Earth?</h3>
                <ul>
                    <li><input type="radio" name="q4" value="a"> A) Atlantic Ocean</li>
                    <li><input type="radio" name="q4" value="b"> B) Indian Ocean</li>
                    <li><input type="radio" name="q4" value="c"> C) Pacific Ocean</li>
                    <li><input type="radio" name="q4" value="d"> D) Arctic Ocean</li>
                </ul>

                <h3>5. What is the chemical symbol for water?</h3>
                <ul>
                    <li><input type="radio" name="q5" value="a"> A) H2</li>
                    <li><input type="radio" name="q5" value="b"> B) O2</li>
                    <li><input type="radio" name="q5" value="c"> C) H2O</li>
                    <li><input type="radio" name="q5" value="d"> D) CO2</li>
                </ul>

                <button type="submit">Submit</button>
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

    <!-- JavaScript -->
    <script>
        document.getElementById('quizForm').addEventListener('submit', function (e) {
            e.preventDefault();
            let score = 0;

            if (document.querySelector('input[name="q1"]:checked')?.value === 'c') score++;
            if (document.querySelector('input[name="q2"]:checked')?.value === 'b') score++;
            if (document.querySelector('input[name="q3"]:checked')?.value === 'a') score++;
            if (document.querySelector('input[name="q4"]:checked')?.value === 'c') score++;
            if (document.querySelector('input[name="q5"]:checked')?.value === 'c') score++;

            alert(`Your score is: ${score}/5`);
        });
    </script>

</body>

</html>

"""
    return HttpResponse(something)

def result(request):
    something = "result page"
    return HttpResponse(something)

