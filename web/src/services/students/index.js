export function getStudent(ID_Pessoa) {
  return axios.get(`/student/${ID_Pessoa}`)
}