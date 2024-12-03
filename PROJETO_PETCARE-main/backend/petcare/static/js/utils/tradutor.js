const messages = [
    {
        id: 0,
        _message: "",
        message : "Erro Desconhecido"
    },
    {
        id: 1,
        _message: "account with this email already exists.",
        message: "Este email já está cadastrado. Você será redirecionado para a página de login."
    },
    {
        id: 2,
        _message: "Credenciais inválidas",
        message: "Credenciais invalidas ou não tem cadastro com este email."
    }

];


export function getMessageOrDefault(message){
    const messageFounded = messages.filter(obj => obj._message == message)
    if (messageFounded.length == 0) return messages[0];
    return messageFounded[0];
}

