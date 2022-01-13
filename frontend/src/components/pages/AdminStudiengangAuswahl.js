import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export default function AdminStudiengangAuswahl() {
  return (
    <Box sx={{ width: '100%', maxWidth: 650 }}>
     
      <Typography variant="h6" gutterBottom component="div">
        Wählen Sie einen Studiengang aus!
      </Typography>
           
      <Stack spacing={2} direction="column">
      
      <Button variant="contained">Wirtschaftsinformatik und digitale Medien</Button>
      <Button variant="contained">Online-Medien-Management</Button>

      </Stack>
    </Box>
  );
}
