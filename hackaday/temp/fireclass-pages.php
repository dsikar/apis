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
	$where = " WHERE pageID = " . intval($id);
}

// connect
$db = new SQLite3('/home/ubuntu/sqlite/fireclass.db');

// query
$results = $db->query('SELECT * FROM tblPages' . $where);
$json = "";

// build string
while ($row = $results->fetchArray()) {
	$json .= "{\"Title\":\"" . $row[0] . "\",\"Title2\":\"" . $row[1] . "\",\"stockcode\":\"" . $row[2] . "\"";
	$json .= ",\"InMenu\":" . $row[3] . ",\"ImageMini\":\"" . $row[4] . "\",\"Image1\":\"" . $row[5] . "\"";
	$json .= ",\"Image2\":\"" . $row[6] . "\",\"Image3\":\"" . $row[7] . "\",\"Image4\":\"" . $row[8] . "\"";
	$json .= ",\"Image5\":\"" . $row[9] . "\",\"long\":\"" . $row[10] . "\",\"hasPDF\":\"" . $row[11] . "\"";
	$json .= ",\"pageID\":" . $row[12] . "},";
}

// output
if(strlen($json)>0){
	// wrap json and trim last comma if need be
	$json = "{\"pages\":[" . rtrim($json, ",") . "]}";
	echo $json;
}
?>

