import { defineStore } from 'pinia';
import { ref } from 'vue';


export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'));
  const user = ref(localStorage.getItem('user'));

  function setUser(userValue) {
    localStorage.setItem('user', userValue);
    user.value = userValue;
  };

  function setExpToken(tokenValue, ttl) {
    const now = new Date()
    const item = {
      value: tokenValue,
      expiry: now.getTime() + ttl,
    }
    localStorage.setItem('token', JSON.stringify(item));
  };

  function getExpToken() {
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
    return now.getTime();
  };

  return { token, setExpToken, getExpToken, setUser, user };
});