export const variables = {
    localStorageKeyAccessToken : "accessToken"
}

export const HTTP_STATUS = {
    not_acceptable: 406,
    not_authorized: 401,
    bad_request: 400,
    forbidden: 403,
    created: 201,
    ok: 200
}

export const ROUTES_API = {
    login: "/accounts/login/",
    register_account : "/accounts/",
    account_me: "/accounts/me",
    register_owner : "/owner/",
    owner_me: "/owner/me",
    get_pets: "/pet",
    register_pet: "/pet/",
    register_clinic: "/clinic/",
    vet_me: "/vet/me",
    vet_pets: "/vet/pets",
    mirante_create: "/mirante/create-with-mirante/",
}

export const ROUTES_SITE = {
    login: "/login",
    cadastrar_informacoes: "/cadastrar/informacoes",
    cadastrar_conta: "/cadastrar/conta",
    pagina_inicial: "/",
    bem_vindo: "/bemvindo",
    cadastrado_com_sucesso : "/cadastrado",
    meuspets: "/meuspets",
    clinica_cadastrada: "/clinicacadastradacomsucesso",
    painel: "/painel",
    pesquisar_pet: "/pesquisarpet",
}