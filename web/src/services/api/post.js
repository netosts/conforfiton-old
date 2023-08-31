import http from "./http";

export async function postStudent(form) {
  try {
    const response = await http.post("/student", form);
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
