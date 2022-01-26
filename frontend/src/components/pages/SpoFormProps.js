import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";

export default function FormPropsTextFields() {
  return (
    <Box
      component="form"
      sx={{
        "& .MuiTextField-root": { m: 1, width: "25ch" },
      }}
      noValidate
      autoComplete="off"
    >
      <div>
        <TextField
          required
          id="outlined-required"
          label="Modul"
          defaultValue="Modulname"
        />

        <TextField
          required
          id="outlined-required"
          label="Studiengang"
          defaultValue="Name"
        />
        <TextField
          required
          id="outlined-required"
          label="Modulepart"
          defaultValue="Veranstaltung"
        />
        <TextField
          required
          id="outlined-required"
          label="Prüfungsart"
          defaultValue="Prüfungsart"
        />
        <TextField
          required
          id="outlined-required"
          label="Modulart"
          defaultValue="Modulart"
        />
        <TextField
          required
          id="outlined-required"
          label="Semester"
          defaultValue="number"
        />
        <TextField
          required
          id="outlined-required"
          label="Ects"
          defaultValue="Punkte"
        />
        <TextField
          required
          id="outlined-required"
          label="Sws"
          defaultValue="Punkte"
        />

        <TextField
          required
          id="outlined-required"
          label="Professor/Instructor"
          defaultValue="Professor"
        />

        <TextField
          required
          id="outlined-required"
          label="Lektüre"
          defaultValue="Lektüre"
        />
      </div>
    </Box>
  );
}
