<!-- 1. Write a HTML script containing use of media query for changing the background-color of html page to red if the viewport is between 800 pixels to 1200 pixels, changing the background color of html page to yellow if the viewport is between 799pixels to 500pixels otherwise if the viewport is less than 499pixels then the background-color should be changed to green. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color</title>
    <style>
        body{
            background-color: green;
        }

        @media (min-width: 500px) and (max-width: 799px){
            body{
                background-color: red;
            }
        }

        @media (min-width: 800px) and (max-width: 1200px){
            body{
                background-color: red;
            }
        }
    </style>
</head>
<body>
    
</body>
</html>