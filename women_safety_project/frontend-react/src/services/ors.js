import axios from "axios";
import { ORS_API_KEY } from "../config";

export const getRouteGeometry = async (start, end) => {
  const url = "https://api.openrouteservice.org/v2/directions/driving-car";

  const response = await axios.get(url, {
    params: {
      api_key: ORS_API_KEY,
      start: `${start.lng},${start.lat}`,
      end: `${end.lng},${end.lat}`,
    },
  });

  return response.data.features[0].geometry.coordinates;
};
