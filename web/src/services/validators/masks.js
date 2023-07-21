export function maskCnpj(v) {
  // Remove tudo o que não é dígito
  v = v.replace(/\D/g, "");

  // Limita a string a no máximo 14 dígitos
  v = v.slice(0, 14);

  // Aplica a máscara
  v = v.replace(/^(\d{2})(\d)/, "$1.$2");
  v = v.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3");
  v = v.replace(/\.(\d{3})(\d)/, ".$1/$2");
  v = v.replace(/(\d{4})(\d)/, "$1-$2");

  return v;
}

export function maskCpf(v){
  // Remove tudo o que não é dígito
  v = v.replace(/\D/g, "");

  // Limita a string a no máximo 11 dígitos
  v = v.slice(0, 11);

  // Aplica a máscara
  v = v.replace(/(\d{3})(\d)/, "$1.$2");
  v = v.replace(/(\d{3})(\d)/, "$1.$2");
  v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

  return v;
}

export function maskRg(v) {
  v = v.replace(/\D/g, "");
  v = v.slice(0, 19);

  return v;
}