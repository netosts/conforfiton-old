export function postStudent(axios, form) {
  axios.post('/student', form).then((res) => {
    alert(res.data);
    console.log('ALUNO CRIADO COM SUCESSO..');
    location.reload();
  }).catch((err) => {
    console.error(err);
    throw err;
  });
};