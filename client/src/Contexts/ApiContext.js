import axios from 'axios';
import React, { createContext, useCallback, useContext, useState } from 'react';

export const ApiContext = createContext(null);

export const ApiContextProvider = ({ children }) => {
  const [playerId, setPlayerId] = useState();
  const [message, setMessage] = useState();
  const [data, setData] = useState();

  const [apiResponseError, setApiResponseError] = useState();

  const baseUrl = 'http://localhost:5050';

  const initialise = useCallback(() => {
    setApiResponseError(undefined);

    axios
      .get(`${baseUrl}/`)
      .then((response) => {
        setPlayerId(response.data.player_id);
        setMessage(response.data.message);
        setData(response.data.data);
      })
      .catch((error) => {
        setApiResponseError(error.message);
      })
  }, [baseUrl])

  const sendCommand = useCallback(async (input) => {
    setApiResponseError(undefined);

    const requestData = {
      data: input
    }

    axios
      .post(`${baseUrl}/command`, requestData)
      .then((response) => {
        setPlayerId(response.data.player_id);
        setMessage(response.data.message);
        setData(response.data.data);
      })
      .catch((error) => {
        setApiResponseError(error.message);
      })
  }, [baseUrl])

  return (
    <ApiContext.Provider
      value={{
        initialise,
        playerId,
        message,
        data,
        sendCommand,
        apiResponseError,

      }}
    >
      {children}
    </ApiContext.Provider>
  );
}

export const useApiContext = () => {
  const context = useContext(ApiContext);
  if (context) {
    return context;
  }

  throw Error("API context was not registered");
}