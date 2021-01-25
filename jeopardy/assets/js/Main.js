

//window.onload = nombre_de_la_funcion;
(() => {

	


	
	const btn_iniciar = document.getElementById("iniciar_jeopardy");

	//eventos
	btn_iniciar.addEventListener('click', () => {
		console.log(' evento iniciar '); 

		
		

		
		
		

		
	});
	





let obJson = {
	id: "1",
	equipo: [{"nombre": "eq1","integrantes":"2","puntos":"100"}],
	fecha: "2021-01-24"
}
		
})();



/*exampleModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient



  const fileJSON = './assets/js/preguntas.json';
	const request = new XMLHttpRequest();

	request.open('GET', fileJSON);

	request.responseType = 'json';
	request.send();


	request.onload = function() {
		const ask = request.response;
  		populateHeader(ask);
  		showHeroes(ask);
  		console.log(ask);
	}


	//ajax
		var xhtml = new XMLHttpRequest();
		xhtml.onreadystatechange = function(){
			if (this.readyState == 4 && this.status == 200) {
				var myObject = JSON.parse(this.responseText);
				console.log(myObject);
			}
		};
		xhtml.open("GET", "cuestionrio.txt", true);
		xhtml.send();


  */

