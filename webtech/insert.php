<?php
include "./dbconnect.php";

if($_SERVER["REQUEST_METHOD"] == "POST"){
    $name = $_POST["name"];
    $address = $_POST["address"];
    $phone = $_POST["phone"];

    $sqlcheck = "SELECT * FROM `my_form` WHERE `phone` = '$phone'";
    $result = mysqli_query($conn,$sqlcheck);
    if(mysqli_num_rows($result)>0){
        echo "Data exists!";
    }
    else{
        $sql = "INSERT INTO `my_form` (`name`,`address`,`phone`) VALUES('$name','$address','$phone')";
        if (mysqli_query($conn,$sql)){
            echo "Data Inserted";
        }
        else{
            echo "Data insertion unsuccessfull". mysqli_error($conn);
        }
    }
    mysqli_close($conn);
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="#" method="post">
        <input type="text" name="name" id="name" placeholder="Enter name"><br>
        <input type="text" name="address" id="address" placeholder="Enter address"><br>
        <input type="text" name="phone" id="phone" placeholder="Enter phone"><br>
        <button type="submit">Submit</button>
    </form>

    <ol type="1" start="10">
        <li>Tiger</li>
        <li>Lion</li>
        <li>Deer</li>
        <li>Elephant</li>
    </ol>
</body>
</html>