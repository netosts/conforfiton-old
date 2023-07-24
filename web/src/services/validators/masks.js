export function maskCnpj(v) {
  // Remove everything that is not a digit
  v = v.replace(/[^0-9]/g, "");

  // Limit the string to a maximum of 14 digits
  v = v.slice(0, 14);

  // Apply the mask
  v = v.replace(/^(\d{2})(\d)/, "$1.$2");
  v = v.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3");
  v = v.replace(/\.(\d{3})(\d)/, ".$1/$2");
  v = v.replace(/(\d{4})(\d)/, "$1-$2");

  return v;
}


export function maskCpf(v){
  // Remove everything that is not a digit
  v = v.replace(/[^0-9]/g, "");

  // Limit the string to a maximum of 11 digits
  v = v.slice(0, 11);

  // Apply the mask
  v = v.replace(/(\d{3})(\d)/, "$1.$2");
  v = v.replace(/(\d{3})(\d)/, "$1.$2");
  v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

  return v;
}


export function maskRg(v) {
  v = v.replace(/[^0-9]/g, "");
  v = v.slice(0, 20);

  return v;
}


export function maskTelefone(v) {
  // Remove everything that is not a digit
  v = v.replace(/[^0-9]/g, "");

  // Limit the string to a maximum of 11 digits
  v = v.slice(0, 11);

  // Apply the mask
  v = v.replace(/^(\d{2})(\d)/, "($1)$2");
  v = v.replace(/(\d{5})(\d)/, "$1-$2");

  return v;
}


export function maskName(v) {
  // Remove everything that is not a letter
  v = v.replace(/[^A-Za-záàâãéèêíïóôõöúçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ\s~]/g, "");

  // Capitalize the first letter of each word
  v = v.replace(/(?:^|\s)\S/g, (char) => char.toUpperCase());

  return v;
}