export const schema = {
  name: "required|maxLength:100|name",
  cpf: "required|cpf|maxLength:11",
  phone_number: "required|minLength:11|maxLength:11",
  email: "required|email|maxLength:255",
  birth_date: "required|date",
  gender: "required",
  shirt_size: "required",
  shorts_size: "required",
  height: "required|between:100,250",
  weight: "required|between:0,600",
};
