const inputSenha = document.getElementById("senha");
const icone = document.getElementById("toggleSenha");

function atualizarIcone() {
    if (inputSenha.value === "") {
        icone.textContent = "lock"; // vazio → fechado
    } else if (inputSenha.type === "password") {
        icone.textContent = "lock_open"; // oculto com texto → aberto
    } else {
        icone.textContent = "lock"; // visível → fechado
    }
}

// estado inicial
atualizarIcone();

// quando digita
inputSenha.addEventListener("input", atualizarIcone);

// quando clica
icone.addEventListener("click", () => {
    if (inputSenha.value !== "") {
        inputSenha.type = inputSenha.type === "password" ? "text" : "password";
        atualizarIcone();
    }
});