<?php
session_start();

$_SESSION["username"] = "ronil";

if(isset($_SESSION["username"])){
    $username = $_SESSION["username"];
}
else{
    $username = "guest";
}

echo "Hello ". $username;

session_destroy();

?>