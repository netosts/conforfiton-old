import { reactive } from 'vue';

const storedValues = sessionStorage.getItem('registerStudent')

const defaultValues = {
  name: undefined,
  cpf: undefined,
  gender: undefined,
  role: 'Student',
  email: undefined,
  phone_number: undefined,
  birth_date: undefined,
  height: undefined,
  shirt_size: undefined,
  shorts_size: undefined,
  profile_picture: null,
  weight: undefined,
  created_at: undefined,
  personal_id: undefined,
}

const parsedValues = storedValues ? JSON.parse(storedValues) : defaultValues

export const form = reactive(parsedValues);
