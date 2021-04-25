<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="utf-8">
	<title>Sitio con PHP</title>
 	<link href="assets/css/styles.css" rel="StyleSheet">

</head>
<body>
	<div class="contein">
		<header class="contenn">
			<div class="nav-h">
				<div class="div-h">
					<h3>Estructura con PHP</h3>
					<?php
						echo "Linea desde PHP";
					?>
				</div>
			</div>
			<div class="div-h2">
					<input type="search" id="buscar" name="busca" />	
				</div>
		</header>


<form method="post" action="" name="signup-form">
	<div class="form-element">
		<label>Username</label>
		<input type="text" name="username" pattern="[a-zA-Z0-9]+" requered />
	</div>
	<div class="form-element">
		<label>Email</label>
		<input type="email" name="email" requered />
	</div>
	<div class="form-element">
		<label>Password</label>
		<input type="password" name="password" requered />
	</div>
	<button type="submit" name="register" value="register">Register</button>
</form>

</body>
</html>
