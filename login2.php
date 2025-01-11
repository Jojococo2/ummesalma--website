<?php
       $email=$_POST["email"];
       $mobile=$_POST["mname"];
       $pass=$_POST["pass"];
    $servername="localhost";
    $username="root";
    $password="";
    $dbname="umme";

    $conn=mysqli_connect($servername,$username,$password,$dbname);
    if($conn){
        echo"connected";
    }
    /*$q1=mysqli_query($conn,"create table logins(Email varchar(30),Mobile varchar(30),Password varchar(30))");
    if($q1){
        echo" one connected";
    }*/
    $q2=mysqli_query($conn,"insert into logins(Email,Mobile,Password)values('$email','$mobile','$pass')");
    if($q2){
        echo" one";
    }

    ?>