irBnB Clone - Web Static
This project involves building the static front-end structure for an AirBnB clone. The main goal is to create responsive, visually appealing web pages using HTML and CSS. Each task builds upon the previous to implement different design elements and layouts.

Project Overview
This project covers:

Creating and styling web pages for a header, footer, filter sections, and dynamic content sections like places and search results.
Writing modular and reusable CSS for various components.
Enhancing visual hierarchy and responsiveness.
Following W3C standards for valid and accessible HTML/CSS.
Learning Objectives
By completing this project, you will:

Understand and apply web static design principles.
Use semantic HTML5 tags effectively (e.g., <header>, <footer>, <section>, <article>).
Write modular CSS to maintain clean and scalable stylesheets.
Develop a structured workflow for building static web pages.Project Requirements

All files must end with a new line.
Use editors: vi, vim, or emacs.
Maintain a styles directory for all CSS files.
Store all images in the images folder.
Use semantic HTML5 tags without inline styles.
Use only class selectors for CSS; avoid IDs (#...).
Follow W3C standards (validate HTML/CSS with W3C Validator).

Project Tasks
0. Inline Styling
Create an HTML page with a header and footer using inline styles.
File: 0-index.html
Requirements:

Header: red background, height 70px, width 100%.
Footer: green background, height 60px, width 100%, text centered.
1. Head Styling
Style the header and footer using the <style> tag within the <head> section.
File: 1-index.html
Requirements:

Move inline styles into a <style> block.
Maintain the same layout as Task 0.
2. CSS Files
Separate styles into modular CSS files.
File: 2-index.html
CSS Files:

styles/2-common.css (global styles)
styles/2-header.css (header styles)
styles/2-footer.css (footer styles)
3. Zoning Done!
Add a favicon and adjust the header/footer styles.
File: 3-index.html
CSS Files:

styles/3-header.css
styles/3-footer.css
New Features:

Header/footer borders.
Adjusted font styles and alignment.
4. Search!
Add a filter section with a search button.
File: 4-index.html
CSS Files:

styles/4-common.css
styles/4-filters.css
New Features:

Create a filter box styled with borders and rounded corners.
Add a search button with hover effects.
5. More Filters
Enhance the filter section with "Locations" and "Amenities" options.
File: 5-index.html
CSS Files:

styles/5-filters.css
New Features:

Add filter titles and subtitles within sections.
Style borders and spacing.
6. It's (h)over
Add dropdown functionality for filters.
File: 6-index.html
CSS Files:

styles/6-filters.css
New Features:

Display dropdowns with hover effects.
Use nested lists for subcategories (e.g., states → cities).
7. Display Results
Create a "Places" section to display results.
File: 7-index.html
CSS Files:

styles/7-places.css
New Features:

Add an H1 title for "Places."
Style individual "Place" cards with borders, spacing, and a consistent layout.
8. More Details
Enhance the "Places" section with detailed information.
File: 8-index.html
CSS Files:

styles/8-places.css
New Features:

Add sections for price, description, user information, and icons.
Use borders, font styling, and spacing for better structure.
File Structure
css
Copy code
project/
│
├── images/
│   └── [All image assets here]
├── styles/
│   ├── 2-common.css
│   ├── 2-header.css
│   ├── 2-footer.css
│   ├── 4-common.css
│   ├── 4-filters.css
│   ├── 5-filters.css
│   ├── 6-filters.css
│   ├── 7-places.css
│   └── 8-places.css
├── 0-index.html
├── 1-index.html
├── 2-index.html
├── 3-index.html
├── 4-index.html
├── 5-index.html
├── 6-index.html
├── 7-index.html
├── 8-index.html
└── README.md
How to Run
Clone this repository.
Open any .html file in your browser (preferably Google Chrome).
Validate each page with W3C Validator.
Resources
HTML5 Reference
CSS Reference
W3C Validator

