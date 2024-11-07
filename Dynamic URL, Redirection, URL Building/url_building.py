# Flask URL Handling: Dynamic URLs, Redirection, and URL Building

This project demonstrates how to handle dynamic URLs, URL redirection, and URL building in a Flask web application. Each component is implemented in separate Python files for easy understanding and modularity.

## Table of Contents

- [Overview](#overview)
- [Files and Functionality](#files-and-functionality)
  - [dynamic_url.py](#dynamic_urlpy)
  - [url_redirection.py](#url_redirectionpy)
  - [url_building.py](#url_buildingpy)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)

## Overview

In this project, we explore three key concepts:

1. **Dynamic URLs**: Generating URLs that can change based on user input.
2. **URL Redirection**: Redirecting users to specific pages based on conditions.
3. **URL Building**: Constructing URLs dynamically within the application using Flask's `url_for` function.

These concepts are commonly used in web applications to enhance user navigation, maintain functionality during site updates, and provide personalized responses.

## Files and Functionality

### dynamic_url.py

The `dynamic_url.py` file demonstrates the creation of dynamic URLs in a Flask application.

- **Home Page** (`/home` or `/`): Displays a welcome message.
- **Dynamic Welcome Page** (`/welcome/<name>`): Greets the user with a personalized message using their name from the URL.

Example:
```python
@app.route("/welcome/<name>")
def Lt(name):
    return f"<h1>Hi {name.title()}, welcome here </h1>"
