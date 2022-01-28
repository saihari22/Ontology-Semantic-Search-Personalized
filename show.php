<?php
include 'functions.php';
ini_set('max_execution_time', 300);
$query = $_GET['query'];
$username = $_GET['username'];
$pieces = explode(" ", $query);
$result = "\"" . implode('", "', $pieces) . "\"";
$fin = array($result);
?>

<html>
<head>
<title>Results</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="/Ontology/scripts/main.js"></script>
</head>
<link href="/Ontology/styles/main.css" type="text/css" rel="stylesheet" />
<body>

<div>
  <br>

<h1>Results for
<?php
echo $query;
?><br></h1>
<br><br>
<div class="aboutpane"><p>
  <h5>
<?php
$t = exec('C:\Users\Sairam\Anaconda3\python.exe recommend.py ' . $username . " " . json_encode($fin));
$r = explode(" ", $t);
$r = str_replace('\'', '', $r);
$r = str_replace('(', '', $r);
$r = str_replace(')', '', $r);
$r = str_replace(',', '', $r);
$r = str_replace('[', '', $r);
foreach ($r as $element) {
    echo '<li>';
    echo "<a class='link' href='$element'>$element</a>";
    echo '</li>';
}
emptythefile();
?>
</h5>
  <br><br>
</p></div>
</div>
<a class ="spbtn" href="index.php">Home</a>

</body>
</html>
