import { reactive } from 'vue';

const form = reactive({
  nm_pessoa: '',
  ser: 'Aluno',
  tipo_pessoa: 'PF',
  cpf_cnpj: '',
  rg: '',
  uf_rg: '',
  emp_personal: false,
  dt_nascimento: '',
  ds_obs: '',
  ds_email: '',
  telefone: '',
  altura: '',
  sexo: '',
  tm_camisa: '',
  foto_aluno: null,
  id_empresa: 1,
  id_personal: 2,
  peso: '',
  dt_data: '',
  ...Object.fromEntries(Array.from({ length: 27 }, (_, i) => [`q${i + 1}`, i + 1 === 13 ? [] : undefined])),
  q4: { treinando: undefined, tempo: undefined },
});

export { form };
