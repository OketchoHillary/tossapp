<?PHP
	session_start();
	ob_start();
	
	require '../database_connection.php';		
	//require 'core.inc.php';
	
	
	if(isset($_SESSION['username']) && isset($_SESSION['user_id']) || isset($_SESSION['user_phno'])  ){
		//put stored session variables into local php variables
		$user_id = $_SESSION['user_id'];
		$username = $_SESSION['username'];
		$phone_number = $_SESSION['user_phno'];
		
		
		include 'game_header.php';  
	?>
	<head>
		<title>Slot Machine Game!</title>
		<link rel="stylesheet" type="text/css" href="game_css/slots.css" >
		
	</head>
	<!--PAGE CONTENT -->
	<div style="padding-left:10px; padding-top:10px;">
		
		<!--
			<img id="gif_moving" src="img/slot_moving.gif" alt="Tartan" />
			<img id="slot2" class="slot_img" src="img/slots/slot2.png" alt="Tartan" />
			<img id="slot3" class="slot_img" src="img/slots/slot3.png" alt="Tartan" />
			<img id="slot1" class="slot_img" src="img/slots/slot1.png" alt="Tartan" />
		-->
		
		<p>THIS IS A SLOT MACHINE</p>
		<div id="machine_slot" class="row"> 
			<div class="col-xs-3 col-md-3">
				
			</div> 
			
			<div class="col-xs-6 col-md-6">
				<div class="row">
					<div id="slot_coloms" class="col-xs-4 col-md-4">
						<div class="slot_out" >
							<div id="machine_slot1" class="slot_displays"  class="col-xs-4 col-md-4">
								<!-- MACHINE SLOT 1 -->
							</div> 
						</div> 
					</div>
					
					<div id="slot_coloms" class="col-xs-4 col-md-4">
						<div class="slot_out" >
							<div id="machine_slot2" class="slot_displays" class="col-xs-4 col-md-4">
								<!-- MACHINE SLOT 2 -->
							</div>
						</div>
					</div>
					
					<div id="slot_coloms" class="col-xs-4 col-md-4">
						<div class="slot_out" >
							<div id="machine_slot3" class="slot_displays" class="col-xs-4 col-md-4">
								<!-- MACHINE SLOT 3 -->
							</div> 
						</div> 
					</div> 
				</div> 
				
				<div class="row">
					<div class="panel-heading">
						<form action="#" method="POST" role="form" autocomplete="off">
							<input type="text" name="bet" placeholder="Place your Bet Here" class="form-control"style="width:204px;"/><br/> 
							<input type="button" class="btn btn-success btn-lg btn-line" value="RETRAY">
							<input  id="pull"  type="button" class="btn btn-danger btn-lg btn-line" value="PLAY">
						</form>
					</div>
				</div>
			</div> 
			
			<div class="col-xs-3 col-md-3">
			</div> 
		</div> 
		
	</div><!--END PAGE CONTENT -->
	
	
	<!--LINKING THE SCIPTS -->
	<script type="text/javascript" src="game_js/jQuery_1.11.3.js"></script>
	<script type="text/javascript" src="game_js/slots_effects.js"></script>
	<!--LINKING THE SCIPTS -->
	
	
	
	<?PHP 
		include "game_footer.php";	
	?>
	
	
	<?php	
		} else {
		header('location: login.php');
	}	
?>
