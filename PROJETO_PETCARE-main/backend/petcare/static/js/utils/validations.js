export function validarCEP(value){
    let msg = "";
    value = removeCarecteresNaoNumericos(value);

    if (value.length !== 8) {
        msg += "O Cep deve conter 8 carecteres";
    }
    return msg;
}
export function validarCpF(value){
    let msg = "";
    value = removeCarecteresNaoNumericos(value);

    if (value.length !== 11 || /^(\d)\1+$/.test(value)) {
        msg += "O CPF deve conter 11 caracteres.";
    }else{
        let soma = 0;
        for (let i = 0; i < 9; i++) {
            soma += parseInt(value[i]) * (10 - i);
        }
        let primeiroDigito = 11 - (soma % 11);
        primeiroDigito = primeiroDigito >= 10 ? 0 : primeiroDigito;

        if (parseInt(value[9]) !== primeiroDigito) {
            msg += "CPF invalido.";
        }else{
            soma = 0;
            for (let i = 0; i < 10; i++) {
                soma += parseInt(value[i]) * (11 - i);
            }
            let segundoDigito = 11 - (soma % 11);
            segundoDigito = segundoDigito >= 10 ? 0 : segundoDigito;
            if(!(parseInt(value[10]) === segundoDigito)) {
                msg += "CPF invalido.";
            } 
        }
    }
    return msg;
}
export function validarCNPJ(cnpj) {
    // Remover caracteres não numéricos
    cnpj = removeCarecteresNaoNumericos(cnpj);
  
    // Verificar se o CNPJ tem 14 dígitos
    if (cnpj.length !== 14) {
        return "O CPF deve conter 11 caracteres.";
    }
  
    // Impedir CNPJs com números repetidos (exemplo: 11111111111111)
    if (/^(\d)\1{13}$/.test(cnpj)) {
      return "Numeros repetidos";
    }
  
    // Validação do primeiro dígito verificador
    let soma = 0;
    let pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    for (let i = 0; i < 12; i++) {
      soma += cnpj[i] * pesos[i];
    }
    let resto = soma % 11;
    let digito1 = resto < 2 ? 0 : 11 - resto;
  
    // Validação do segundo dígito verificador
    soma = 0;
    pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    for (let i = 0; i < 13; i++) {
      soma += cnpj[i] * pesos[i];
    }
    resto = soma % 11;
    let digito2 = resto < 2 ? 0 : 11 - resto;
  
    // Verificar se os dígitos calculados coincidem com os dígitos informados
    if(cnpj[12] == digito1 && cnpj[13] == digito2) {
        return "";
    }
    return "CNPJ inválido.";
  }
  
export function validarTelefone(value){
    let msg = "";
    value = removeCarecteresNaoNumericos(value);

    if (value.length !== 13) {
        msg += "O telefone deve conter 13 carecteres";
    } 
    return msg;
}
export function validarSenha(value){
    let msg = "";
    if(value.length < 8 || value.length > 16 ) {
        msg += "A senha deve conter entre 8 a 16 carecteres";
    }
    return msg;
}
export function validarConfirmSenha(value, senha){
    let msg = "";
    if(value.trim().length === 0){
        msg += "O campo esta vazio.";
    }
    if(value !== senha){
        msg += "As senhas não são iguais.";
    }
    return msg;
}
export function validarTexto(value){
    let msg = "";
    value = value.trim();
    if (value == "") {
        msg += "O campo esta vazio.";
    }
    return msg;
}
export function removeCarecteresNaoNumericos(value){
    return value.replace(/[^\d]/g, '');
}