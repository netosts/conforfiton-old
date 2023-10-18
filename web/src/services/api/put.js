import http from "./http";

export async function updateAntropometriaProtocol(person_id, value) {
  try {
    const response = await http.put(
      `/antropometria/protocol/${person_id}`,
      value
    );
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function updateNeuromuscularProtocol(person_id, value) {
  try {
    const response = await http.put(
      `/neuromuscular/protocol/${person_id}`,
      value
    );
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function updateCardioProtocol(person_id, value) {
  try {
    const response = await http.put(`/cardio/protocol/${person_id}`, value);
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function editStudent(person_id, form) {
  try {
    const response = await http.put(`/student/${person_id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function updateMorphofunctional(person_id, form) {
  try {
    const response = await http.put(
      `/anamnese/morphofunctional/${person_id}`,
      form
    );
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function updateAnamnese(person_id, form) {
  try {
    const response = await http.put(`/anamnese/${person_id}`, form);
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

export async function usedLinkShare(salt_link) {
  try {
    const response = await http.put(`/link_share/${salt_link}`, {
      status: "Used",
    });
    return response.data;
  } catch (err) {
    console.error(err.response);
    throw err;
  }
}

// export async function expireLinkShare(salt_link) {
//   try {
//     const response = await http.put(`/link_share/${salt_link}`, {
//       status: "Expired",
//     });
//     return response.data;
//   } catch (err) {
//     console.error(err.response);
//     throw err;
//   }
// }
