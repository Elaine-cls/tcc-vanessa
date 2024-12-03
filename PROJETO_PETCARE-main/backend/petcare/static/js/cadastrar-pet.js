import {makePostRequest, setAuthorizationTokenHeader, tratamentosDeErros, user_have_register} from "./utils/api-utils.js";
import {registrarPrototypes, validarCampo} from "./utils/form-utils.js";
import {validarTexto} from "./utils/validations.js";
import {ROUTES_API,HTTP_STATUS,ROUTES_SITE} from "./utils/global.js";
import {showAlert, redirectTo} from "./utils/site-utils.js";

user_have_register((response) => {}, (response) => {
  tratamentosDeErros.owner.register.dont_have_register(response);
  tratamentosDeErros.accounts.unauthorized(response, ROUTES_SITE.bem_vindo);
});

document.addEventListener("DOMContentLoaded", async function(){
    const form = document.getElementById("registrationForm");
    const alertplaceholder = document.getElementById("liveAlertPlaceholder");
    const nome = document.getElementById("nome");
    const nome_feedback = document.getElementById("invalid-feedback-nome");
    const raca = document.getElementById("raca");
    const raca_feedback = document.getElementById("invalid-feedback-raca");
    const especie = document.getElementById("especie");
    const especie_feedback = document.getElementById("invalid-feedback-especie");
    const idade = document.getElementById("idade");
    const idade_feedback = document.getElementById("invalid-feedback-idade");
    const genero = document.getElementById("genero");
    const genero_feedback = document.getElementById("invalid-feedback-genero");
    const peso = document.getElementById("peso");
    const peso_feedback = document.getElementById("invalid-feedback-peso");

    validarCampo(nome, nome_feedback, validarTexto);
    validarCampo(raca, raca_feedback, validarTexto);
    validarCampo(especie, especie_feedback, validarTexto);
    validarCampo(idade, idade_feedback, validarTexto);
    validarCampo(genero, genero_feedback, validarTexto);
    validarCampo(peso, peso_feedback, validarTexto);

    registrarPrototypes();

    form.validarFormulario(async() => {
          const formData = constructFormData();
          const headers = setAuthorizationTokenHeader();
          const responseCaseOk = async(response) => {
            if (response.status == HTTP_STATUS.created){
                showAlert("Pet cadastrado com sucesso!", "success", alertplaceholder);
                redirectTo(ROUTES_SITE.meuspets, 2000);
            }
          }
          const responseCaseError = async(response) => {
            const data = await response.json();
            console.log(data);
          }
          await makePostRequest(ROUTES_API.register_pet, headers, formData, responseCaseOk, responseCaseError);
    })

    function constructFormData(){
        return {
            name: nome.value,
            species: especie.value,
            race: raca.value,
            age: idade.value,
            weight: peso.value,
            gender: genero.value
        }
    }

});