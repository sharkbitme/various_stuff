<?php

$prvkey = openssl_pkey_get_private("file://PATH_TO_PRVKEY_PEM");
$cryptfile = fopen("PATH_TO_RESULTS_FILE", "r");
if ($cryptfile) {
    while (($line = fgets($cryptfile)) !== false) {
        $decoded = base64_decode($line);
        openssl_private_decrypt($decoded, $decrypted, $prvkey);
        echo $decrypted.PHP_EOL;
    }
    fclose($cryptfile);
}
?>
