export function postStudent(axios, form) {
  axios.post('/student', form).then((res) => {
    console.log('ALUNO CRIADO COM SUCESSO..');
    alert(res.data);
    location.reload();
  }).catch((err) => {
    console.error(`{Error: ${err.response.data}} {Status: ${err.response.status}}`);
    throw err;
  });
};