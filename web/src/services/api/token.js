import { encrypt, decrypt } from '../validators/encryption';


export function getExpToken() {
  try {
    const itemStr = localStorage.getItem('token');
    if (!itemStr) {
      return null;
    }

    const item = JSON.parse(itemStr);
    const now = new Date();

    const decryptedExp = decrypt(item.expiry);
    const numericExp = Number(decryptedExp);  // make sure expiry time is number, if not, remove token

    if (!numericExp || now.getTime() > numericExp) {
      localStorage.removeItem('token');
      return null;
    }
    return item.value;
  } catch (e) {
    console.error(e);
    return null;
  }
};

export function setExpToken(tokenValue, ttl) {
  const now = new Date()
  const item = {
    value: tokenValue,
    expiry: now.getTime() + ttl,
  }
  // Encrypt the expiry timestamp before assigning it to the item object
  item["expiry"] = encrypt(item.expiry);

  localStorage.setItem('token', JSON.stringify(item));
};

export function getUserIdSession() {
  try {
    const itemStr = sessionStorage.getItem('u:u');
    if (!itemStr) {
      return null;
    }

    const item = JSON.parse(itemStr);

    const decryptedId = decrypt(item);
    const numberedId = Number(decryptedId)

    if (typeof numberedId !== 'number') {
      localStorage.removeItem('u:u');
      return null;
    }
    return decryptedId;
  } catch (e) {
    console.error(e);
    return null;
  }
};

export function setUserIdSession(id) {
  const item = encrypt(id);

  sessionStorage.setItem('u:u', JSON.stringify(item));
};

export function getUserIdLocal() {
  try {
    const itemStr = localStorage.getItem('user');
    if (!itemStr) {
      return null;
    }

    const item = JSON.parse(itemStr);

    const decryptedId = decrypt(item);
    const numberedId = Number(decryptedId)

    if (typeof numberedId !== 'number') {
      localStorage.removeItem('user');
      return null;
    }
    return decryptedId;
  } catch (e) {
    console.error(e);
    return null;
  }
};

export function setUserIdLocal(id) {
  const item = encrypt(id);

  localStorage.setItem('user', JSON.stringify(item));
};