import axios from 'axios';
import { getExpToken } from './token';

const http = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
});

http.interceptors.request.use((request)=>{
  const token = getExpToken();
  if (!token) {
    localStorage.removeItem('user');
  } else {
    request.headers.Authorization = `Bearer ${token}`;
  }
  return request;
});

export default http;