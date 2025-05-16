# 🎬 Movie Preference Survey (Python + Shiny for Python)

A simple interactive survey web app for collecting film preferences using [Shiny for Python](https://shiny.posit.co/py/). This tool collects user input on basic demographics and movie ratings, and stores responses locally in a CSV file.

## 🔧 Features

- Clean, responsive design with two-column layout
- Demographic and film rating inputs via sliders
- Input validation to ensure required fields are completed
- Responses saved locally to `responses.csv` using `pandas` and `pathlib`
- Confirmation modal after successful submission

## 🚀 Technologies Used

- [Shiny for Python](https://shiny.posit.co/py/)
- Python 3.10+
- `pandas`
- `pathlib` (standard library)

## My Approach
This was a beginner project to practise building simple web apps using Shiny in Python. I wanted to focus on creating a clean, user-friendly form that would allow people to rate a few films and submit their preferences.

I started by setting up basic form inputs using built-in Shiny UI functions. I included a mix of input types such as text boxes, dropdowns, and sliders. To keep things organised and readable, I grouped inputs into two columns — one for demographic information and one for film ratings.

Instead of advanced layout tools, I used simple CSS styling to centre the form and improve spacing. I chose pastel colours to keep the look light and accessible.

For storage, I used pandas to collect and append each submission to a CSV file, and pathlib to handle file paths in a cross-platform way. I originally experimented with star ratings but found sliders easier to implement cleanly for now.

This project helped me practise UI layout, form handling, and basic data storage with Python and Shiny.

## Requirements
pip install shiny pandas

## Running the app 
shiny run --reload app.py
