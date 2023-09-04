import http from "./http";

export async function updateAntropometriaProtocol(person_id, value) {
  try {
    const response = await http.put(
      `student/antropometria_protocol/${person_id}`,
      value
    );
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}
