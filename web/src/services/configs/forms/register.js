import { reactive } from 'vue';

const form = reactive({
  name: undefined,
  cpf: undefined,
  gender: undefined,
  role: 'Studeent',
  email: undefined,
  phone_number: undefined,
  birth_date: undefined,
  height: undefined,
  shirt_size: undefined,
  shorts_size: undefined,
  profile_picture: null,
  weight: undefined,
  company_id: undefined,
  personal_id: undefined,
  ...Object.fromEntries(Array.from({ length: 27 }, (_, i) => [`q${i + 1}`, i + 1 === 13 ? [] : undefined])),
  q4: { treinando: undefined, tempo: undefined },
});

export { form };
