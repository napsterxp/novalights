<?php
$myfile = fopen("webstatus.txt", "w");
$txt = "System Shutdown";
fwrite($myfile, $txt);
fclose($myfile);
shell_exec("sudo killall python");
shell_exec("sudo shutdown now > /dev/null 2>/dev/null &");
header ("Location: http://www.novafm.co.uk");

?>
