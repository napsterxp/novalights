<?php
$myfile = fopen("webstatus.txt", "w");
$txt = "Stopped by user";
fwrite($myfile, $txt);
fclose($myfile);
shell_exec("sudo killall python");
header ("Location: /");
?>
