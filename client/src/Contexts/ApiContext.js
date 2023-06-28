import axios from 'axios';
import React, { createContext, useCallback, useContext, useState } from 'react';

export const ApiContext = createContext(null);

export const ApiContextProvider = ({ children }) => {
  const [playerId, setPlayerId] = useState();
  const [message, setMessage] = useState();
  const [data, setData] = useState();

  const [apiResponseError, setApiResponseError] = useState();

  const baseUrl = 'http://localhost:5050';

  const parseCommand = (input) => {
    const singleCommandRegex = /^(\w+)$/;

    let matches = singleCommandRegex.exec(input);
    if (matches) {
      return {
        command: matches[1],
      }
    }

    const targetCommandRegex = /^(\w+)[\w ]*(\w+)$/;
    matches = targetCommandRegex.exec(input);
    if (matches) {
      return {
        command: matches[1],
        arguments: {
          target: matches.length > 1 ? matches[2] : ''
        }
      }
    }

    const multiCommandRegex = /(\w+) [\w ]*(\w+) with [\w ]*(\w+)/;
    matches = multiCommandRegex.exec(input);
    
    return {
      command: matches[1],
      arguments: {
        target: matches.length > 1 ? matches[2] : '',
        weapons: [matches.length > 2 ? matches[3] : '']
      }
    }
  }

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

  const createPlayer = useCallback(async (playerName) => {
    setApiResponseError(undefined);

    const formData = {
      command: 'create_player',
      arguments: {
        name: playerName
      }
    }

    axios
      .post(`${baseUrl}/command`, formData)
      .then((response) => {
        setPlayerId(response.data.player_id);
        setMessage(response.data.message);
        setData(response.data.data);
      })
      .catch((error) => {
        setApiResponseError(error.message);
      })
  }, [baseUrl])

  const sendCommand = useCallback(async (command) => {
    setApiResponseError(undefined);

    const formData = parseCommand(command);

    axios
      .post(`${baseUrl}/command`, formData)
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
        createPlayer,
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