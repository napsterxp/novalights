<?php
$myfile = fopen("webstatus.txt", "w");
$txt = "Running";
fwrite($myfile, $txt);
fclose($myfile);
shell_exec("sudo bash webscript.sh > /dev/null 2>/dev/null &");
header ("Location: /");
?>
