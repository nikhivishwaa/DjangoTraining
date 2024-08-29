from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):

    que = [
    {
      "question": "What does HTML stand for?",
      "options": [
        "Hyper Text Markup Language",
        "Home Tool Markup Language",
        "Hyperlinks and Text Markup Language",
        "Hyper Tool Machine Language"
      ],
      "correctAnswer": "Hyper Text Markup Language"
    },
    {
      "question": "Which CSS property is used to change the background color?",
      "options": [
        "background-color",
        "color",
        "bgcolor",
        "background"
      ],
      "correctAnswer": "background-color"
    },
    {
      "question": "Which of the following is not a JavaScript data type?",
      "options": [
        "Number",
        "Boolean",
        "String",
        "Float"
      ],
      "correctAnswer": "Float"
    },
    {
      "question": "Which HTML element is used for the largest heading?",
      "options": [
        "<h1>",
        "<h6>",
        "<heading>",
        "<head>"
      ],
      "correctAnswer": "<h1>"
    },
    {
      "question": "Which of the following is a CMS platform?",
      "options": [
        "React",
        "Node.js",
        "WordPress",
        "Vue.js"
      ],
      "correctAnswer": "WordPress"
    }
  ]




    template = loader.get_template('index.html')
    paper = template.render(context={'questions':que})

    return HttpResponse(paper)
