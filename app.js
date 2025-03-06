function enviar() {
    var contenido = document.querySelector('#contenido');
    var v1 = Number(document.querySelector('#t1').value);
    var v2 = Number(document.querySelector('#t2').value);
    var url = "";

    if (document.querySelector('#opcion1').checked) {
        url = `http://127.0.0.1:5000/${v1}/${v2}`;
    } else if (document.querySelector('#opcion2').checked) {
        url = `http://127.0.0.1:5000/resta/${v1}/${v2}`;
    } else if (document.querySelector('#opcion3').checked) {
        url = `http://127.0.0.1:5000/multiplicacion/${v1}/${v2}`;
    } else if (document.querySelector('#opcion4').checked) {
        url = `http://127.0.0.1:5000/division/${v1}/${v2}`;
    } else if (document.querySelector('#opcion5').checked) {
        url = `http://127.0.0.1:5000/potenciacion/${v1}/${v2}`;
    } else if (document.querySelector('#opcion6').checked) {
        if (!v1) {
            swal("Mensaje", "Por favor, ingrese un valor para calcular el seno", "warning");
            return;
        }
        url = `http://127.0.0.1:5000/seno/${v1}`;
    } else if (document.querySelector('#opcion7').checked) {
        if (!v1) {
            swal("Mensaje", "Por favor, ingrese un valor para calcular el coseno", "warning");
            return;
        }
        url = `http://127.0.0.1:5000/coseno/${v1}`;
    } else {
        swal("Mensaje", "Seleccione una opción", "warning");
        return;
    }

    console.log(`URL generada: ${url}`); // Verifica la URL generada

    fetch(url)
        .then(function (response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Error en la llamada");
            }
        })
        .then(function (texto) {
            console.log(texto);
            var cadena = `<h3>Resultado: ${texto.Resultado}  Operación: ${texto.Operacion}</h3>`;
            contenido.innerHTML = cadena;
            swal("Mensaje", "Proceso realizado correctamente", "success");
        })
        .catch(function (error) {
            console.error(error);
            contenido.innerHTML = `<p>Error: ${error.message}</p>`;
            swal({
                title: "Advertencia",
                text: error.message,
                icon: "warning",
                buttons: true,
                dangerMode: true,
            });
        });
}
