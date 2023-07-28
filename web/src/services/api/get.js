// Get specific student by id
export function getStudent(http, ID_Pessoa) {
  return http.get(`/student/${ID_Pessoa}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(`Error: ${err.response.data}; Status: ${err.response.status}`);
    throw err;
  });
};

// Get Credentials of Student by ID
export function getStudentCredentials(http, ID_Pessoa) {
  return http.get(`/student/credentials/${ID_Pessoa}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(`Error: ${err.response.data}; Status: ${err.response.status}`);
    throw err;
  });
};

// Return how many of the specified CPF are in the database
export function countCpfDuplicate(http, cpf) {
  return http.get(`/cpfCnpj/${cpf}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// Return how many of the specified RG in UF are in the database
export function countRgUfDuplicate(http, rg, ufRG) {
  return http.get(`/rg/${rg}/${ufRG}`)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};

// Return how many of the specified Email are in the database
export function countEmailDuplicate(http, dsEmail) {
  return http.get(`/dsEmail/${dsEmail}`)
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