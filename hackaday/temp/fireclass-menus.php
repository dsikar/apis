<?php

/*********************************
fireclass-menus.php

Output json string for menu id.
If no menu id given, return all.

*********************************/

// get menu id if exists
$id = $_GET["id"];
// where statement
$where = "";
if(is_numeric($id)){
	$where = " WHERE MenuID = " . intval($id);
}
// connect
$db = new SQLite3('/home/ubuntu/sqlite/fireclass.db');
// query
$results = $db->query('SELECT * FROM tblMenus' . $where);
$json = "";
// build string
while ($row = $results->fetchArray()) {
	// {"menus":[{"MenuMain":"Panel and Loop Devices FAQs","MenuSub":"Excludes network issues.","MenuID":22}, (...) ]}
	$json  .= "{\"MenuMain\":\"" . $row[0] . "\",\"MenuSub\":\"" . $row[1] . "\",\"MenuID\":" . $row[2] . "},";
}
// output
if(strlen($json)>0){
	// wrap json and trim last comma if need be
	$json = "{\"menus\":[" . rtrim($json, ",") . "]}";
	echo $json;
}
?>

