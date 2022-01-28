<?php
include ('functions.php');
$query = $_GET['query'];
// $vbl = $_POST["action"];

//write to origina.txt
$myfile = fopen("original.txt", "w") or die("Unable to open file!");
fwrite($myfile, $query);

$pieces = explode(" ", $query);

$result = "\"" . implode ( '", "', $pieces ) . "\"";
$fin=array($result);

fclose($myfile);

$res = exec('C:\Users\Sairam\Anaconda3\python.exe retrieve.py ' . json_encode($fin) . ' 2>&1');
echo $res;
$resultData = json_decode($res, true);
var_dump($resultData);

?>
