import http from "../../services/api/http";

export async function deleteEvaluation(evaluation_type, evaluation_id) {
  return http
    .delete(`/${evaluation_type}/${evaluation_id}`)
    .then((res) => res.data)
    .catch((err) => {
      console.error(err.response);
      throw err;
    });
}
