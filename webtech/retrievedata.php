<?php
include 'dbconnect.php';
$sql = "SELECT * FROM `my_form`";

$result = mysqli_query($conn,$sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table,th,tr,td{
            border: 1px solid black;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
    
    <table>
        <tr>
            <th>s_id</th>
            <th>name</th>
            <th>address</th>
            <th>phone</th>
        </tr>
        <?php
            while($row = mysqli_fetch_assoc($result)){
                echo"<tr>";
                echo"<td>".$row["s_id"]."</td>";
                echo"<td>".$row["name"]."</td>";
                echo"<td>".$row["address"]."</td>";
                echo"<td>".$row["phone"]."</td>";
                echo "</tr>";
            }
        ?>
    </table>
    <?php mysqli_close($conn); ?>
</body>
</html>