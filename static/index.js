document.addEventListener("DOMContentLoaded", () => {
    const buttonLogin = document.querySelector("#login");
    const buttonRegister = document.querySelector("#register");
    const contenido = document.querySelector("#contenedor");

    buttonLogin.addEventListener("click", () => {
        contenido.innerHTML = "";

        contenido.innerHTML = `
            <h1>Iniciar sesion</h1>
            <label for="femail">Correo: </label><br>
            <input type="email" id="femail" name="email"><br><br>
            <button type="button" class="btn btn-secondary">Iniciar sesion</button>
        `;
    });

    buttonRegister.addEventListener("click", () => {
        contenido.innerHTML = "";

        contenido.innerHTML = `
            <h1>Registrarse</h1>
        `
    });
});