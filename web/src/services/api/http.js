import axios from "axios";
import { getExpToken, getSecondUserIdLocal, getUserIdLocal } from "./token";

const http = axios.create({
  baseURL: "https://api.hml.conforfiton.com.br",
  withCredentials: true,
});

http.interceptors.request.use((request) => {
  const token = getExpToken();
  const user1 = getUserIdLocal();
  const user2 = getSecondUserIdLocal();
  if ((!token && user1) || user1 != user2) {
    localStorage.removeItem("user");
    localStorage.removeItem("u:u");
    location.reload();
  }
  return request;
});

export default http;
