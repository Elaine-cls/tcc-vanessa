import {tratamentosDeErros, user_is_vet_registered} from './utils/api-utils.js';

user_is_vet_registered((response) => {}, (response) => {
    tratamentosDeErros.vet.is_not_a_vet(response)
})