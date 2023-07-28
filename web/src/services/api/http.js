import axios from 'axios';
import { getExpToken } from './token';

const http = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
});

http.interceptors.request.use((request)=>{
  const token = getExpToken();
  const user = localStorage.getItem('user');
  if (!token && user) {
    localStorage.removeItem('user');
    location.reload();
  }
  return request;
});

export default http;