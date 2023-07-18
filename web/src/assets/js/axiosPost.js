export function postStudent(axios, telefoneTransformed, alturaTransformed, pesoTransformed, formattedDate) {
  axios.post('/student', {
    "nmPessoa": nmPessoa.value,
    "ser": "AL", // default: Aluno (AL)
    "tipoPessoa": "F", // default: Pessoa Física (F)
    "cpfCnpj": cpfCnpj.value,
    "rg": rg.value,
    "ufRG": ufRG.value,
    "dtNascimento": dtNascimento.value,
    "dsObs": dsObs.value,
    "dsEmail": dsEmail.value,
    "telefone": telefoneTransformed,
    "altura": alturaTransformed,
    "sexo": sexo.value,
    "fotoAluno": null,
    "peso": pesoTransformed,
    "dtData": formattedDate // current date and time
  }).then((res) => {
    alert(res.data);
    console.log('ALUNO CRIADO COM SUCESSO..');
    location.reload();
  }).catch((err) => {
    console.error(err);
  });
};