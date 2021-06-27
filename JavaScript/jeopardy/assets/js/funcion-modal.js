
(() => {
'use strict'
//import * as data from './preguntas.json';

//const preguntas = require('./preguntas.json');
//const {ask} = data;
//console.log(ask);

/*
Modal para categ-1

*/
const btn_c1v5 = document.getElementById("bt-c1v5");
const btn_c1v4 = document.getElementById("bt-c1v4");
const btn_c1v3 = document.getElementById("bt-c1v3");
const btn_c1v2 = document.getElementById("bt-c1v2");
const btn_c1v1 = document.getElementById("bt-c1v1");

/*
Modal para categ-2

*/
const btn_c2v5 = document.getElementById("bt-c2v5");
const btn_c2v4 = document.getElementById("bt-c2v4");
const btn_c2v3 = document.getElementById("bt-c2v3");
const btn_c2v2 = document.getElementById("bt-c2v2");
const btn_c2v1 = document.getElementById("bt-c2v1");

/*
Modal para categ-3

*/

/*
Modal para categ-4

*/

/*
Modal para categ-5

*/
const btn_c5v1 = document.querySelector("#bt-c5v1");


/*
opciones respuesta
*/
const pregunta = document.getElementById("question");
const opcion1 = document.getElementById("option1");
const opcion2 = document.getElementById("option2");
const opcion3 = document.getElementById("option3");

let titlecat1v5 = document.getElementById("exampleModalLabel");


//eventos cat-1
	btn_c1v5.addEventListener('click', () => {
		titlecat1v5.innerHTML = "Pregunta Categoria 1 Valor 500";
		pregunta.innerHTML = objetoGeneral[0].question;
		opcion1.innerHTML = objetoGeneral[0].res_1;
		opcion2.innerHTML = objetoGeneral[0].res_2;
		opcion3.innerHTML = objetoGeneral[0].res_3;
	});

	btn_c1v4.addEventListener('click', () => {
		console.log(cat1v5);
		cat1v5.innerHTML = "Pregunta Categoria 1 Valor 400";
	});

	btn_c1v3.addEventListener('click', () => {
		console.log(cat1v5);
		cat1v5.innerHTML = "Pregunta Categoria 1 Valor 300";
	});

	btn_c1v2.addEventListener('click', () => {
		console.log(cat1v5);
		cat1v5.innerHTML = "Pregunta Categoria 1 Valor 200";
	});

	btn_c1v1.addEventListener('click', () => {
		console.log(cat1v5);
		cat1v5.innerHTML = "Pregunta Categoria 1 Valor 100";
	});

//eventos cat-2
//eventos cat-3
//eventos cat-4
//eventos cat-5
	btn_c5v1.addEventListener('click', () => {
		console.log(cat1v5);
		cat1v5.innerHTML = "Pregunta Categoria 5 Valor 100";
	});

})();


  const objetoGeneral = [
            {
              "claveAsk"   : "cat1val1",
              "question"   : "¿Qué es Windows?",
              "res_1"      : "Un sistema operativo",
              "res_2"      : "Un editor de Imágenes",
              "res_3"      : "Un Disco Rígido",
              "correcto"   : "res_1"
            },
            {
              "claveAsk": "cat2val1",
              "question": "La Informática es:",
              "res_1": "Ciencia que estudia la gestión de información con medios electrónicos",
              "res_2": "Ciencia que estudia el funcionamiento del computador",
              "res_3": "Ciencia que estudia el uso de internet",
              "correcto": "res_1"
            },
            {
              "claveAsk": "cat3val1",
              "question": "¿Qué es el software?",
              "res_1": "Parte física del computador",
              "res_2": "Parte tangible del computador",
              "res_3": "Conjunto de programas del computador",
              "correcto": "res_3"
            },
            {
              "claveAsk": "cat4val1",
              "question": "¿Señala el hardware de la siguiente lista?",
              "res_1": "Windows",
              "res_2": "Impresora",
              "res_3": "Paint",
              "correcto": "res_2"
            },
            {
              "claveAsk": "cat5val1",
              "question": "¿Cuál es la unidad más pequeña de representación de información en un ordenador?",
              "res_1": "Bit",
              "res_2": "Byte",
              "res_3": "Mega Byte",
              "correcto": "res_1"
            },
            {
             "claveAsk": "cat1val2",
              "question": "¿El elemento principal de la computadora, él cual coordina y realiza las operaciones del sistema es?",
              "res_1": "Memoria",
              "res_2": "Disco Duro",
              "res_3": "Procesador",
              "correcto": "res_3"
            },
            {
              "claveAsk": "cat1val3",
              "question": "¿Los computadores almacenan la información utilizando?",
              "res_1": "Sistema Binario",
              "res_2": "Sistema Decimal",
              "res_3": "Sistema Hexadecimal",
              "correcto": "res_1"
            }
]


