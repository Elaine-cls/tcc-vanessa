import {makePostRequest, tratamentosDeErros, makeLogin, makeGetRequest, setAuthorizationTokenHeader} from './utils/api-utils.js';
import {redirectTo, showAlert} from './utils/site-utils.js';
import {ROUTES_API, ROUTES_SITE} from './utils/global.js';
import {validarSenha, validarConfirmSenha, validarTexto,validarCEP, validarTelefone, validarCNPJ, removeCarecteresNaoNumericos} from './utils/validations.js';
import {validarCampo, setValidationFeedback, validClass, registrarPrototypes} from './utils/form-utils.js';


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById("registrationForm");

    // Informações da clinica
    const nome_clinica = document.getElementById("nome-clinica");
    const nome_clinica_feecback = document.getElementById("invalid-feedback-nome-clinica");
    const cnpj = document.getElementById("cnpj");
    const cnpj_feedback = document.getElementById("invalid-feedback-cnpj");

    // Informações do endereço da clinica
    const cep = document.getElementById("cep");
    const cep_feedback = document.getElementById("invalid-feedback-cep");
    const estado = document.getElementById("estado");
    const estado_feedback = document.getElementById("invalid-feedback-estado");
    const cidade = document.getElementById("cidade");
    const cidade_feedback = document.getElementById("invalid-feedback-cidade");

    // Informações da pessoa
    const nome = document.getElementById("nome");
    const nome_feedback = document.getElementById("invalid-feedback-nome")
    const especializacao = document.getElementById("especializacao");
    const especializacao_feedback = document.getElementById("invalid-feedback-especializacao");
    const phone = document.getElementById("telefone");
    const phone_feedback = document.getElementById("invalid-feedback-telefone");
    const email = document.getElementById('email');
    const email_feedback = document.getElementById("invalid-feedback-email");
    const password = document.getElementById('password');
    const password_feedback = document.getElementById("invalid-feedback-password");
    const confirmPassword = document.getElementById('confirmPassword');
    const confirm_password_feedback = document.getElementById("invalid-feedback-confirm-password");

    // Placeholder
    const alertplaceholder = document.getElementById("liveAlertPlaceholder");
    
    registrarPrototypes();
    preenchimentoAutomaticoEstadoCidade();
    validarCampo(nome_clinica, nome_clinica_feecback, validarTexto);
    validarCampo(cnpj, cnpj_feedback, validarCNPJ);

    validarCampo(cep, cep_feedback, validarCEP);
    validarCampo(estado, estado_feedback, validarTexto);
    validarCampo(cidade, cidade_feedback, validarTexto);

    validarCampo(nome, nome_feedback, validarTexto);
    validarCampo(especializacao, especializacao_feedback, validarTexto);
    validarCampo(email, email_feedback, validarTexto);
    validarCampo(phone, phone_feedback, validarTelefone);
    validarCampo(password, password_feedback, validarSenha);
    validarCampo(confirmPassword, confirm_password_feedback, (value) => validarConfirmSenha(value, password.value))

    form.validarFormulario(async() => {
        const formData = constructFormData();
        const headers = setAuthorizationTokenHeader();

        await makePostRequest(ROUTES_API.register_clinic,headers,formData, async(response) => {
            if(response.ok){
                await makeLogin(email.value, password.value);
                redirectTo(ROUTES_SITE.clinica_cadastrada);
            }
        }, async (response) => {
            tratamentosDeErros.accounts.register.tratarErroDeEmail(response, (message) => {showAlert(message, 'danger', alertplaceholder)})
        });
    })

    function preenchimentoAutomaticoEstadoCidade(){
        cep.addEventListener("blur", async() => {
            const value = cep.value.replace(/\D/g, "");
    
            if(value.length === 8){
                const url = `https://viacep.com.br/ws/${value}/json/`;
    
                const responseCaseOK = async(response) => {
                    const data = await response.json();
                    if (data.erro){
                        console.log("cep não encontrado.");
                    }
                    estado.value = data.uf || "";
                    cidade.value = data.localidade || "";
                    estado.setCustomValidity("");
                    cidade.setCustomValidity("");
                    setValidationFeedback(estado_feedback, estado.validationMessage);
                    setValidationFeedback(cidade_feedback, cidade.validationMessage);
                    validClass(estado);
                    validClass(cidade);
                }
                const responseCaseError = (resonse) => {
                    console.log("Erro ao buscar cep");
                }
    
                await makeGetRequest(url, {},responseCaseOK, responseCaseError)
            }
        })
    }

    function constructFormData(){
        return {
            vet: {
                account: {
                    email: email.value,
                    password: password.value
                },
                name: nome.value,
                phone: removeCarecteresNaoNumericos(phone.value),
                specialization: especializacao.value
            },
            address: {
                city: cidade.value,
                state: estado.value,
                country: "Brasil",
                cep: removeCarecteresNaoNumericos(cep.value)
            },
            name: nome_clinica.value,
            cnpj: removeCarecteresNaoNumericos(cnpj.value)
        }
    }

});
