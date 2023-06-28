import React, { useEffect, useState } from 'react';
import { Alert, Button, Grid, Paper, TextField, Typography } from "@mui/material";
import './App.css';
import { useApiContext } from 'Contexts/ApiContext';

function App() {
  const [command, setCommand] = useState('')
  const [playerName, setPlayerName] = useState('')

  const {
    initialise,
    playerId,
    message,
    data,
    createPlayer,
    sendCommand,
    apiResponseError,
  } = useApiContext();

  useEffect(() => {
    initialise();
  }, [])

  return (
    <Paper sx={{ m: 2, p: 2, minHeight: '50vh' }}>
      <Grid container spacing={2} sx={{ justifyContent: 'center' }}>
        <Grid item xs={12}>
          <Typography variant="h3">Choose Your Own Adventure!</Typography>
        </Grid>
        {playerId && (
          <Grid item xs={12} sx={{ my: 3 }}>
            <TextField
              fullWidth
              label="Enter your command"
              value={command}
              onChange={(event) => setCommand(event.target.value)}
            />
            <Button
              variant="outlined"
              onClick={() => sendCommand(command)}
            >
              Send Command
            </Button>
          </Grid>
        )}
        <Grid item xs={12} sx={{ m: 1, textAlign: 'left' }}>
          <Typography sx={{ mb: 4 }}>
            {message}
          </Typography>
          {apiResponseError && (
            <Alert severity='error'>
              {apiResponseError}
            </Alert>
          )}
        </Grid>
        {!playerId && (
          <Grid item xs={12} sx={{ my: 3 }}>
            <TextField
              fullWidth
              label="Enter your player name"
              value={playerName}
              onChange={(event) => setPlayerName(event.target.value)}
            />
            <Button
              variant="outlined"
              onClick={() => createPlayer(playerName)}
            >
              Create Player
            </Button>
          </Grid>
        )}
      </Grid>
    </Paper>
  );
}

export default App;
