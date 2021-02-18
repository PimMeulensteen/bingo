<?php
    echo "hello world\n";
    echo "generating card for ".$_POST["email"]."\n";
    $command = "python3 main.py ".$_POST["email"];
    $output = shell_exec($command);
    echo $output;
    echo "done\n";
?>
