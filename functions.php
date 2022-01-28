<?php


function display(){

echo "<li><a href=\"#\">link1</a></li>
    <li><a href=\"#\">link2</a></li>
    <li><a href=\"#\">link3</a></li>
    <li><a href=\"#\">link4</a></li>
    <li><a href=\"#\">link5</a></li>";
}



function summary(){

  $output = exec('python summary.py');
    $f = @fopen("func.txt", "w+");
    fwrite($f,"sigh_new");
    fclose($f);
}

function emptythefile(){
  $f = @fopen("example.txt", "r+");
if ($f !== false) {
    ftruncate($f, 0);
    fclose($f);

}
}

?>
