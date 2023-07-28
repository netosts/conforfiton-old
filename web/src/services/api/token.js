export function getExpToken() {
  const itemStr = localStorage.getItem('token');
  if (!itemStr) {
    return null;
  }

  const item = JSON.parse(itemStr);
  const now = new Date();

  if (now.getTime() > item.expiry) {
    localStorage.removeItem('token');
    return null;
  }
  return item.value;
};