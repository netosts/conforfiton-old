export function postStudent(http, form) {
  http.post('/student', form).then((res) => {
    console.log('ALUNO CRIADO COM SUCESSO..');
    alert(res.data);
    location.reload();
  }).catch((err) => {
    console.error(err.response.data);
    throw err;
  });
};


export function getToken(http, payload) {
  return http.post('/user/token', payload)
  .then((res) => res.data)
  .catch((err) => {
    console.error(err);
    throw err;
  });
};