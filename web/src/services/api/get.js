import http from '../../services/api/http';

// Get specific student by id
export function getStudent(id_pessoa) {
  return http.get(`/student/${id_pessoa}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err.response);
    throw err;
  });
};

// Get Credentials of Student by ID
export function getStudentCredentials(id_pessoa) {
  return http.get(`/student/credentials/${id_pessoa}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err.response);
    throw err;
  });
};

// Get Student for Avaliar page
export function getStudentAvaliar(id_pessoa) {
  return http.get(`/student/avaliar/${id_pessoa}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err.response);
    throw err;
  });
};

// Get RM Config
export function getRmConfig(sexo) {
  return http.get(`/rm_config/${sexo}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err.response);
    throw err;
  })
}

// Return how many of the specified CPF are in the database
export function countCpfDuplicate(cpf) {
  return http.get(`/cpf_cnpj/${cpf}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// Return how many of the specified RG in UF are in the database
export function countRgUfDuplicate(rg, uf_rg) {
  return http.get(`/rg/${rg}/${uf_rg}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// Return how many of the specified Email are in the database
export function countEmailDuplicate(ds_email) {
  return http.get(`/ds_email/${ds_email}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// Check if token is valid
// export function getAuthorization(http, token) {
//   return http.get('/user/verify', {
//     headers: {
//       Authorization: 'Bearer ' + token
//     }
//   }).then((res) => res.data)
//     .catch((err) => {
//       console.error(err);
//       throw err;
//     });
// };