import axios from "axios";
import { getExpToken, getUserIdSession, getUserIdLocal } from "./token";

const http = axios.create({
  baseURL: "http://localhost:8000",
  withCredentials: true,
});

http.interceptors.request.use((request) => {
  const token = getExpToken();
  const user1 = getUserIdLocal();
  const user2 = getUserIdSession();
  if ((!token && user1) || user1 != user2) {
    localStorage.removeItem("user");
    sessionStorage.removeItem("u:u");
    // location.reload();
  }
  return request;
});

export default http;
