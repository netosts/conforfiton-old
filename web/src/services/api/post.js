import http from "./http";

export async function postStudent(form) {
  try {
    const response = await http.post("/student/", form);
    console.log("ALUNO CRIADO COM SUCESSO..");
    return response.data;
  } catch (err) {
    console.error(err.response.data);
    alert(
      `${err.response.status}(${err.response.statusText}): ALUNO NÃO FOI CRIADO`
    );
    throw err;
  }
}

export async function uploadPhoto(file) {
  try {
    const response = await http.post(`/student/photo`, file);
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function getToken(payload) {
  try {
    const response = await http.post("/user/token", payload);
    return response.data;
  } catch (err) {
    console.error(err);
    throw err;
  }
}

export async function postAnamnese(form, email) {
  try {
    const response = await http.post(`/anamnese/${email}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    alert(
      `${err.response.status}(${err.response.statusText}): ANAMNESE NÃO FOI CRIADA`
    );
    throw err;
  }
}

export async function postStudentAnamnese(form, person_id) {
  try {
    const response = await http.post(`/anamnese/student/${person_id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    alert(
      `${err.response.status}(${err.response.statusText}): ANAMNESE NÃO FOI CRIADA`
    );
    throw err;
  }
}

export async function postNeuromuscular(form, id) {
  try {
    const response = await http.post(`/neuromuscular/${id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    alert(
      `${err.response.status}(${err.response.statusText}): NEUROMUSCULAR NÃO FOI CRIADA`
    );
    throw err;
  }
}

export async function postNeuromuscularRml(form, id) {
  try {
    const response = await http.post(`/neuromuscular/rml/${id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    alert(
      `${err.response.status}(${err.response.statusText}): NEUROMUSCULAR RML NÃO FOI CRIADA`
    );
    throw err;
  }
}

export async function postAntropometria(form, id) {
  try {
    const response = await http.post(`/antropometria/${id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    alert(
      `${err.response.status}(${err.response.statusText}): ANTROPOMETRIA NÃO FOI CRIADA`
    );
    throw err;
  }
}

export async function postCardio(form, id) {
  try {
    const response = await http.post(`/cardio/${id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    alert(
      `${err.response.status}(${err.response.statusText}): CARDIORRESPIRATÓRIA NÃO FOI CRIADA`
    );
    throw err;
  }
}

export async function postWeight(id, weight) {
  try {
    const response = await http.post(`/weight/${id}`, weight);
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function newLinkShare(data) {
  return http
    .post(`/link_share/`, data)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
      throw err;
    });
}
