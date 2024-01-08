<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $x = $_POST['x'];
    $y = $_POST['y'];
    $z = $_POST['z'];

    $sum = $x + $y + $z;
    echo `Sum is $sum.`;
}
?>