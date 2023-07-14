// get all cpf/cnpj in database
export function getCpfCnpj(axios) {
  return axios.get(`/cpfCnpj`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// get all rg from specific uf in database
export function getRgUF(axios, ufRG) {
  return axios.get(`/rg/${ufRG}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};