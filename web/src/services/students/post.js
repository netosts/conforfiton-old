export function postStudent(axios, form) {
  axios.post('/student', form).then((res) => {
    console.log('ALUNO CRIADO COM SUCESSO..');
    alert(res.data);
  }).catch((err) => {
    console.error(err.response.data);
    throw err;
  });
};