import {makeGetRequest, makePostRequest, setAuthorizationTokenHeader, tratamentosDeErros, user_have_register} from './utils/api-utils.js';
import {redirectTo, showAlert} from './utils/site-utils.js';
import {validarCampo, setValidationFeedback, validClass} from './utils/form-utils.js';
import {validarCEP, validarCpF, validarTexto, validarTelefone} from "./utils/validations.js";
import {removeCarecteresNaoNumericos} from './utils/validations.js';
import {HTTP_STATUS, ROUTES_API, ROUTES_SITE} from './utils/global.js';

user_have_register((response) => { if(response.status == HTTP_STATUS.ok) redirectTo(ROUTES_SITE.pagina_inicial) }, (response) => tratamentosDeErros.accounts.unauthorized(response));

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("registrationForm");
    const name = document.getElementById("nome");
    const cpf = document.getElementById("cpf");
    const phone = document.getElementById("telefone");
    const cep = document.getElementById("cep");
    const estado = document.getElementById("estado");
    const cidade = document.getElementById("cidade");
    const feedback_name = document.getElementById("invalid-feedback-nome");
    const feedback_cpf = document.getElementById("invalid-feedback-cpf");
    const feedback_phone = document.getElementById("invalid-feedback-telefone");
    const feedback_cep = document.getElementById("invalid-feedback-cep");
    const feedback_estado = document.getElementById("invalid-feedback-estado");
    const feedback_cidade = document.getElementById("invalid-feedback-cidade");
    const alertplaceholder = document.getElementById("liveAlertPlaceholder");
    const pais = "Brasil";

    preenchimentoAutomaticoEstadoCidade();
    validarCampo(name, feedback_name, validarTexto);
    validarCampo(cpf, feedback_cpf, validarCpF);
    validarCampo(phone, feedback_phone, validarTelefone);
    validarCampo(cep, feedback_cep, validarCEP);
    validarCampo(estado, feedback_estado, validarTexto);
    validarCampo(cidade, feedback_cidade, validarTexto);
    cadastrarComMirante();

    form.addEventListener("submit", async function (event) {
        event.preventDefault();  

        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add("was-validated");
            return;
        }

        const formData = constructFormData();

        const responseCaseOK = async(response) => {
            if(response.ok){
                redirectTo(ROUTES_SITE.cadastrado_com_sucesso);
            }
        }
        const responseCaseError = async(response) => {
            tratamentosDeErros.owner.register.already_registered(response,(message) => {showAlert(message,"danger",alertplaceholder)})
        }
        await makePostRequest(ROUTES_API.register_owner, setAuthorizationTokenHeader(), formData, responseCaseOK, responseCaseError);
    });

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
                    setValidationFeedback(feedback_estado, estado.validationMessage);
                    setValidationFeedback(feedback_cidade, cidade.validationMessage);
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
    function cadastrarComMirante(){
        document.getElementById("mirante").addEventListener("click", async() => {
            const headers = setAuthorizationTokenHeader();
            const responseCaseOK = async(response) => {
                if(response.ok){
                    redirectTo(ROUTES_SITE.cadastrado_com_sucesso);
                }
            }
            const responseCaseError = async(response) => {
                const data = await response.json();
                console.log(data);
            }

            await makePostRequest(ROUTES_API.mirante_create, headers, {},responseCaseOK,responseCaseError);
        })
    }
    function constructFormData(){
        return {
            address: {
                city: cidade.value,
                state: estado.value,
                country: pais,
                cep: removeCarecteresNaoNumericos(cep.value)
            },
            name: name.value,
            cpf: removeCarecteresNaoNumericos(cpf.value),
            phone: removeCarecteresNaoNumericos(phone.value)
        }
    }
});
