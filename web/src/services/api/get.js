import http from "../../services/api/http";

// Get specific student by id
export async function getStudent(id) {
  return http
    .get(`/student/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

// Get Credentials of Student by ID
export async function getStudentCredentials(id) {
  return http
    .get(`/student/credentials/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

// Get Student for Avaliar page
export async function getStudentAvaliar(id) {
  return http
    .get(`/student/avaliar/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

// Get RM Config
export async function getRmConfig(gender) {
  return http
    .get(`/rm_config/${gender}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

// Return how many of the specified CPF are in the database
export async function countCpfDuplicate(cpf) {
  return http
    .get(`/cpf/${cpf}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}

// Return how many of the specified Email are in the database
export async function countEmailDuplicate(email) {
  return http
    .get(`/email/${email}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}

// Return how many of the specified Phone number are in the database
export async function countPhoneDuplicate(phone_number) {
  return http
    .get(`/phone_number/${phone_number}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}

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

// Get protocol used in antropometry valuation
export async function getAntropometriaProtocol(id) {
  return http
    .get(`/student/antropometria_protocol/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

export async function getPersonalCredentials(id) {
  return http
    .get(`/personal/credentials/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}
