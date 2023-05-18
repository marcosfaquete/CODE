type usuario = {
    idade: number
}

function mostraIdadeDoUsuario(usuario) {
    return usuario.idade
}

const usuario = {
    name: "Marcos",
    idade: 31
}

mostraIdadeDoUsuario(usuario);

const usuario2 = {
    name: "Diego",
}

mostraIdadeDoUsuario(usuario2);

console.log('Hello')