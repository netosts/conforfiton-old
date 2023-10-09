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

// Get protocol used in neuromuscular valuation
export async function getNeuromuscularProtocol(id) {
  return http
    .get(`/neuromuscular/protocol/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

// Get protocol used in antropometry valuation
export async function getAntropometriaProtocol(id) {
  return http
    .get(`/antropometria/protocol/${id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

// Get protocol used in cardio valuation
export async function getCardioProtocol(id) {
  return http
    .get(`/cardio/protocol/${id}`)
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

export async function getAnamnese(person_id) {
  return http
    .get(`/anamnese/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}

export async function getNeuromuscularStudentPage(person_id) {
  return http
    .get(`/neuromuscular/student/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}
export async function getAntropometriaStudentPage(person_id) {
  return http
    .get(`/antropometria/student/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}
export async function getCardioStudentPage(person_id) {
  return http
    .get(`/cardio/student/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

export async function getOverviewInformation(person_id) {
  return http
    .get(`/anamnese/overview/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}

export async function countCpfDuplicateEditStudent(cpf, person_id) {
  return http
    .get(`/cpf/${cpf}/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}

export async function countEmailDuplicateEditStudent(email, person_id) {
  return http
    .get(`/email/${email}/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}

export async function countPhoneDuplicateEditStudent(phone_number, person_id) {
  return http
    .get(`/phone_number/${phone_number}/${person_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}
