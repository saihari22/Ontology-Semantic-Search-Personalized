<?php
// include 'show.php';
$link = $_GET['link'];
$username = $_GET['username'];

// if(!session_id()) session_start();
// if(!isset($_SESSION['username'])) {
//   $_SESSION['username'] = $username;
// }
echo $link;
$up=exec('C:\Users\Sairam\Anaconda3\python.exe increment.py ' . $link . " " . $username);

 ?>
