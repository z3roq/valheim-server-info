<?php
$file = file_get_contents('game_info_file');
$data = explode('|', $file);

if ($data[0] == 1) 
$status = "Online";
else
$status = "Offline";

echo "Server status: ".$status."<br>";
echo "Players: ".$data[1]."/10";

?>
