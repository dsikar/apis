<?php

/*********************************
fireclass-menus.php

Output json string for menu id.
If no menu id given, return all.

*********************************/

// get menu id if exists
$label = $_GET["label"];
// where statement
$where = "";
if($label){
	$where = " WHERE Label = '" . $label . "'";
}
// connect
$db = new SQLite3('/home/ubuntu/sqlite/fireclass.db');
// query
$results = $db->query('SELECT * FROM tblText' . $where);
$json = "";
// build string
while ($row = $results->fetchArray()) {
	// {"menus":[{"MenuMain":"Panel and Loop Devices FAQs","MenuSub":"Excludes network issues.","MenuID":22}, (...) ]}
	$json  .= "{\"Label\":\"" . $row[0] . "\",\"Text\":\"" . $row[1] . "\"},";
}
// output
if(strlen($json)>0){
	// wrap json and trim last comma if need be
	$json = "{\"Text\":[" . rtrim($json, ",") . "]}";
	echo $json;
}
?>

