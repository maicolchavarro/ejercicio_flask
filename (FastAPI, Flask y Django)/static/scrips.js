async function enviarCotizacion(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = {
        paquete: form.paquete.value,
        personas: form.personas.value,
        email: form.email.value,
        fecha: form.fecha.value
    };

    try {
        const response = await fetch('/cotizar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const resultado = await response.json();
        
        if (response.ok) {
            mostrarResultado(resultado);
        } else {
            alert('Error: ' + resultado.error);
        }
    } catch (error) {
        alert('Error al conectar con el servidor');
    }
}

function mostrarResultado(data) {
    const resultadoDiv = document.getElementById('resultado-cotizacion');
    const detalles = document.getElementById('detalles-cotizacion');
    
    detalles.innerHTML = `
        <strong>Paquete:</strong> ${data.paquete}<br>
        <strong>Personas:</strong> ${data.personas}<br>
        <strong>Fecha:</strong> ${data.fecha}<br>
        <strong>Precio estimado:</strong> $${data.precio.toLocaleString()}<br>
        <strong>Email:</strong> ${data.email}
    `;
    
    resultadoDiv.style.display = 'block';
    document.getElementById('form-cotizacion').reset();
}