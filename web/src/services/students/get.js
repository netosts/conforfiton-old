// get specific student by id
export function getStudent(axios, ID_Pessoa) {
  return axios.get(`/student/${ID_Pessoa}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// this function will return how many of the specified CPF are in the database
export function countCpfDuplicate(axios, cpf) {
  return axios.get(`/cpfCnpj/${cpf}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// this function will return how many of the specified RG in UF are in the database
export function countRgUfDuplicate(axios, rg, ufRG) {
  return axios.get(`/rg/${rg}/${ufRG}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};