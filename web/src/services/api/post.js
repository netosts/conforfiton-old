import http from './http';

export function postStudent(form) {
  http.post('/student', form).then((res) => {
    console.log('ALUNO CRIADO COM SUCESSO..');
    alert(res.data.data);
    // location.reload();
  }).catch((err) => {
    console.error(err.response.data);
    throw err;
  });
};


export function getToken(payload) {
  return http.post('/user/token', payload)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};


export function postAnamnese(form) {
  http.post(`/anamnese`, form)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err.response);
    throw err;
  });
};