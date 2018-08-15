<?php

// expecting fc or zx
$product_id   = $_GET['prod'];

// expecting en, de
$language_id  = $_GET['lang'];

// expected, pages, menus, buttons
$content_id   = $_GET['cont'];

include_once  './inc_json_pages.php'; 
include_once  './inc_json_menus.php'; 
include_once  './inc_json_buttons.php'; 
include_once  './inc_json_text.php'; 


function notSupported()
{
	echo "Not Supported";
}

function HandlePages( $product, $language )
{
	 if ($product == "mzx")
	 {
		 if ($language  == "en")
			 MXPagesEN();
		 else if ($language  == "de")
			 MXPagesDE();
		 else 
			 notSupported();
			 
	 }
	 else if ($product == "fc")
	 {
		 if ($language  == "en")
			 FCPagesEN();
		 else 
			 notSupported();
	 }
	 else
		 notSupported();
}	 


function HandleMenus( $product, $language )
{
	 if ($product == "mzx")
	 {
		 if ($language  == "en")
			 MZXMenusEN();
		 else if ($language  == "de")
			 MZXMenusDE();
		 else 
			 notSupported();
			 
	 }
	 else if ($product == "fc")
	 {
		 if ($language  == "en")
			 FCMenusEN();
		 else 
			 notSupported();
	 }
	 else
		 notSupported();
}




function HandleButtons( $product, $language )
{
	 if ($product == "mzx")
	 {
		 if ($language  == "en")
			 MZXButtonsEN();
		 else if ($language  == "de")
			 MZXButtonsDE();
		 else 
			 notSupported();
			 
	 }
	 else if ($product == "fc")
	 {
		 if ($language  == "en")
			 FCButtonsEN();
		 else 
			 notSupported();
	 }
	 else
		 notSupported();
}


function HandleText( $product, $language )
{
	 if ($product == "mzx")
	 {
		 if ($language  == "en")
			 MZXTextEN();
		 else if ($language  == "de")
			 MZXTextDE();
		 else 
			 notSupported();
			 
	 }
	 else if ($product == "fc")
	 {
		 if ($language  == "en")
			 FCTextEN();
		 else 
			 notSupported();
	 }
	 else
		 notSupported();
}



if ($content_id == "pages")
	HandlePages($product_id, $language_id);

else if ($content_id == "menus")
	HandleMenus($product_id, $language_id);

else if ($content_id == "text")
	HandleText($product_id, $language_id);

else if ($content_id == "buttons")
	Handlebuttons($product_id, $language_id);
else
	notSupported();


?>
