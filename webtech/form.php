<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple form</title>
    <style>
        *{
            margin: 5px;
        }

        button{
            height: 20px; 
            width: 100px; 
            background-color: aqua;
        }
    </style>
</head>
<body>
    <form action="#" method="post">
        <label for="firstname">First Name</label>
        <input type="text" name="firstname" id="firstname" style="background-color: aqua;"><br>
        <input type="text" name="lastname" id="lastname" style="background-color: aqua;">
        <label for="lastname"> Last Name</label>
        <input type="email" name="email" placeholder="Enter email"><br>
        <label for="gender">Gender</label>
        Male <input type="radio" name="gender">
        Female <input type="radio" name="gender">
        Others <input type="radio" name="gender">
        <br>
        Password
        <input type="password" name="password" id=""><br>
        <button type="submit"><b>Submit</b></button>
    </form>
</body>
</html>