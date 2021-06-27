
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


<form method="post" action="" name="signin-form">
	<div class="form-element">
		<label>Username</label>
		<input type="text" name="username" pattern="[a-zA-z0-9]+" required />
	</div>
	<div class="form-element">
		<label>Password</label>
		<input type="password" name="password" required />
	</div>
	<button type="submit" name="login" value="Login">Log In</button>
</form>

</body>
</html>
