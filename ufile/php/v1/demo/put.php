<?php

require_once("../ucloud/proxy.php");

$bucket = "your bucket";
$key    = "your key";
$file   = "local file path";

list($data, $err) = UCloud_PutFile($bucket, $key, $file);
if ($err) {
	echo "error: " . $err->ErrMsg . "\n";
	echo "code: " . $err->Code . "\n";
	exit;
}
echo "ETag: " . $data['ETag'] . "\n";
